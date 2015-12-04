library("jsonlite")

TEST_FOLDER = "test/Log_Hierar_Both_FrEn/"

##Draw graph 
data = read.table(paste(TEST_FOLDER,"clustering.test",sep=""), header=T, sep="\t")

par(mfrow=c(1,3))

plot(data$intra, main="mean Intra distance", type="l", xlab ="number of cluster")
plot(data$extra, main="exta distance", type="l", xlab ="number of cluster")
plot(data$silhouette, main="Silhouette score", type="l", xlab ="number of cluster")

n_cluster = data$n_cluster

file.names <- dir(TEST_FOLDER, pattern =".json$")
for(i in 1:length(file.names)){
filename = paste(TEST_FOLDER,file.names[i], sep = "")
json = fromJSON(filename)

data = json$clusters$count
#combi = sort(c(data, rep(0,length(n_cluster) - length(data))), decreasing = T)

append = rep(0,length(n_cluster) +1 - length(data))
combi   = sort(c(data, append), decreasing = T)

print(combi)

png(filename=paste(filename,".png", sep=""))
barplot(combi, main=paste("n = ", n_cluster[i]), ylim = c(0,500))
dev.off()
}
