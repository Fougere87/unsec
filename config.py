import unsec
from unsec.vectorizer import *
from unsec.algorithm import *


DEBUG      = True
PATH       = "data/complete/"
N_CLUSTERS = 19
TARGET     = "both"
LANG       = "fr"
VECTORIZER = TfidfVectorizer()
ALGORITHM  = SKMeanAlgo()
JSON_FILE  = "clustering.json"


