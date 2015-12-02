#!/usr/bin/python3
import os
import logging
import unsec
from sklearn import cluster
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn import metrics
from mpl_toolkits.mplot3d import Axes3D
from sklearn import  decomposition
from sklearn.metrics import pairwise
from sklearn import mixture
import matplotlib.cm as cm
import numpy as np
from unsec import Email, EmailCollection, Cleaner
from unsec.vectorizer import TfidfVectorizer, LogicVectorizer
from unsec.algorithm import  SKMeanAlgo, HierarchicalAlgo
from unsec import Clusterizer
import unsec
# import logging
# logging.basicConfig(level=logging.INFO)

logging.basicConfig(level=logging.INFO)
collection = EmailCollection()
collection.add_from_directory("data/bioinfo_2014-01/")
# collection.keep_lang("fr")


engine   = Clusterizer(collection)
engine.target = "body"
engine.set_vectorizer(TfidfVectorizer())
engine.set_algorithm(HierarchicalAlgo(n_clusters = 30))

engine.compute()

labels = engine.groups
matrix = np.array(engine.vectorizer.matrix)
silhouette_res =  metrics.silhouette_score(matrix, labels, metric='cosine')
print("score silhouette",silhouette_res)

sample_silhouette_values = metrics.silhouette_samples(matrix, labels)
print(sample_silhouette_values)
fig, (ax1, ax2) = plt.subplots(1, 2)
n_clusters =30
y_lower = 10
for i in range(n_clusters):
        # Aggregate the silhouette scores for samples belonging to
        # cluster i, and sort them
        ith_cluster_silhouette_values = \
            sample_silhouette_values[labels == i]

        ith_cluster_silhouette_values.sort()

        size_cluster_i = ith_cluster_silhouette_values.shape[0]
        y_upper = y_lower + size_cluster_i

        color = cm.spectral(float(i) / n_clusters)
        ax1.fill_betweenx(np.arange(y_lower, y_upper),
                          0, ith_cluster_silhouette_values,
                          facecolor=color, edgecolor=color, alpha=0.7)

        # Label the silhouette plots with their cluster numbers at the middle
        ax1.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))

        # Compute the new y_lower for next plot
        y_lower = y_upper + 10  # 10 for the 0 samples

ax1.set_title("The silhouette plot for the various clusters.")
ax1.set_xlabel("The silhouette coefficient values")
ax1.set_ylabel("Cluster label")

plt.show()
# for c in engine.clusters :
#     for e in c :
#         print(e.get_subject())

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
