from unsec.algorithm import Algo
from unsec.vectorizer import Vectorizer
from unsec import Cleaner, tools
from unsec import EmailCollection, Email
from sklearn import metrics
import logging
import json
import datetime
import numpy as np

class Clusterizer(object):

    def __init__(self, email_collection: EmailCollection, target = "body",
                 vectorizer = None,
                 algorithm  = None):
        """
        Create a clusterizer object
        @arg string email_collection    this should be an EmailCollection
        """
        # Input Source email Collection to clusterize
        self.email_collection = email_collection
        # List of text to clusterize
        self.raws        = []
        # Output Clusterized collections of email
        self.clusters    = []
        # Current clustering algorithm
        self.algorithm   = algorithm
        # Current vectorizer
        self.vectorizer  = vectorizer
        # Current Cleaner
        self.cleaner     = Cleaner()
        # Clusters ID
        self.labels      = []
        # Email subject or Email body as the target of analysis
        self.target      = target
        self.log         = logging.getLogger(__name__)
        self.target_factor = 1

    def set_algorithm(self, algorithm: Algo) :
        """ set Algo to use """
        self.algorithm = algorithm

    def set_vectorizer(self, vectorizer: Vectorizer) :
        """ set Vectorizer to use """
        self.vectorizer  = vectorizer

    def run_vectorizer(self):
        """ start vectorizer """
        self.log.info(str(self.vectorizer.__class__.__name__)+" running ...")
        # fill te vectorizer input
        self.vectorizer.raws = self.raws
        self.vectorizer.vectorize()

        # meta programmation : associate vector to mails
        for index in range(len(self.vectorizer.matrix)):
            self.email_collection[index].vector = self.vectorizer.matrix[index]


    def run_cleaner(self):
        """ clean collection and fill vectorizer """
        self.raws.clear()
        self.log.info("Cleaner running (target: "+self.target+")")
        for email in self.email_collection:
            source = str()

            if self.target == "both":
                subject_clean = self.cleaner.clean(email.get_subject())
                body_clean    = self.cleaner.clean(email.get_body())

                len_subject   = len(subject_clean.split(" "))
                len_body      = len(body_clean.split(" "))

                # compute coef
                coef = int(len_body / len_subject * self.target_factor)
                add  = " ".join(subject_clean.split(" ") * coef)

                clean = body_clean + " " + add





            else:
                if self.target == "subject":
                    source = email.get_subject()
                if self.target == "body":
                    source = email.get_body()
                clean = self.cleaner.clean(source)

            self.raws.append(clean)
            email.clean = clean   # Meta programmation ! Create new variable



    def run_algorithm(self):
        self.log.info(str(self.algorithm.__class__.__name__)+" running ...")
        self.labels = self.algorithm.run(self.vectorizer.matrix)
        # self.groups = self.order_groups(self.groups)
        self.compute_clusters()



    def compute(self):

        self.log.info("Start clustering on collection {} emails".format(self.email_collection.count()))
        self.run_cleaner()
        self.run_vectorizer()
        self.run_algorithm()

        self.show_log()



    def show_log(self):

        s_scores = self.silhouette_samples()
        self.log.info("Results : ")
        for index in range(len(self.clusters)):
            self.log.info("\t{} email(s)\t[{:5}]  [{:5}] ".format(
                self.clusters[index].count(),
                round(self.clusters[index].get_similarity(),3),
                round(s_scores[index],2)))




        self.log.info("total silhouette score: {:5}".format(round(self.silhouette_score(),3)))
        self.log.info("total linkage score:    {:5}".format(round(self.cluster_linkage(),3)))



    def cluster_linkage(self):
        centroids = []
        for coll in self.clusters:
            centroids.append(coll.get_centroid())

        ref = centroids[0]
        return tools.avg_distance(centroids, ref)

    def silhouette_score(self):
        array = np.array(self.vectorizer.matrix)
        return metrics.silhouette_score(array, self.labels, metric='cosine')


    def silhouette_samples(self):
        array = np.array(self.vectorizer.matrix)
        return metrics.silhouette_samples(array, self.labels, metric='cosine')





    def compute_clusters(self):
        '''To recover the docs by cluster'''

        self.log.info("Compute Email clustering ...")
        n_cluster = (max(self.labels))
        self.clusters = [EmailCollection("cluster_"+str(i)) for i in range(n_cluster+1)]

        for index in range(len(self.labels)):
            gid = self.labels[index]
            self.clusters[gid].add_email(self.email_collection[index])


    def to_json(self):
        data   = {}
        meta   = {}

        meta["date"]            = datetime.datetime.now().isoformat()
        meta["collection_size"] = self.email_collection.count()
        meta["target"]          = self.target
        meta["cluster_count"]   = len(self.clusters)
        meta["vectorizer"]      = self.vectorizer.__class__.__name__
        meta["algorithm"]       = self.algorithm.__class__.__name__
        meta["linkage"]         = self.cluster_linkage()



        clusters = []
        for index in range(len(self.clusters)):
            cluster  = {}
            cluster["count"] = self.clusters[index].count()
            cluster["files"] = []
            cluster["similarity"] = self.clusters[index].get_similarity()
            for email in self.clusters[index]:
                e = {}
                e["filename"] = email.filename
                e["subject"]  = email.get_subject()
                cluster["files"].append(e)

            clusters.append(cluster)



        data["meta"] = meta
        data["clusters"] = clusters

        return json.dumps(data)


    def print_table(self):
        for index in range(len(self.clusters)):
            for email in self.clusters[index]:
                print(email.get_name(), self.clusters[index].name, sep="\t")







