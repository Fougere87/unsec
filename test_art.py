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
# coll = Collection.Email_Collection("data/bioinfo_2014-01/*")
articles =  glob.glob("dataset_test/*txt")
collec = []
art_list = []
for art in articles :
    art_file = open(art, "r")
    art_list.append(art)
    collec.append(art_file.readlines())


# for e in Tools.words_in_collection(coll.all_cleaned_bodies) :
#     print(e)
#     input("plop")
# print(len(Tools.words_in_collection(coll.all_cleaned_body)))
# print(Tools.term_freq(coll[0]))
# print(Tools.invert_doc_freq(coll.all_cleaned_subjects))


# matrix_sub = Tools.vectorize_tf_idf(coll.all_cleaned_subjects) # create data matrix
# matrix_bod = Tools.vectorize_tf_idf(coll.all_cleaned_bodies)

coll2 =[]
for e in collec :
    print(str(e))
    coll2.append(Tools.clean(str(e)))

matrix_art = Tools.vectorize_tf_idf(coll2)
# matrixTest = [[4,2,3], [5,3,2], [12,42,54], [4,1,2], [91,87,7], [41,21,31], [51,13,67], [12,2,4], [4,1,2], [31,31,14]]

k_means = cluster.KMeans(n_clusters=2) #create k-mean objet with n clusters as param

print("K-mean fitting...")
k_means.fit(matrix_art)
print(k_means.labels_)
print("list des documents : ",Clustering.get_clustered_docs(k_means.labels_, art_list))
mat_dist_sub = k_means.fit_transform(matrix_art)
print(mat_dist_sub)
print(k_means.score(matrix_art))
# k_means.fit(matrix_bod)
# print(k_means.labels_)
pca = decomposition.PCA(n_components=3)
reduced_mat_bod = pca.fit(matrix_art).transform(matrix_art)
print(pca.components_)
Tools.matrix_to_csv(matrix_art, Tools.words_in_collection(coll2), "tfidf_art.csv")
# Tools.vectorize_to_csv(coll, "data.csv")
# clusters = Clustering.get_clustered_docs(k_means.labels_,coll.all_cleaned_subjects)
# [print(e) for e in clusters]
# clusters_files = Clustering.get_clustered_docs(k_means.labels_,coll.files_list)
# [print(e) for e in clusters_files]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x_data = [e[0] for e in reduced_mat_bod]
y_data = [e[1] for e in reduced_mat_bod]
z_data = [e[2] for e in reduced_mat_bod]
ax.scatter(x_data, y_data, z_data, depthshade=True)
plt.show()

# Clustering.kmeans(matrix, 3)

# print(Tools.vectorize_tf_idf(coll)[1])



#print(e.clean_body())
