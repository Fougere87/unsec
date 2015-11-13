import unsec
from nltk import stem
from nltk.stem.snowball import FrenchStemmer, EnglishStemmer
from langdetect import detect
from math import log
import glob
import pickle
import csv

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
	return re.sub(r"\b\d+\b","",raw)
# ====================================================================
def remove_accent(raw) :
	raw = re.sub(r"[éèê]","e",raw)
	raw = re.sub(r"[àâ]","a",raw)
	raw = re.sub(r"[ôö]","o",raw)
	raw = re.sub(r"[ïî]","i",raw)

	return raw

# ====================================================================
def vectorize(collection) :
	vectors = []
	space = words_in_collection(collection)
	for doc in collection :
		vector = list()
		for word in space :
			if word in doc :
				vector.append(True)
			else:
				vector.append(False)
		vectors.append(vector)

	return vectors

# ====================================================================





def term_freq(raw) :
    # '''returns a dictionnary with the tf of each word (as a key) as a value'''
	words =  raw.split(" ")
	return {word:words.count(word)  for word in words}

def term_freq2(raw, space) :
    # '''returns a dictionnary with the tf of each word (as a key) as a value'''
	words =  raw.split(" ")
	return [raw.count(word) for word in space]
# ====================================================================


def invert_doc_freq(collection) :
	'''returns a dict with the invert doc frequency of each term in the collection'''
	d = len(collection)
	space = words_in_collection(collection)
	idf = [0]*(len(space))
	n_word = 0
	for w in space :
		for raw in collection :
			if w in raw.split(" ") :
				idf[n_word] += 1
		n_word += 1
	idf = [log(d/w) for w in idf]
	return idf

# ====================================================================


def vectorize_tf_idf(collection) :
	idf = invert_doc_freq(collection)
	space = words_in_collection(collection)
<<<<<<< HEAD
	ti = [[]]*(len(space)-1)
	n_doc = 0
	for doc in collection :
		term_frequencies = term_freq(doc)
		for word in space:
			ti[n_doc] = [term_frequencies[word]*idf[word] if word in doc else 0  for word in space ]
=======
	ti = []
	n_doc = 0
	for doc in collection :
		term_frequencies = term_freq2(doc,space)
		ti.append([term_frequencies[n_word]*idf[n_word] for n_word in range(len(space))])

			# ti[n_doc] = [term_frequencies[word]*idf[word] if word in doc.split(" ") else 0 for word in space ]
		print(n_doc)
>>>>>>> 6c126596b5bcecab815e5421b0cc74b96789e91d
		n_doc +=1

	return ti

# ====================================================================
def words_in_collection(collection) :

	return tuple(set([w for raw in collection for w in raw.split(" ")]))


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
# ====================================================================

def vectorize_to_csv(collection, filename):

	matrix = vectorize_tf_idf(collection)

	with open(filename,"w") as file:
		writer = csv.writer(file,delimiter="\t")
		writer.writerow(words_in_collection(collection))
		for vector in matrix :
			writer.writerow(vector)

# ====================================================================
def vectorize_to_pickle(collection, filename):

	space  = words_in_collection(collection)
	matrix = vectorize(collection)
	all = {"space": space, "matrix": matrix}

	with open(filename, "wb") as file:
		file.write(	pickle.dumps(all)
)
