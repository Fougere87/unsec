#!/usr/bin/python3
import os
import glob
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from unsec import Email, EmailCollection, Cleaner, TfidfVectorizer, LogicVectorizer
from unsec import Clusterizer, Cluster, SmallEmailCollection
import unsec
print("test")


collection = EmailCollection()

collection.add_from_directory(unsec.MEDIUM_DATASET_PATH)


for i in collection:
    print(i.get_subject())

print(collection.count())



# print(collection.count())

# engine   = Clusterizer(collection)

# engine.compute(algorithm="kmeans", n_clusters=8)
# clusters = engine.get_clusters()
