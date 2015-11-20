import math
import random
from operator import add
from unsec.distance import *




# # #===============================================================

# def barycenter(vectors) :
# 	''' numpy ... I miss you '''
# 	if len(vectors) == 0:
# 		raise ValueError("vectors cannot be empty")
# 	out = [0] * len(vectors[0])
# 	for v in vectors :
# 		out=[sum(x) for x in zip(out, v)]

# 	return [i/len(vectors) for i in out]

# #===============================================================
# def random_vector(vectors):
# 	''' generate a random vectors '''

# 	if len(vectors) == 0:
# 		raise ValueError("Cannot generate from emply vectors")

# 	random_vector = list()
# 	for i in range(len(vectors[0])):
# 		random_vector.append(random.choice(vectors)[i])

# 	return random_vector


# #===============================================================

# def kmeans(vectors, n_clusters=2, max_iter=300, n_init = 10, tol=1e-4):
# 	''' Kmeans clustering '''
# 	print("start kmeans ")

# 	# Check if data is 2 dimensions
# 	if len(vectors) == 0 or len(vectors[0]) == 0:
# 		raise ValueError("data are not well formatted")

# 	# select random clusters
# 	centroids = random.sample(vectors, n_clusters)
# 	results   = [None for i in range(len(vectors))]

# 	for iter in range(max_iter):
# 		distances = []
# 		for v_index in range(len(vectors)):
# 			distances.clear()
# 			for c_index in range(len(centroids)):
# 				distance = euclidian_distance(vectors[v_index], centroids[c_index])
# 				distances.append(distance)

# 			results[v_index] = distances.index(min(distances))


# 		# Compute barycenter
# 		for j in range(len(centroids)):
# 			sub = [vectors[i] for i in range(len(vectors)) if results[i]==j]
# 			centroids[j] = barycenter(sub)
# 	return results

# #===============================================================






# 	''' k is the number of cluster '''
# 	pass
	#  create clusters
	# centroids = [random_vector(vectors) for i in range(k)]
	# clusters =  [list() for i in range(k)]

	# #print("debut ", centroids)

	# iter = 0

	# while iter < 100 :


	# 	for c in centroids :
	# 		for v in c :
	# 			print(v,";", end="")
	# 	print("\n",end="")

	# 	for v_index in range(len(vectors)):
	# 		min_distance = 1000000
	# 		clust_index = 0
	# 		v = vectors[v_index]
	# 		# loop over all centroids and compare with vector
	# 		for index in range(len(centroids)):
	# 			d = euclidian_distance(centroids[index], v)
	# 			# Find the minimum distance
	# 			if min(d, min_distance) == d:
	# 				clust_index = index
	# 				min_distance = d

	# 		clusters[clust_index].append(v)




	# 	# Compute barycenter
	# 	for ci in range(len(clusters)):
	# 		if clusters[ci]:
	# 			centroids[ci] = barycenter(clusters[ci])

	# 	#print("fin ", centroids)
	# 	iter+=1

	#print(clusters[clust_index])

#===============================================================

# def get_clustered_docs(clustering_labels, collection) :
# 	'''To recover the docs by cluster'''
# 	result = [[] for x in range(len(set(clustering_labels)))]
# 	n_lab = 0
# 	for lab in clustering_labels :
# 		result[lab].append(collection[n_lab])
# 		n_lab+=1

