
class Stop_list(object):
    """
    Allows to read, keep in lists, merge lists of stop words.
    """


    def __init__(self, filename):
        self.mylist = self.create_list(filename)


    def create_list(self, filename):
        """
        Allows to read a stop words list.
        IN : The filepath. The field separator is \n
        OUT: Prints a list which contains the stop words (not retained).
        """
        with open(filename, 'r') as myfile:
            mylist = myfile.read().split("\n")
        return(mylist)

    def merge_lists(self, list2):
        new_list = []
        new_list = set(self.mylist + list2)  # devrait marcher
        print(new_list)
        return(new_list)


fr1 = Stop_list("../stop_list/french1")
fr2 = Stop_list("../stop_list/french2")
print(fr1.mylist)
# print(fr1.merge_lists(fr2))
