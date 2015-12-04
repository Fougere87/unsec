import unsec
from unsec.vectorizer import *
from unsec.algorithm import *

# print console output
DEBUG      = True
# place of emails to clusterize
PATH       = "data/complete"
# number of clusters
N_CLUSTERS = 3
# apply clustering on body, subject or both
TARGET     = "both"
# filter by language
# LANG       = "fr"
# Which Vectorizer to use : LogicalVectorizer or TfidfVectorizer
VECTORIZER = TfidfVectorizer()
# which algorithm to use : SKMeanAlgo or HierarchicalAlgo
ALGORITHM  = HierarchicalAlgo()
# Results output file
JSON_FILE  = "clustering.json"

ENABLE_TEST = False

TEST_CLUSTERING_RANGE = range(2,5)
TEST_FOLDER = "test_folder"
