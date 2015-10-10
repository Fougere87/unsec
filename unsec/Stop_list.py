
class Stop_list:
    """
    Allows to read, keep in lists, merge lists of stop words.
    """
    def __init__(self, filename):
        self.mylist = self.create_list(filename)


    def read_file(self, filename):
        """
        Allows to read a stop words list.
        IN : The filepath. The field separator is \n
        OUT: Prints a list which contains the stop words (not retained).
        """
        with open(filename, 'r') as myfile:
            print(myfile.read().split("\n"))
        return(None)

    @staticmethod
    def create_list(filename):
        """
        Allows to keep in a list the stop words list.
        IN : The filepath. The field separator is \n
        OUT: A list which contains the stop words (retained in a variable).
        """
        mylist = []
        myfile = open(filename, 'r')
        mylist.append(myfile.read().split("\n"))
        myfile.close()
        print("type ", type(mylist))
        return(mylist)

    def merge_lists(self, list2):
        new_list = []
        new_list = set(self.mylist + list2)  # devrait marcher
        print(new_list)
        return(new_list)
