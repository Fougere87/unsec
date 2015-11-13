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
    e=Email(mail).clean_body()

    if e == None :
        print(mail)
    else :
        coll.append(e)


print(len(Tools.words_in_collection(coll)))

# print(Tools.term_freq(coll[0]))
# print(Tools.invert_doc_freq(coll))





Tools.vectorize_to_csv(coll, "data.csv")
# print(Tools.vectorize_tf_idf(coll)[1])



#print(e.clean_body())
