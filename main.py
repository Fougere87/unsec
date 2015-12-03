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
    log = logging.getLogger(__name__)

else:
    logging.disable(logging.NOTSET)


collection = EmailCollection()
collection.add_from_directory(cfg.PATH)

if hasattr(cfg,"LANG"):
    collection.keep_lang("fr")

engine = Clusterizer(collection)

engine.vectorizer            = getattr(cfg,"VECTORIZER", LogicVectorizer())
engine.algorithm             = getattr(cfg,"ALGORITHM",  HierarchicalAlgo())
engine.algorithm.n_clusters  = getattr(cfg,"N_CLUSTERS", 3)

engine.target                = getattr(cfg,"TARGET", "both")


if getattr(cfg,"ENABLE_TEST", False):
    assert hasattr(cfg,"TEST_CLUSTERING_RANGE"), "TEST_CLUSTERING_RANGE has not been defined"

    test_folder = getattr(cfg,"TEST_FOLDER", "results")
    if not os.path.exists(test_folder):
        os.makedirs(test_folder)

    engine.run_cleaner()
    engine.run_vectorizer()

    with open(test_folder+"/clustering.test","w") as file :
        file.write("n_cluster\tintra\textra\tsilhouette\n")

        for n_cluster in cfg.TEST_CLUSTERING_RANGE:
            print("FUCK ", n_cluster)
            log.info("Clustering with n_cluster : {}".format(n_cluster))

            engine.algorithm.n_clusters = n_cluster
            engine.run_algorithm()
            engine.show_log()

            engine.save_json(test_folder+"/clustering-{}.json".format(n_cluster))
            item = engine.scores()
            file.write("{}\t{}\t{}\t{}\n".format(n_cluster,item[0],item[1],item[2]))


else:
    engine.compute()
    engine.save_json(getattr(cfg,"JSON_FILE", "out.json"))










# print(cl.clean(collection[10].get_body() + " ab"))

# print(collection.count())

# engine   = Clusterizer(collection)

# engine.compute(algorithm="kmeans", n_clusters=8)
# clusters = engine.get_clusters()



# webbrowser.open_new("http://www.google.fr")
