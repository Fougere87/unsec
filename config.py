import unsec
from unsec.vectorizer import *
from unsec.algorithm import *


DEBUG      = True
PATH       = unsec.SMALL_DATASET_PATH
N_CLUSTERS = 4
VECTORIZER = LogicVectorizer()
ALGORITHM  = HierarchicalAlgo()
JSON_FILE  = "clustering.json"


