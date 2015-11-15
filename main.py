import os
import glob
from unsec import Email
from unsec import Tools
from unsec import Collection
from unsec import Clustering
from sklearn import cluster

Tools.vectorize("data/bioinfo_2014-01")
coll = Collection.Email_Collection("data/bioinfo_2014-01/.*recoded")
print("Collection créée")



# coll =[]
# mails = glob.glob("data/bioinfo_2014-01/*.recoded")
# for mail in mails :
#     e=Email(mail).clean_body()
#     if e == None :
#         print(mail, "Has no content")
#     else :
#         coll.append(e)


# print(len(Tools.words_in_collection(coll.all_cleaned_body)))
# print(Tools.term_freq(coll[0]))
# print(Tools.invert_doc_freq(coll))
matrix = Tools.vectorize_tf_idf(coll.all_cleaned_subjects) # create data matrix
matrixTest = [[4,2,3], [5,3,2], [12,42,54], [4,1,2], [91,87,7], [41,21,31], [51,13,67], [12,2,4], [4,1,2], [31,31,14]]

k_means = cluster.KMeans(n_clusters=3) #create k-mean objet with n clusters as param
print("K-mean fitting...")
k_means.fit(matrix)

print(k_means.labels_)
# Tools.vectorize_to_csv(coll, "data.csv")
# clusters = Clustering.get_clustered_docs(k_means.labels_,coll.all_cleaned_subjects)
# [print(e) for e in clusters]
clusters_files = Clustering.get_clustered_docs(k_means.labels_,coll.files_list)
[print(e) for e in clusters_files]


# Clustering.kmeans(matrix, 3)

# print(Tools.vectorize_tf_idf(coll)[1])



#print(e.clean_body())
