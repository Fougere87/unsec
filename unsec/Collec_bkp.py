from math import log
import os
import Email
class Collection(object) :
    def __init__(self, dir):
        dir_cont = [file for file in os.walk("data/bioinfo_2014-01/")][0][2]
        recoded_docs = [doc for doc in dir_cont if 'recoded' in doc ]
        raws_coll = []
        for doc in recoded_docs :
            cdoc = Email(cdir+doc, "r")
            email_coll.append(cdoc)
        self.subjects = [doc.subject for doc in email_coll]
        self.bodies = [doc.body for doc in email_coll]
        # Et là comment dire que chaque elt de raws_coll est une instance de la classe Email ?
        # [print(doc) for doc in coll]

    # def invert_doc_freq(coll) :
    #       '''returns a dict with the invert doc frequency of each term in the collection'''
    #       d = len(collection)
    #       total = set([w for doc in collection for w in doc])
    #       idf = {}
    #       for w in total :
    #           for doc in collection :
    #               if w in doc :
    #                   idf[w] = idf.get(w,0) +1
    #       for w in idf :
    #           idf[w]=log(d/idf[w])
    #       return idf

    def invert_doc_freq(coll) :
        '''returns a dict with the invert doc frequency of each term in the collection'''
        d = len(collection)
        total = set([w for doc in collection for w in doc])
        idf = {}
        for w in total :
            for doc in collection :
                if w in doc :
                    idf[w] = idf.get(w,0) +1
        for w in idf :
            idf[w]=log(d/idf[w])
        return idf
    #
    # def tf_idf(coll) :
    #     for

#
# bow1 =['bonjour','truc','comment','bonjour','manger','argent','courses','légume','soleil','ratatouille','été','soupe','hasard']
# bow2 = ['hugo','cafe','thé','chocolat','café','ostiane','enervé','soleil','sommeil','nana','fatigue','ratatouille','code','python']
# bow3 = ['café','clope','caca','chocolat','magnesium', 'antidepresseur','joint','schizophrénie','psychiatre']
# collection = [bow1,bow2,bow3]
# print(term_frequ(bow1))
# print(invert_doc_freq(collection))
