#!/usr/bin/python3
import os
import unsec
import logging

from unsec.algorithm import HierarchicalAlgo, KMeanAlgo, SKMeanAlgo
from unsec.vectorizer import TfidfVectorizer, LogicVectorizer
from unsec import EmailCollection, TestEmailCollection
from unsec import Clusterizer, Assessor
from unsec import tools

from sklearn import metrics
import numpy as np
import multiprocessing as mp
from threading import Thread






class Test(Thread):
    def __init__(self, k = 3):
        super(Test, self).__init__()
        self.k = 3




    def run(self):
        for i in range(10000):
            a = i ** i




for i in range(10):
    Test().start()








# for i in range(10000):
#     compute(i)





# logging.basicConfig(level=logging.INFO)



# collection = EmailCollection("data/bioinfo_2014-01/")

# # collection.keep_lang("fr")


# engine = Clusterizer(collection,
#                             target         = "body",
#                             algorithm      = HierarchicalAlgo(),
#                             vectorizer     = TfidfVectorizer())

# engine.run_cleaner()
# engine.run_vectorizer()

# for n in range(2,100):


#     engine.algorithm.n_clusters = n
#     engine.run_algorithm()


#     intra = sum(engine.cluster_similarity()) / n
#     inter = engine.cluster_linkage()
#     sil   = engine.cluster_silhouette_score()
#     print(n,intra, inter, sil,sep="\t")

# print(tester.categories)



# #collection.keep_lang("fr")


# c = Clusterizer(collection)
# c.set_vectorizer(TfidfVectorizer())
# c.set_algorithm(HierarchicalAlgo(n_clusters=2))

# c.compute()

# c.print_table()


# c.print_table()



# collection = EmailCollection()
# collection.add_from_directory(unsec.LARGE_DATASET_PATH)
# collection.keep_lang("fr")


# engine   = Clusterizer(collection)
# engine.target = "body"
# engine.set_vectorizer(TfidfVectorizer())
# engine.run_cleaner()
# engine.run_vectorizer()


# engine.set_algorithm(HierarchicalAlgo(n_clusters = 4, affinity = "cosine"))

# engine.run_algorithm()
# engine.compute_clusters()


# engine.print_table()
