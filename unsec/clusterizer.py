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
        self.clusters   = []
        self.algorithm  = None
        self.vectorizer = None
        self.groups     = []
        # self.by = Clusterizer.
        self.cleaner = Cleaner()
    def set_algo(self, algorithm: Algo) :
        self.algorithm = algorithm

    def set_vectorizer(self, vectorizer: Vectorizer) :
        self.vectorizer  = vectorizer

    def compute_vectors(self, verbose = True):
        self.vectorizer.vectorize()

    def compute_cleaner(self, verbose = True):
        raws = []
        for email in self.email_collection:
            raws.append(self.cleaner.clean(email.get_body()))
        self.vectorizer.raws = raws

    def compute(self, verbose = True):
        self.compute_cleaner()
        self.compute_vectors()
        self.groups = self.algorithm.run(self.vectorizer.matrix)
        self.compute_clusters()



    def compute_clusters(self):
        '''To recover the docs by cluster'''
        result = [[] for x in range(len(set(self.groups)))]
        n_lab = 0
        for lab in self.groups :
            result[lab].append(self.email_collection[n_lab])
            n_lab+=1
        self.clusters = result
