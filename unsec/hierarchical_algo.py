from unsec import Algo
from sklearn import cluster


class Hierarch(Algo) :
    def __init__(self, n_clusters = 3):
        super(Hierarch, self).__init__()
        self.n_clusters = n_clusters
        self.centroids = []
        self.distances = []
        self.k_means = None
    def run(self, matrix) :
        self.hierar = cluster.AgglomerativeClustering(n_clusters= self.n_clusters)
        return self.hierar.fit_predict(matrix)
        
