from unsec import Algo
from unsec import Vectorizer
from unsec import Cleaner

class Clusterizer(object):

    def __init__(self, email_collection):
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
        self.target     = "subject"

    def set_algorithm(self, algorithm: Algo) :
        """ set Algo to use """
        self.algorithm = algorithm

    def set_vectorizer(self, vectorizer: Vectorizer) :
        """ set Vectorizer to use """
        self.vectorizer  = vectorizer

    def run_vectorizer(self, verbose = True):
        """ start vectorizer """
        self.vectorizer.vectorize()

    def run_cleaner(self, verbose = True):
        """ clean collection and fill vectorizer """
        raws = []
        for email in self.email_collection:
            source = str()
            if self.target == "subject":
                source = email.get_subject()
            if self.target == "body":
                source = email.get_body()
            raws.append(self.cleaner.clean(source))
        self.vectorizer.raws = raws

    def run_algorithm(self, verbose = True):
        self.groups = self.algorithm.run(self.vectorizer.matrix)


    def compute(self, verbose = True):
        self.run_cleaner()
        self.run_vectorizer()
        self.run_algorithm()
        self.compute_clusters()


    def compute_clusters(self):
        '''To recover the docs by cluster'''
        result = [[] for x in range(len(set(self.groups)))]
        n_lab = 0
        for lab in self.groups :
            result[lab].append(self.email_collection[n_lab])
            n_lab+=1
        self.clusters = result
