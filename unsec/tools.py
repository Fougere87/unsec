from math import *
from decimal import Decimal

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
def variance(vectors):
    center = barycenter(vectors)
    var = 0
    for vector in vectors:
        var += euclidian_distance(vector, center)
    return var
#===============================================================

def avg_distance(vectors, ref_vector, distance_func = euclidian_distance):
    assert len(vectors) >  0, "vectors is empty or"
    distance   = 0

    for vector in vectors:
        distance += distance_func(ref_vector, vector)

    distance = distance /(len(vectors))

    return distance
#===============================================================
def silhouette_samples(X, labels ):

    # PRobably wrong with avg_distance
    samples = []
    for index in range(len(X)):
        vector = X[index]
        label  = labels[index]
        vin    = [X[i] for i in range(len(X)) if labels[i] == label]
        a      = avg_distance(vin, vector)

        list_b = []
        for l in set(labels):
            if l != label:
                vout  = [X[i] for i in range(len(X)) if labels[i] == l]
                list_b.append(avg_distance(vout, vector))

        b = min(list_b)
        s = (b-a) / max(a,b)
        samples.append(s)

    return samples
#===============================================================
def silhouette_score(X, labels ):
    samples = silhouette_samples(X, labels)
    return sum(samples) / len(samples)


#===============================================================
def random_vector(vectors):

    if len(vectors) == 0:
        raise ValueError("Cannot generate from emply vectors")

    random_vector = list()
    for i in range(len(vectors[0])):
        random_vector.append(random.choice(vectors)[i])

    return random_vector
