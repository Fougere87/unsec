from unsec import Algo
from unsec import Vectorizer
from unsec import Cleaner
import logging
import json
import datetime
class Clusterizer(object):

    def __init__(self, email_collection, target = "body"):
        """
        Create a clusterizer object
        @arg string email_collection    this should be an EmailCollection
        """
        self.email_collection = email_collection
        # Contains collection of email collections ex [[a,b], [a,b,c]]
        self.clusters   = []
        self.algorithm  = None
        self.vectorizer = None
        # Contains list of groups for each email ex:[1,2,1,1,2]
        self.groups     = []
        self.cleaner    = Cleaner()
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
        self.vectorizer.vectorize()



    def run_cleaner(self):
        """ clean collection and fill vectorizer """
        raws = []
        self.log.info("Cleaner running (target: "+self.target+")")
        for email in self.email_collection:
            source = str()
            if self.target == "subject":
                source = email.get_subject()
            if self.target == "body":
                source = email.get_body()
            raws.append(self.cleaner.clean(source))
        self.vectorizer.raws = raws

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
            self.log.info("\t[{}] {} email(s)".format(index, len(self.clusters[index])))



    def compute_clusters(self):
        '''To recover the docs by cluster'''

        self.log.info("Compute Email clustering ...")

        result = [[] for x in range(len(set(self.groups)))]
        n_lab = 0
        for lab in self.groups :
            result[lab].append(self.email_collection[n_lab])
            n_lab+=1
        self.clusters = result



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
            cluster["count"] = len(self.clusters[index])
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







