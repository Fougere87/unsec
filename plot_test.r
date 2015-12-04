
file = "test/TFCl_Hierar_Both_Fr/clustering.test"

data = read.table(file, header=T, sep="\t")

par(mfrow=c(1,3))

plot(data$intra, main="mean Intra distance", type="l", xlab ="number of cluster")
plot(data$extra, main="exta distance", type="l", xlab ="number of cluster")
plot(data$silhouette, main="Silhouette score", type="l", xlab ="number of cluster")

