import os
import glob
from unsec import Email
from unsec import Tools
from unsec import Collection
from unsec import Clustering

#Tools.vectorize("data/bioinfo_2014-01")
coll = ["bonjour je suis suis truc", "j'aime le café", "je suis un chat chat chat"]


Tools.vectorize_to_csv(coll, "data.csv")

# matrix = Tools.vectorize(coll)

# print(Clustering.euclidian_distance(matrix[0], matrix[1]))

# print(matrix[0])
# print(matrix[1])




#print(e.clean_body())
