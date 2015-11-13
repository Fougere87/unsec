import os
cdir=  "data/bioinfo_2014-01/"
dir_cont = [file for file in os.walk("data/bioinfo_2014-01/")][0][2]
print(dir_cont)
recoded_docs = [doc for doc in dir_cont if 'recoded' in doc ]
coll = []
for doc in recoded_docs :
    cdoc = open(cdir+doc, "r")
    coll.append("".join(cdoc.readlines()))
[print(doc) for doc in coll]# print(recoded_docs)
