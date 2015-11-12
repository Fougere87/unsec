import math
import random 
#===============================================================

def manathan_distance(a,b):
	''' a and b are vectors ''' 
	if len(a) != len(b):
		raise ValueError("a and b has not the same size")
	distance = 0
	for i in range(len(a)):
		distance += b[i] - a[i]

	return distance 

#===============================================================

def euclidian_distance(a,b):
	''' a and b are vectors ''' 
	if len(a) != len(b):
		raise ValueError("a and b has not the same size")

	distance = 0
	for i in range(len(a)):
		distance += (b[i] - a[i]) ** 2

	return math.sqrt(distance) 

#===============================================================

def random_vector(vectors):
	''' generate a random vectors ''' 
	random_vector = list()
	for i in range(len(vectors)):
		random_vector.append(random.choice(vectors)[i])
	return random_vector 

	
#===============================================================
