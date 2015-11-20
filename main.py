import os
import glob
from unsec import Email
from unsec import Tools
from unsec import Collection
from unsec import Clustering
from sklearn import cluster
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from sklearn import  decomposition


collection = EmailCollection()

collection.add_from_directory("data/bioinfo_2014-01")


cleaner = Cleaner("en")

for i in cleaner.clean_collection(collection.get_subjects()):
    print(i)
