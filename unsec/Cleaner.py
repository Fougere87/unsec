import unsec
import re
from nltk.stem.snowball import FrenchStemmer, EnglishStemmer

class Cleaner(object):
    def __init__(self, lang = "fr"):
        self.stop_list       = set()
        self.lang            = lang

        if self.lang not in ("fr","en"):
            raise ValueError("{} this language are not supported".format(self.lang))

        if self.lang == "fr":
            self.add_stop_list(unsec.STOP_LIST_PATH+"fr")
            self.stemmer = FrenchStemmer()

        if self.lang == "en":
            self.add_stop_list(unsec.STOP_LIST_PATH+"en")
            self.stemmer = EnglishStemmer()



#============================================================

    def add_stop_list(self, filename):
        with open(filename,"r") as file:
            for word in file.read().split("\n"):
                self.stop_list.add(word)

#============================================================

    @staticmethod
    def tokenization(raw):
        ''' remove all punctuation caracter '''
        tok = re.compile('[,-\\/.\?!;:\"\'\(\)\{\}\[\]\n*\+=]\s*')
        news = tok.sub(" ", raw)
        return news

# ====================================================================

    @staticmethod
    def remove_email(raw) :
        return re.sub(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+","",raw)

# ====================================================================

    @staticmethod
    def remove_url(raw) :
        # TODO : remove www.google.fr
        return re.sub(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+","",raw)

# ====================================================================

    @staticmethod
    def remove_number(raw) :

        return re.sub(r"\b\d+\b","",raw)
# ====================================================================

    @staticmethod
    def remove_accent(raw) :
        raw = re.sub(r"[éèê]","e",raw)
        raw = re.sub(r"[àâ]","a",raw)
        raw = re.sub(r"[ôö]","o",raw)
        raw = re.sub(r"[ïî]","i",raw)

        return raw
# ====================================================================

    def remove_stopwords(self, raw) :
        ''' remove words from raw which are found in sl list '''
        elist = str(raw).split(' ')
        # makes a list of words from the email
        cleaned = [w for w in elist if w.lower() not in self.stop_list]
        return ' '.join(cleaned)
#============================================================

    def steamming(self, raw) :
        word_list  = re.split('\W+', raw)
        results    = [self.stemmer.stem(word) for word in word_list]
        return " ".join(results)


#============================================================
    def clean(self, raw):

        raw = self.remove_number(raw)
        raw = self.remove_email(raw)
        raw = self.remove_url(raw)
        raw = self.remove_stopwords(self.tokenization(raw))
        raw = self.steamming(raw)

        raw = self.remove_accent(raw)
        return raw

#============================================================
    def clean_list(self, l):

        for raw in l:
            yield self.clean(raw)


