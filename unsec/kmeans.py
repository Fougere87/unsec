from unsec.tools import *

class KMeans(object):
    def __init__(self):
        pass

    def run(vectors, n_clusters=2, max_iter=300, n_init = 10, tol=1e-4):
      ''' Kmeans clustering '''
      print("start kmeans ")

      # Check if data is 2 dimensions
      if len(vectors) == 0 or len(vectors[0]) == 0:
          raise ValueError("data are not well formatted")

      # select random clusters
      centroids = random.sample(vectors, n_clusters)
      results   = [None for i in range(len(vectors))]

      for iter in range(max_iter):
          distances = []
          for v_index in range(len(vectors)):
              distances.clear()
              for c_index in range(len(centroids)):
                  distance = euclidian_distance(vectors[v_index], centroids[c_index])
                  distances.append(distance)

              results[v_index] = distances.index(min(distances))


          # Compute barycenter
          for j in range(len(centroids)):
              sub = [vectors[i] for i in range(len(vectors)) if results[i]==j]
              centroids[j] = barycenter(sub)
      return results
