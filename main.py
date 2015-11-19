#!/usr/bin/python3
import os
import glob
import begin
from unsec import Email, EmailCollection, Cleaner, TfidfVectorizer, LogicVectorizer
import logging
import random
from unsec import Clusterizer, Cluster



collection = EmailCollection()
collection.add_from_directory("data/bioinfo_2014-01/")

cl = Cleaner()



print(cl.clean(collection[10].get_body() + " ab"))

# print(collection.count())

# engine   = Clusterizer(collection)

# engine.compute(algorithm="kmeans", n_clusters=8)
# clusters = engine.get_clusters()
