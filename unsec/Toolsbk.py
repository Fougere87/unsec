 # coding=utf-8
import unsec
from nltk import stem
from nltk.stem.snowball import FrenchStemmer
from langdetect import detect
import re
from math import log

#====================================================================

def stop_list(lang):
	filename = unsec.STOP_LIST_PATH + lang
	try:
		with open(filename, 'r') as myfile:
			mylist = myfile.read().split("\n")
		return(mylist)
	except:
		return []

#====================================================================

def tokenization(doc) :
	tok = re.compile('[,-\\/.\?!;:\"\'\(\)\{\}\[\]\n*\+=]\s*')
	news = tok.sub(" ", doc)
	return news
#====================================================================
def lemmatize(doc, lang) :
	''' lemmatization'''
	if lang == 'fr':
		stemmer = FrenchStemmer()
	if lang == 'en':
		stemmer = EnglishStemmer() # to be checked

	word_list = re.split('\W+', tokenization(doc))

	lemmatized = [stemmer.stem(word) for word in word_list]
	return " ".join(lemmatized)

#====================================================================

def remove_stopwords(doc, sl) :
    elist = str(doc).split(' ')
     # makes a list of words from the email
    cleaned = [w for w in elist if w.lower() not in sl]
    return ' '.join(cleaned)
# ====================================================================
def clean(doc) :
	lang = detect(doc)
	sl   = stop_list(lang)
	result = lemmatize(remove_stopwords(tokenization(doc),sl),lang)
	return result

# ====================================================================


def term_freq(doc) : #bow is the bag of word
    '''returns a dictionnary with the tf of each word (as a key) as a value'''
    return {word:doc.count(word)  for word in doc}

# ====================================================================[]


def invert_doc_freq(collection) :
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

# ====================================================================


def tf_idf(doc, collection) :
	c_idf = idf(collection)
	term_frequencies = term_freq(doc)
	ti = {word:term_frequencies[word]*c_idf[word] for word in doc}
	return ti
