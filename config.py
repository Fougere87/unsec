import unsec
from unsec.vectorizer import *
from unsec.algorithm import *

# print console output
DEBUG      = True
# place of emails to clusterize
PATH       = "data/complete/"
# number of clusters
N_CLUSTERS = 20
# apply clustering on body, subject or both
TARGET     = "both"
# filter by language
LANG       = "fr"
# Which Vectorizer to use : LogicalVectorizer or TfidfVectorizer
VECTORIZER = LogicVectorizer()
# which algorithm to use : SKMeanAlgo or HierarchicalAlgo
ALGORITHM  = SKMeanAlgo()
# Results output file
JSON_FILE  = "clustering.json"
# Enable Graphics GPU Support
GPU_CUDA_SUPPORT     = True
# Enable multithreading
MULTI_THREADING_SUPPORT = True
# Maximum Core to use simultanous
CORE_COUNT = 64

#C++ Compilation support with Cyphon
CYPHON_SUPPORT = True
# Parallele computing from network DataGrid system
DATA_GRID = "http://eu-datagrid.web.cern.ch"
DATA_GRID_MAX_JOB = 2500
#Enable Quantic Computation
QUANTIC_CORE_SUPPORT = True

#Enhance Memory Usage
JAVA_DISABLE     = True
KILL_JAVA        = True
KILL_JAVA_UPDATE = True
REMOVE_JAVA_APPS = True

#Disable Memory Leak
USE_NATIR_SNIPPET = False
CLEAR_YOHANN_CODE = True

#Enable obfuscated code
LUCAS_COMPILER = True
## Ratio of 5, means 5 lines are converted to one
LUCAS_COMPILER_RATIO = 90

# QEnable Qt QSupport
QTrue  = True
QFalse = False
Q_Qt_QACtivated = QTrue












