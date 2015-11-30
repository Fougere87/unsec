#!/usr/bin/python3
import os
import unsec
import logging

from unsec.algorithm import HierarchicalAlgo, KMeanAlgo
from unsec.vectorizer import TfidfVectorizer
from unsec import EmailCollection
from unsec import Clusterizer


logging.basicConfig(level=logging.INFO)


print("salut")



collection = EmailCollection()
collection.add_from_directory(unsec.MEDIUM_DATASET_PATH)

print(collection.count())

collection.keep_lang("fr")

print(collection.count())

c = Clusterizer(collection)
c.set_vectorizer(TfidfVectorizer())
c.set_algorithm(KMeanAlgo(n_clusters=4))

c.compute()

print(c.to_json())



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
