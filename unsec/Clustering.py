import math
import random
from operator import add 
#===============================================================


def manathan_distance(a, b):
	''' a and b are vectors '''
	if len(a) != len(b):
		raise ValueError("a and b has not the same size")
	distance = 0
	for i in range(len(a)):
		distance += b[i] - a[i]

	return distance

#===============================================================


def euclidian_distance(a, b):
	''' a and b are vectors '''
	if len(a) != len(b):
		raise ValueError("a and b has not the same size")

	distance = 0
	for i in range(len(a)):
		distance += (b[i] - a[i]) ** 2

	return math.sqrt(distance)

#===============================================================

def barycenter(vectors) : 
	''' numpy ... I miss you ''' 
	if len(vectors) == 0: 
		raise ValueError("vectors cannot be empty")
	out = [0] * len(vectors[0])
	for v in vectors : 
		out=[sum(x) for x in zip(out, v)]

	return [i/len(vectors) for i in out]

#===============================================================
def random_vector(vectors):
	''' generate a random vectors '''

	if len(vectors) == 0:
		raise ValueError("Cannot generate from emply vectors")

	random_vector = list()
	for i in range(len(vectors[0])):
		random_vector.append(random.choice(vectors)[i])

	return random_vector


#===============================================================

def kmeans(vectors, k):
	''' k is the number of cluster '''
	#  create clusters
	centroids = [random_vector(vectors) for i in range(k)] 
	clusters =  [list() for i in range(k)]

	#print("debut ", centroids)

	iter = 0 

	while iter < 100 : 


		for c in centroids : 
			for v in c : 
				print(v,";", end="")
		print("\n",end="")
			
		for v_index in range(len(vectors)):
			min_distance = 1000000
			clust_index = 0
			v = vectors[v_index]
			# loop over all centroids and compare with vector
			for index in range(len(centroids)):
				d = euclidian_distance(centroids[index], v)
				# Find the minimum distance
				if min(d, min_distance) == d:
					clust_index = index
					min_distance = d

			clusters[clust_index].append(v)




		# Compute barycenter 
		for ci in range(len(clusters)):
			if clusters[ci]:
				centroids[ci] = barycenter(clusters[ci])
				
		#print("fin ", centroids)
		iter+=1

	#print(clusters[clust_index])

