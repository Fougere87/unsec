
def create_list(filename):
    """
    Allows to read a stop words list.
    IN : The filepath. The field separator is \n
    OUT: Prints a list which contains the stop words (not retained).
    """
    with open(filename, 'r') as myfile:
        mylist = myfile.read().split("\n")
    return(mylist)


def merge_lists(list1, list2):
    new_list = []
    new_list = set(list1 + list2)  # devrait marcher
    return(new_list)

def remove_stopwords(email, *stop_lists) :
    stoplist = e.lang
    elist = e.split(' ') # makes a list of words from the email
    cleanedEmail = list(set(elist) - set(stoplist))
# print(fr1.merge_lists(fr2))
