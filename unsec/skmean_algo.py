from unsec import Algo
from sklearn import cluster


class SKMeanAlgo(Algo) :
    def __init__(self, n_clusters = 3):
        super(SKMeanAlgo, self).__init__()
        self.n_clusters = n_clusters
        self.centroids = []
        self.distances = []
        self.k_means = None
    def run(self, matrix) :
        self.k_means = cluster.KMeans(n_clusters= self.n_clusters)
        self.k_means.fit(matrix)
        return self.k_means.labels_
