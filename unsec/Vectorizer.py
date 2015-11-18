

class Vectorizer(object):
    def __init__(self, collection):
        self.collection = collection


# ====================================================================
#   ABSTRACT METHOD TO REDEFINE IN SUBCLASS

    def vectorize(self):
        return None

# ====================================================================

    def unique_terms(self):
        return tuple(set([w for raw in self.collection for w in raw.split(" ") if w !=""]))

