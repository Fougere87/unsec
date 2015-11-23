#!/usr/bin/python3
import os
import glob
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from unsec import Email, EmailCollection, Cleaner, TfidfVectorizer, LogicVectorizer
from unsec import Clusterizer, Cluster, SmallEmailCollection, HierarchicalAlgo, SKMeanAlgo
import unsec
import logging



#logging.basicConfig(level=logging.DEBUG)


collection = EmailCollection()

collection.add_from_directory(unsec.MEDIUM_DATASET_PATH)
collection.keep_lang("fr")


c = Clusterizer(collection)
c.set_vectorizer(TfidfVectorizer())
c.set_algorithm(HierarchicalAlgo(n_clusters=2, affinity = "cosine"))

c.compute()


print(c.to_json())


# c.vectorizer.to_csv("out.csv")



# c.groups = c.algorithm.run(c.vectorizer.matrix)

# c.compute_clusters()

# for e in c.clusters[1]:
#     print(e.filename)





# print(collection.count())

# engine   = Clusterizer(collection)

# engine.compute(algorithm="kmeans", n_clusters=8)
# clusters = engine.get_clusters()
