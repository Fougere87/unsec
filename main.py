#!/usr/bin/python3
import os
import glob
import logging
import webbrowser
from sklearn import  decomposition
from unsec import Email, EmailCollection, Clusterizer
from unsec import Cleaner
from unsec.vectorizer import LogicVectorizer
from unsec.algorithm import HierarchicalAlgo
import config as cfg


if cfg.DEBUG is True:
    logging.basicConfig(level=logging.INFO)
else:
    logging.disable(logging.NOTSET)


collection = EmailCollection()
collection.add_from_directory(cfg.PATH)


engine = Clusterizer(collection)

engine.vectorizer            = getattr(cfg,"VECTORIZER", LogicVectorizer())
engine.algorithm             = getattr(cfg,"ALGORITHM",  HierarchicalAlgo())
engine.algorithm.n_clusters  = getattr(cfg,"N_CLUSTERS", 3)


engine.compute()

json_file  = getattr(cfg,"JSON_FILE", "out.json")

with open(json_file,"w") as file:
    file.write(engine.to_json())


print("Done! Paste {} to http://jsonviewer.stack.hu".format(json_file))

# print(cl.clean(collection[10].get_body() + " ab"))

# print(collection.count())

# engine   = Clusterizer(collection)

# engine.compute(algorithm="kmeans", n_clusters=8)
# clusters = engine.get_clusters()



# webbrowser.open_new("http://www.google.fr")
