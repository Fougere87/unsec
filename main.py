import os
import glob
from unsec import Email
from unsec import Tools
from unsec import Collection
from unsec import Clustering

#Tools.vectorize("data/bioinfo_2014-01")
coll = ["bonjour je suis suis truc", "j'aime le café", "je suis un chat chat chat"]

print(Tools.term_freq(coll[0]))
print(Tools.invert_doc_freq(coll))





Tools.vectorize_to_csv(coll, "data.csv")
print(Tools.vectorize_tf_idf(coll)[1])



#print(e.clean_body())
