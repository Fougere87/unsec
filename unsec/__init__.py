import os
STOP_LIST_PATH       = os.path.dirname(__file__)+"/stop_list/"
DATASET_PATH         = os.path.dirname(__file__)+"/dataset/"
LARGE_DATASET_PATH   = os.path.dirname(__file__)+"/dataset/large"
MEDIUM_DATASET_PATH   = os.path.dirname(__file__)+"/dataset/medium"
SMALL_DATASET_PATH   = os.path.dirname(__file__)+"/dataset/small"


from unsec.email import Email
from unsec.email_collection import EmailCollection
from unsec.cleaner import Cleaner
from unsec.vectorizer import Vectorizer
from unsec.tfidf_vectorizer import TfidfVectorizer
from unsec.logic_vectorizer import LogicVectorizer
from unsec.cluster import Cluster
from unsec.algo import Algo
from unsec.skmean_algo import SKMeanAlgo
from unsec.hierarchical_algo import Hierarch
from unsec.clusterizer import Clusterizer
from unsec.kmeans import KMeans
from unsec.cmeans import CMeans
from unsec.tools import *
from unsec.small_email_collection import SmallEmailCollection




