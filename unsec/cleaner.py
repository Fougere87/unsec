# coding: utf8

"""cleaner.py: Cleaner aims to clean string according several. This is a natural language processing"""

__author__      = "Sacha Schutz - Hugo Mayere"
__copyright__   = "Copyright 2009, labsquare"
__license__     = "GPL3"
__email__       = "sacha@labsquare.org"

import unsec
import re
from nltk.stem.snowball import FrenchStemmer, EnglishStemmer
import logging

class Cleaner(object):
    def __init__(self, lang = "fr"):
        """
        Create a cleaner object
        @arg string lang    language used
        """
        self.stop_list       = set()
        self.lang            = lang
        self.regexp_rules    = []

        if self.lang not in ("fr","en"):
            raise ValueError("{} this language is not supported".format(self.lang))

        if self.lang == "fr":
            self.add_stop_list(unsec.STOP_LIST_PATH+"fr")
            self.stemmer = FrenchStemmer()

        if self.lang == "en":
            self.add_stop_list(unsec.STOP_LIST_PATH+"en")
            self.stemmer = EnglishStemmer()


    def add_regexp_rule(self, regexp):
        """
        add a regexp rule. All match will be removed
        @arg re regexp  regular expression
        """
        try:
            reg = re.compile(regexp)
            self.regexp_rules.append(regexp)
        except:
            raise ValueError("wrong regular expression ")



    def add_stop_list(self, filename):
        """
        add stop list element from filename
        @params string filename     a file containing a list of words
        """
        with open(filename,"r") as file:
            for word in file.read().split("\n"):
                self.stop_list.add(word)

    @staticmethod
    def tokenization(raw):
        """
        Remove punctuation caracter from a string
        @arg string raw     the source string
        """
        tok = re.compile('[,-\\/.\?!;:\"\'\(\)\{\}\[\]\n*\+=]\s*')
        news = tok.sub(" ", raw)
        return news

    @staticmethod
    def remove_email(raw) :
        """
        Remove all email adress from a string
        @arg string raw      source string
        """
        return re.sub(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+","",raw)

    @staticmethod
    def remove_url(raw) :
        """
        Remove all url adress from a string
        @arg string raw      source string
        """
        # TODO : remove www.google.fr
        return re.sub(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+","",raw)

    @staticmethod
    def remove_number(raw) :
        """
        Remove all free number from a string
        @arg string raw      source string
        """
        return re.sub(r"\b\d+\b","",raw)

    @staticmethod
    def remove_accent(raw) :
        """
        Replace all accent caracter by the same caracter without accent
        @arg string raw     source string
        """
        raw = re.sub(r"[éèê]","e",raw)
        raw = re.sub(r"[àâ]","a",raw)
        raw = re.sub(r"[ôö]","o",raw)
        raw = re.sub(r"[ïî]","i",raw)

        return raw

    def remove_stopwords(self, raw) :
        """
        Remove all stop worlds from a string
        @arg string raw     source string
        """
        elist = str(raw).split(' ')
        # makes a list of words from the email
        cleaned = [w for w in elist if w.lower() not in self.stop_list]
        return ' '.join(cleaned)

    def remove_shortwords(self, raw, k=2):
        regexp = "\\b\w{1,"+str(k)+"}\\b"
        return re.sub(re.compile(regexp),"",raw)

    def remove_regexp_rules(self, raw ) :
        """
        Remove regexp rules
        """
        for r in self.regexp_rules:
            raw = re.sub(r, "", raw )
        return raw


    def steamming(self, raw) :
        """
        Steem all word from a string
        @arg string raw     source string
        """
        word_list  = re.split('\W+', raw)
        results    = [self.stemmer.stem(word) for word in word_list]
        return " ".join(results)

    def clean(self, raw):
        """
        Clean a string
        @arg string raw     source string
        """
        raw = self.remove_number(raw)
        raw = self.remove_email(raw)
        raw = self.remove_url(raw)
        raw = self.remove_stopwords(self.tokenization(raw))
        raw = self.steamming(raw)
        raw = self.remove_accent(raw)
        raw = self.remove_shortwords(raw,2)
        raw = self.remove_regexp_rules(raw)

        # #REMOVE 2-mers

        # raw = re.sub(r"\s\w{1,2}\s", ' ', raw)

        return raw

    def clean_list(self, l):
        """
        Clean all string from a list
        @arg list       list of string
        """
        for raw in l:
            yield self.clean(raw)
