class Algo(object) :
    def __init__(self) :
        self.n_clusters = None
    def run(self, matrix) :
        """ Abstract method to be redefine on each childs """
        raise NotImplemented()
