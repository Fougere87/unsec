import re


class Stop_list(object):
    def __init__(self, filename):
        self.myfile = self.create_list(filename)


    def create_list(self, filename):
        with open(filename, 'r') as myfile:
            print(myfile.read().split("\n"))
        return(None)

    # @staticmethod
    # def create_list(raw):
    #     stop_list = []
    #     for line in raw:
    #         stop_list.append(line)
    #     print(stop_list)
    #     return(stop_list)
    #
    # def create_array(self):
    #     return(Stop_list.create_list(self.stop_words))
