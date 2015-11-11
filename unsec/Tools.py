import unsec
from nltk import stem
from nltk.stem.snowball import FrenchStemmer
from langdetect import detect
import re
#====================================================================

def stop_list(lang):
	''' return stop list array from file ''' 
	filename = unsec.STOP_LIST_PATH + lang
	try:
		with open(filename, 'r') as myfile:
			mylist = myfile.read().split("\n")
		return(mylist)
	except:
		return []

#====================================================================
def tokenization(raw) :
	''' remove all punctuation caracter ''' 
	tok = re.compile('[,-\\/.\?!;:\"\'\(\)\{\}\[\]\n*\+=]\s*')
	news = tok.sub(" ", raw)
	return news
#====================================================================
def lemmatize(raw, lang) :
	''' Return lemmatization of raw according language. Only french and english are supported'''
	if lang == 'fr':
		stemmer = FrenchStemmer()
	if lang == 'en':
		stemmer = EnglishStemmer() # to be checked

	word_list = re.split('\W+', tokenization(raw))

	lemmatized = [stemmer.stem(word) for word in word_list]
	return " ".join(lemmatized)

#====================================================================
def remove_stopwords(raw, sl) :
	''' remove words from raw which are found in sl list ''' 
	elist = str(raw).split(' ')
	# makes a list of words from the email
	cleaned = [w for w in elist if w.lower() not in sl]
	return ' '.join(cleaned)
# ====================================================================
def clean(raw) :
	''' main function to clean text. Tokenisation + lematization + stop word removed ''' 
	lang   = detect(raw)
	sl     = stop_list(lang)
	result = lemmatize(remove_stopwords(tokenization(raw),sl),lang)
	return result
