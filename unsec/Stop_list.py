import re


class Stop_list(object):
    def __init__(self, filename):
        self.myfile = self.create_list(filename)


    def create_list(self, filename):
        with open(filename, 'r') as myfile:
            print(myfile.read().split("\n"))
        return(None)
