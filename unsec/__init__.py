import os
STOP_LIST_PATH = os.path.dirname(__file__)+"/stop_list/"
DATASET_PATH   = os.path.dirname(__file__)+"/dataset/"


from unsec.email import Email
from unsec.email_collection import EmailCollection
from unsec.cleaner import Cleaner
from unsec.vectorizer import Vectorizer
from unsec.tfidf_vectorizer import TfidfVectorizer
from unsec.logic_vectorizer import LogicVectorizer
from unsec.cluster import Cluster
from unsec.algo import Algo
from unsec.skmean_algo import SKMeanAlgo
from unsec.clusterizer import Clusterizer
from unsec.kmeans import KMeans
from unsec.cmeans import CMeans
from unsec.tools import *
from unsec.small_email_collection import SmallEmailCollection




