import re
from nltk.stem.snowball import FrenchStemmer
from langdetect import detect
# from nltk import stem

class Email(object):
    def __init__(self, filename):
        file = open(filename, "r")
        raw = "".join(file.readlines())
        self.subject = Email.extract_subject(raw)
        self.body    = Email.extract_body(raw)
        self.sender  = Email.extract_sender(raw)
        self.lang = Email.language_detection(raw)



    def tokenBody(self) :
        return Email.tokenization(self.body)
    def tokenSubject(self) :
        return Email.tokenization(self.subject)
    def lemmatizeBody(self) :
        '''French only (for now) body lemmatization'''
        stemmer = FrenchStemmer()
        word_list = re.split('\W+', Email.tokenization(self.body))
        lemmatized = [stemmer.stem(word) for word in word_list]
        return " ".join(lemmatized)


    @staticmethod
    def extract_subject(raw):
        ''' extract subject '''
        match = re.search(r"Subject:\s(?P<subject>.+)", raw)
        return match.group("subject")

    @staticmethod
    def extract_body(raw):
        ''' extract body '''
        subj = re.split("Subject:\s.+", raw)
        line = subj[1]
        return line

    @staticmethod
    def extract_sender(raw):
        ''' extract email with a regexp '''
        return "truc@tete.fr"
        # try:
        #     match = re.search(r"From:.*(?P<email>.+@)\s", raw)
        #     return match.group("email")
        # except:
        #     return None

    @staticmethod
    def tokenization(raw) :
        tok = re.compile('[,-\\/.\?!;:\"\'\(\)\{\}\[\]\n*\+=]\s*')
        news = tok.sub(" ", raw)
        return news

    @staticmethod
    def language_detection(raw) :
        return detect(raw)



    def __str__(self):
        return "mail de " + self.sender
