import os
import glob
from unsec import Email
from unsec import Tools
from unsec import Collection
from unsec import Clustering

#Tools.vectorize("data/bioinfo_2014-01")
coll = []
mails = glob.glob("data/bioinfo_2014-01/*.recoded")
for mail in mails :
    e=Email(mail).clean_subject()
    if e == None :
        print(mail)
    else :
        coll.append(e)


print(len(Tools.words_in_collection(coll)))
# print(Tools.term_freq(coll[0]))
# print(Tools.invert_doc_freq(coll))
matrix = Tools.vectorize(coll)
Tools.vectorize_to_csv(coll, "data.csv")

matrixTest = [[4,2,3], [5,3,2], [12,42,54], [4,1,2], [91,87,7], [41,21,31], [51,13,67], [12,2,4], [4,1,2], [31,31,14]]
Clustering.kmeans(matrix, 3)


Tools.vectorize_to_csv(coll, "data.csv")

# print(Tools.vectorize_tf_idf(coll)[1])



#print(e.clean_body())
