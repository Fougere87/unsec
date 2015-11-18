
from unsec import Vectorizer
from math import log

class LogicVectorizer(Vectorizer):
    def __init__(self,collection):
        # CALL PARENT CLASS
        super(LogicVectorizer,self).__init__(collection)

# ====================================================================
#   ABSTRACT METHOD TO REDEFINE IN SUBCLASS

    def vectorize(self):
        vectors = []
        space = self.unique_terms()
        for doc in self.collection :
            vector = list()
            for word in space :
                if word in doc :
                    vector.append(True)
                else:
                    vector.append(False)
            vectors.append(vector)

        return vectors
