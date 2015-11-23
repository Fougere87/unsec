from unsec.algorithm import Algo
import random
from unsec.tools import *
class KMeanAlgo(Algo) :
    def __init__(self, n_clusters = 3, max_iter = 20):
        super(KMeanAlgo, self).__init__()
        self.n_clusters = n_clusters
        self.centroids = []
        self.distances = []
        self.max_iter = max_iter
        self.k_means = None


    def run(self, vectors) :
      # Check if data is 2 dimensions
        if len(vectors) == 0 or len(vectors[0]) == 0:
            raise ValueError("data are not well formatted")


      # select random clusters
        self.centroids = random.sample(vectors, self.n_clusters)
        results   = [None for i in range(len(vectors))]

        for iter in range(self.max_iter ):
            distances = []
            for v_index in range(len(vectors)):
                distances.clear()
                for c_index in range(len(self.centroids)):
                    distance = euclidian_distance(vectors[v_index], self.centroids[c_index])
                    distances.append(distance)

                results[v_index] = distances.index(min(distances))


          # Compute barycenter
        for j in range(len(self.centroids)):
            sub = [vectors[i] for i in range(len(vectors)) if results[i]==j]
            self.centroids[j] = barycenter(sub)

        return results
