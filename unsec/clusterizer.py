class Clusterizer(object):
    def __init__(self, email_collection):
        """
        Create a clusterizer object
        @arg string email_collection    this should be an EmailCollection
        """
        self.email_collection = email_collection
        self.clusters   = []
        self.algorithms = ("cmeans", "kmeans")


    def compute(self, algorithm="kmeans", verbose = True, n_clusters = 8):

        if algorithm not in self.algorithms:
            raise ValueError("algorithm should be kmeans or cmeans" )


        print("compute")


    def get_clusters(self):
        return self.clusters
