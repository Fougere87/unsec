
def create_list(filename):
    '''
    Allows to read a stop words list and keep it in a list.
    IN : The filepath. The field separator is \n
    OUT: A list which contains the stop words.
    '''
    with open(filename, 'r') as myfile:
        mylist = myfile.read().split("\n")
    return(mylist)


def merge_lists(*arg):
    '''
    Allows to merge n stop words lists.
    IN : n stop words lists.
    OUT: one single list containing all the stop words found in the n stop words lists.
    '''
    new_list = []
    for i in range(len(arg)-1):
        new_list = set(arg[i] + arg[i+1])
    print(len(new_list))
    return(new_list)
