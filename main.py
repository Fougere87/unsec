import os
import glob
from unsec import Email
from unsec import Tools
from unsec import Collection
from unsec import Clustering
from sklearn import cluster
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from sklearn import  decomposition

# Tools.vectorize("data/bioinfo_2014-01")
coll = Collection.Email_Collection("data/bioinfo_2014-01/*")




matrix_sub = Tools.vectorize_tf_idf(coll.all_cleaned_subjects) # create data matrix
matrix_bod = Tools.vectorize_tf_idf(coll.all_cleaned_bodies)
# Tools.matrix_to_csv(matrix_bod, Tools.words_in_collection(coll.all_cleaned_bodies), "tfidf_bod.csv")
k_means = cluster.KMeans(n_clusters=4) #create k-mean objet with n clusters as param

print("K-mean fitting...")
k_means.fit(matrix_sub)
print(k_means.labels_)
# clusters_files = Clustering.get_clustered_docs(k_means.labels_,coll.files_list)
# [print(e) for e in clusters_files]
clusters_files = Clustering.get_clustered_docs(k_means.labels_,coll.files_list)
[print(e) for e in clusters_files]

cluster1 = Clustering.get_clustered_docs(k_means.labels_, coll.all_cleaned_bodies)[0]
cluster2 = Clustering.get_clustered_docs(k_means.labels_, coll.all_cleaned_bodies)[1]
cluster3 = Clustering.get_clustered_docs(k_means.labels_, coll.all_cleaned_bodies)[2]
cluster4 = Clustering.get_clustered_docs(k_means.labels_, coll.all_cleaned_bodies)[3]

mat_cl1 = Tools.vectorize_tf_idf(cluster1)
mat_cl2 = Tools.vectorize_tf_idf(cluster2)
mat_cl3 = Tools.vectorize_tf_idf(cluster3)
mat_cl4 = Tools.vectorize_tf_idf(cluster4)

for 


def get_nmax_elts(listpca, n) :
    sorted_list = sorted(listpca)
    listpca = list(listpca)
    result = []
    for e in sorted_list[:n] :
        result.append(listpca.index(e))
    return(result)
print(get_nmax_elts(pca1.components_[0], 30))



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x_data = [e[0] for e in reduced_mat_cl1]
y_data = [e[1] for e in reduced_mat_cl1]
z_data = [e[2] for e in reduced_mat_cl1]
ax.scatter(x_data, y_data, z_data, depthshade=True)
plt.show()

# Clustering.kmeans(matrix, 3)

# print(Tools.vectorize_tf_idf(coll)[1])



#print(e.clean_body())
