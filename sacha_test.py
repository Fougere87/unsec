#!/usr/bin/python3
import os
import unsec
import logging

from unsec.algorithm import HierarchicalAlgo, KMeanAlgo, SKMeanAlgo
from unsec.vectorizer import TfidfVectorizer
from unsec import EmailCollection, TestEmailCollection
from unsec import Clusterizer, Assessor
from unsec import tools


logging.basicConfig(level=logging.INFO)



collection = TestEmailCollection()






engine = Clusterizer(collection,target="subject",algorithm=HierarchicalAlgo(n_clusters=3), vectorizer = TfidfVectorizer())

engine.compute()







# tester = Assessor(engine)

# tester.compute()




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
