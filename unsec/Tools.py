import unsec
from nltk import stem
from nltk.stem.snowball import FrenchStemmer, EnglishStemmer
from langdetect import detect
import glob


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
	
	if lang == 'en':
		stemmer = EnglishStemmer() # to be checked

	if lang == 'fr':
		stemmer = FrenchStemmer()


	word_list = re.split('\W+', tokenization(raw))

	print(lang)

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
def remove_email(raw) :
	return re.sub(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)","",raw)
# ====================================================================
def remove_url(raw) :
	return re.sub(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+","",raw)
# ====================================================================
def remove_number(raw) :
	return re.sub(r"\s\d+\s","",raw)
# ====================================================================
def remove_accent(raw) :
	raw = re.sub(r"[éèê]","e",raw)
	raw = re.sub(r"[àâ]","a",raw)
	raw = re.sub(r"[ôö]","o",raw)
	raw = re.sub(r"[ïî]","i",raw)

	return raw 

# ====================================================================
def vectorize(directory) :

	words = set()

	for file in glob.glob(directory+"/*.recoded") : 
		print(file)
		e = unsec.Email(file)
		raw =  e.clean_body() 
		if raw is not None :
			for w in e.clean_body().split(" "):
				words.add(w)
		

	print(words)
	print("TINTIN : ",len(words))






# ====================================================================


def clean(raw) :
	''' main function to clean text. Tokenisation + lematization + stop word removed ''' 
	lang   = detect(raw)

	if lang not in ["fr","en"] :
		print("language cannot be detected .. ")
		return None

	raw = remove_number(raw)
	raw = remove_email(raw)
	raw = remove_url(raw)

	sl     = stop_list(lang)
	raw = lemmatize(remove_stopwords(tokenization(raw),sl),lang)
	
	raw = remove_accent(raw)

	#raw = remove_number(raw)


	return raw
