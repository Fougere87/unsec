#!/usr/bin/python3
import os
import glob
from sklearn import cluster
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from sklearn import  decomposition
from sklearn.metrics import pairwise
from sklearn import mixture
from unsec import Email, EmailCollection, Cleaner, TfidfVectorizer, LogicVectorizer
from unsec import Clusterizer, Cluster, SKMeanAlgo, Hierarch



collection = EmailCollection()
collection.add_from_directory("data/bioinfo_2014-01/")



engine   = Clusterizer(collection)
engine.set_vectorizer(TfidfVectorizer())
engine.compute_cleaner()
engine.compute_vectors()

distances = pairwise.pairwise_distances(engine.vectorizer.matrix, metric ='cosine')
print(distances[:100])

engine.set_algo(Hierarch(n_clusters = 15, affinity = "cosine"))
engine.groups = engine.algorithm.run(engine.vectorizer.matrix)
engine.compute_clusters()
for c in engine.clusters :
    print("CLUSTER====================")
    for e in c :
        print(e)

# print(engine.algorithm.k_means.inertia_)


# for n in range(2,50) :
#     engine.set_algo(SKMeanAlgo(n_clusters = n))
#     engine.groups = engine.algorithm.run(engine.vectorizer.matrix)
#     engine.compute_clusters()
#     print(engine.algorithm.k_means.inertia_)
# #
# matrix_sub = Tools.vectorize_tf_idf(coll.all_cleaned_subjects) # create data matrix
# matrix_bod = Tools.vectorize_tf_idf(coll.all_cleaned_bodies)
# # Tools.matrix_to_csv(matrix_bod, Tools.words_in_collection(coll.all_cleaned_bodies), "tfidf_bod.csv")
# k_means = cluster.KMeans(n_clusters=4) #create k-mean objet with n clusters as param
#
# print("K-mean fitting...")
# k_means.fit(matrix_sub)
# print(k_means.labels_)
# # clusters_files = Clustering.get_clustered_docs(k_means.labels_,coll.files_list)
# # [print(e) for e in clusters_files]
# clusters_files = Clustering.get_clustered_docs(k_means.labels_,coll.files_list)
# [print(e) for e in clusters_files]
#
# cluster1 = " ".join(Clustering.get_clustered_docs(k_means.labels_, coll.all_cleaned_bodies)[0])
# cluster2 = " ".join(Clustering.get_clustered_docs(k_means.labels_, coll.all_cleaned_bodies)[1])
# cluster3 = " ".join(Clustering.get_clustered_docs(k_means.labels_, coll.all_cleaned_bodies)[2])
# cluster4 = " ".join(Clustering.get_clustered_docs(k_means.labels_, coll.all_cleaned_bodies)[3])
#
#
# def ntop_inverse_tf(raw, n) :
#     tab =list(set(raw.split(" ")))
#     l = len(raw.split(" "))
#     result = []
#     counts = [[]for i in range(2)]
#     counts[0]=tab
#     counts[1]=[raw.count(word)/l for word in tab]
#     for j in range(n) :
#         i = counts[1].index(max(counts[1]))
#         result.append(counts[0][i])
#         counts[0].pop(i)
#         counts[1].pop(i)
#     return result
#
# print(ntop_inverse_tf(cluster1, 30))
# print(ntop_inverse_tf(cluster2, 30))
# print(ntop_inverse_tf(cluster3, 30))
# print(ntop_inverse_tf(cluster4, 30))
#
# def get_nmax_elts(listpca, n) :
#     sorted_list = sorted(listpca)
#     listpca = list(listpca)
#     result = []
#     for e in sorted_list[:n] :
#         result.append(listpca.index(e))
#     return(result)



# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# x_data = [e[0] for e in reduced_mat_cl1]
# y_data = [e[1] for e in reduced_mat_cl1]
# z_data = [e[2] for e in reduced_mat_cl1]
# ax.scatter(x_data, y_data, z_data, depthshade=True)
# plt.show()

# Clustering.kmeans(matrix, 3)

# print(Tools.vectorize_tf_idf(coll)[1])



#print(e.clean_body())
