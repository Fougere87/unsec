from unsec.algorithm import Algo
from unsec.vectorizer import Vectorizer
from unsec import Cleaner
from unsec import EmailCollection, Email
import logging
import json
import datetime

class Clusterizer(object):

    def __init__(self, email_collection: EmailCollection, target = "body", vectorizer = None, algorithm = None):
        """
        Create a clusterizer object
        @arg string email_collection    this should be an EmailCollection
        """
        # Input Source email Collection to clusterize
        self.email_collection = email_collection
        # List of text to clusterize
        self.raws       = []
        # Output Clusterized collections of email
        self.clusters   = []
        # Current clustering algorithm
        self.algorithm  = algorithm
        # Current vectorizer
        self.vectorizer = vectorizer
        # Current Cleaner
        self.cleaner    = Cleaner()
        # Clusters ID
        self.groups     = []
        # Email subject or Email body as the target of analysis
        self.target     = target
        self.log        = logging.getLogger(__name__)

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


    def run_cleaner(self):
        """ clean collection and fill vectorizer """
        self.raws.clear()
        self.log.info("Cleaner running (target: "+self.target+")")
        for email in self.email_collection:
            source = str()
            if self.target == "subject":
                source = email.get_subject()
            if self.target == "body":
                source = email.get_body()
            self.raws.append(self.cleaner.clean(source))


    def run_algorithm(self):
        self.log.info(str(self.algorithm.__class__.__name__)+" running ...")
        self.groups = self.algorithm.run(self.vectorizer.matrix)


    def compute(self):

        self.log.info("Start clustering on collection {} emails".format(self.email_collection.count()))
        self.run_cleaner()
        self.run_vectorizer()
        self.run_algorithm()
        self.compute_clusters()

        self.log.info("Results : ")
        for index in range(len(self.clusters)):
            self.log.info("\t[{}] {} email(s)".format(index, self.clusters[index].count()))



    def compute_clusters(self):
        '''To recover the docs by cluster'''

        self.log.info("Compute Email clustering ...")
        n_cluster = (max(self.groups))
        self.clusters = [EmailCollection() for i in range(n_cluster+1)]

        for index in range(len(self.groups)):
            gid = self.groups[index]
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


        clusters = []
        for index in range(len(self.clusters)):
            cluster  = {}
            cluster["count"] = self.clusters[index].count()
            cluster["files"] = []
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
                print(email.filename, index, sep="\t")







