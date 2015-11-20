from math import *
from decimal import Decimal
from random import random

def euclidian_distance(a,b ):
    ''' a and b are vector '''
    if len(a) != len(b):
        raise ValueError("a and b has not the same size ")

    return  sqrt(sum(pow(x-y,2) for x, y in zip(a, b)))

#===============================================================

def manathan_distance(a,b):
    ''' a and b are vector '''
    if len(a) != len(b):
        raise ValueError("a and b has not the same size ")

    return sum(abs(x-y) for x,y in zip(a,b))

#===============================================================

def nth_root(value, n_root):
    root_value = 1/float(n_root)
    return round (Decimal(value) ** Decimal(root_value),3)

def minkowski_distance(x,y,p_value):
    return nth_root(sum(pow(abs(a-b),p_value) for a,b in zip(x, y)),p_value)

#===============================================================
def square_rooted(x):
    return round(sqrt(sum([a*a for a in x])),3)

def cosine_similarity(x,y):
    numerator = sum(a*b for a,b in zip(x,y))
    denominator = square_rooted(x)*square_rooted(y)
    return round(numerator/float(denominator),3)
#===============================================================
def barycenter(vectors) :
    if len(vectors) == 0:
        raise ValueError("vectors cannot be empty")

    out = [0] * len(vectors[0])
    for v in vectors :
        out=[sum(x) for x in zip(out, v)]
    return [i/len(vectors) for i in out]
#===============================================================
def random_vector(vectors):

    if len(vectors) == 0:
        raise ValueError("Cannot generate from emply vectors")

    random_vector = list()
    for i in range(len(vectors[0])):
        random_vector.append(random.choice(vectors)[i])

    return random_vector
