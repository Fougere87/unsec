import unsec
from unsec.vectorizer import *
from unsec.algorithm import *

# print console output
DEBUG      = True
# place of emails to clusterize
PATH       = "data/complete"
# number of clusters
N_CLUSTERS = 4
# apply clustering on body, subject or both
TARGET     = "body"
# filter by language
# LANG       = "fr"
# Which Vectorizer to use : LogicalVectorizer or TfidfVectorizer
VECTORIZER = TfidfVectorizer()
# which algorithm to use : SKMeanAlgo or HierarchicalAlgo
ALGORITHM  = SKMeanAlgo()
# Results output file
JSON_FILE  = "clustering.json"

ENABLE_TEST = True
TEST_CLUSTERING_RANGE = range(2,25)
TEST_FOLDER = "test/TFCl_SK_Body_FrEn"
