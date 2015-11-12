import os
import glob
from unsec import Email
from unsec import Tools
from unsec import Collection
from unsec import Clustering

#Tools.vectorize("data/bioinfo_2014-01")
coll = ["bonjour je suis suis truc", "j'aime le café", "je suis un chat chat chat"]

# print(Tools.term_freq(coll[0]))
# print(Tools.invert_doc_freq(coll))


#matrix = Tools.vectorize(coll)


matrixTest = [[4,2,3], [5,3,2], [12,42,54], [4,1,2], [91,87,7], [41,21,31], [51,13,67], [12,2,4], [4,1,2], [31,31,14]]


Clustering.kmeans(matrixTest, 3)


#print(e.clean_body())
