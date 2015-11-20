import csv

class Vectorizer(object):
    def __init__(self):
        self.matrix     = None
        self.raws       = None



# ====================================================================
#   ABSTRACT METHOD TO REDEFINE IN SUBCLASS

    def vectorize(self):
        return None

# ====================================================================

    def unique_terms(self):
        return tuple(set([w for raw in self.raws for w in raw.split(" ") if w !='']))

# ====================================================================

    def to_csv(self, filename):
        if self.matrix is None:
            self.matrix = self.vectorize()

        with open(filename,"w") as file:
            writer = csv.writer(file,delimiter="\t")
            writer.writerow(self.unique_terms())
            for vector in self.matrix :
                writer.writerow(vector)
