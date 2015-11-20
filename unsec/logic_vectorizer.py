
from unsec import Vectorizer
from math import log

class LogicVectorizer(Vectorizer):
    def __init__(self):
        # CALL PARENT CLASS
        super(LogicVectorizer,self).__init__()

# ====================================================================
#   ABSTRACT METHOD TO REDEFINE IN SUBCLASS

    def vectorize(self):
        vectors = []
        space = self.unique_terms()
        for doc in self.raws :
            vector = list()
            for word in space :
                if word in doc :
                    vector.append(True)
                else:
                    vector.append(False)
            vectors.append(vector)
        self.matrix = vectors
        return vectors
