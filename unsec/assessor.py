import itertools
from unsec import Clusterizer

class Assessor(object):
    def __init__(self, clusterizer : Clusterizer):
        self.clusterizer = clusterizer

        self.total_categories = self._get_total_categories_()
        self.total            = self._get_total_()





    def _get_total_categories_(self):
        categories = {}

        for collection in self.clusterizer.clusters:
            for key, value in collection.get_categories().items():
                if key not in categories:
                    categories[key] = value
                else:
                    categories[key] += value
        return categories

    def _get_total_(self):
        return sum ([collection.count() for collection in self.clusterizer.clusters])


    def compute(self):

        print(self.guess_categories())
        # for collection in self.clusters:
        #     x= sorted(collection.get_categories().items(), key=lambda x: x[1], reverse=True)
        #     print(x)
        # a = self.total_categories.keys()
        # b = range(len(self.clusters))

        # combinaison = list(itertools.product(a,b))

        # print(combinaison)

        # for cat, index in combinaison:
        #     print(cat,"<->",index)
        #     contingency = self.get_contingency_table(cat,index)
        #     sensibility = self.__sensibility__(contingency)
        #     specificity = self.__specificity__(contingency)

        #     print(sensibility, specificity)




    def guess_categories(self):
        pass
        # categories = self.total_categories

        # for index in range(self.clusters):
        #     collection = self.clusters[index]
        #     x= sorted(collection.get_categories().items(), key=lambda x: x[1], reverse=True)

        #     if len(x) > 0:
        #         categories[x[0]]



    def intragroup_distance(self):
        pass




    def get_contingency_table(self, category_name, cluster_index):

    #=======# IN   # OUT  #
    #=======#======#======#
    #TRUE   #  TP  #  FN  #
    #=======#======#======#
    #FALSE  #  FP  #  TN  #
    #=======#======#======#

        data = {}
        all_positif   = self.total_categories[category_name]
        all_negatif   = self.total - all_positif



        collection    = self.clusterizer.clusters[cluster_index]

        data["true_positif"]  = collection.category_count(category_name)
        data["false_positif"] = collection.count() - data["true_positif"]

        data["false_negatif"] = all_positif -  data["true_positif"]
        data["true_negatif"]  = all_negatif -  data["false_positif"]

        return data



    def __sensibility__(self, contingency):
        return contingency["true_positif"] / (contingency["true_positif"] + contingency["false_negatif"] )


    def __specificity__(self, contingency):
        return contingency["true_negatif"] / (contingency["true_negatif"] + contingency["false_negatif"] )






