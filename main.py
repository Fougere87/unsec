import os
import glob
from unsec import Email
from unsec import Tools
from unsec import Collection

#Tools.vectorize("data/bioinfo_2014-01")
coll = ["bonjour je suis suis truc", "j'aime le café", "je suis un chat chat chat"]


Tools.vectorize_to_csv(coll, "binary_matrix.csv")




#print(e.clean_body())
