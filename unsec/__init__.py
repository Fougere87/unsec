import os
STOP_LIST_PATH       = os.path.dirname(__file__)+"/stop_list/"
DATASET_PATH         = os.path.dirname(__file__)+"/dataset/"
LARGE_DATASET_PATH   = os.path.dirname(__file__)+"/dataset/large"
MEDIUM_DATASET_PATH  = os.path.dirname(__file__)+"/dataset/medium"
SMALL_DATASET_PATH   = os.path.dirname(__file__)+"/dataset/small"


from unsec.email import Email
from unsec.email_collection import EmailCollection
from unsec.cleaner import Cleaner
from unsec.clusterizer import Clusterizer

# from unsec.algo import Algo
# from unsec.skmean_algo import SKMeanAlgo
# from unsec.hierarchical_algo import HierarchicalAlgo
from unsec.tools import *
# from unsec.small_email_collection import SmallEmailCollection




