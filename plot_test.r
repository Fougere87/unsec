library("jsonlite")
#
# data = read.table("test/Log_Hierar_Both_FrEn/clustering.test", header=T, sep="\t")
#
# par(mfrow=c(1,3))
#
# plot(data$intra, main="mean Intra distance", type="l", xlab ="number of cluster")
# plot(data$extra, main="exta distance", type="l", xlab ="number of cluster")
# plot(data$silhouette, main="Silhouette score", type="l", xlab ="number of cluster")


SIZE = 30

file.names <- dir("test/TFCl_Hierar_Body_FrEn/", pattern =".json")
for(i in 1:length(file.names)){
  filename = paste("test/TFCl_Hierar_Body_FrEn/",file.names[i], sep = "")
  json = fromJSON(filename)

  data = json$clusters$count
  combi = sort(c(data, rep(0,30 - length(data))), decreasing = T)

  print(data)
  png(filename=paste(filename,".png", sep=""))
  
  barplot(combi, main=paste("n = ", 2+i), ylim = c(0,500))

  dev.off()

}
