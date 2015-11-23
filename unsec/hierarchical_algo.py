from unsec import Algo
from sklearn import cluster


class HierarchicalAlgo(Algo) :
    def __init__(self, n_clusters = 3, affinity = "euclidian"):
        super(HierarchicalAlgo, self).__init__()

        self.n_clusters = n_clusters
        self.centroids = []
        self.distances = []
        self.affinity = affinity
        self.k_means = None
        self.affinity = affinity
    def run(self, matrix) :
        self.hierar = cluster.AgglomerativeClustering(n_clusters= self.n_clusters, affinity =self.affinity, linkage = 'average' )
        return self.hierar.fit_predict(matrix)
