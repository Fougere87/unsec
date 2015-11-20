
from unsec import Vectorizer
from math import log

class TfidfVectorizer(Vectorizer):
    def __init__(self,collection):
        # CALL PARENT CLASS
        super(TfidfVectorizer,self).__init__(collection)

# ====================================================================

    def term_freq(self,raw, space):
        words =  raw.split(" ")
        return [raw.count(word) for word in space]
# ====================================================================

    def invert_doc_freq(self):
        '''returns a list with the invert doc frequency of each term in the collection'''
        d = len(self.collection)
        space = self.unique_terms()
        idf = [0 for x in range(len(space))]
        n_word = 0
        for w in space :
            for raw in self.collection :
                if w in raw.split(" ") :
                    idf[n_word] += 1
            n_word += 1
        idf = [log(d/w) for w in idf]
        return idf

# ====================================================================
#   ABSTRACT METHOD TO REDEFINE IN SUBCLASS

    def vectorize(self):
        print("Vectorizing...")
        idf = self.invert_doc_freq()
        space = self.unique_terms()
        ti = []
        n_doc = 0
        for doc in self.collection :
            term_frequencies = self.term_freq(doc,space)
            ti.append([term_frequencies[n_word]*idf[n_word] for n_word in range(len(space))])
            n_doc +=1
        print("Vectorization done...")
        self.matrix = ti
        return ti
