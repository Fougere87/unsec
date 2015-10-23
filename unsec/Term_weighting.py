

def term_frequ(bow) : #bow is the bag of word
    '''returns a dictionnary with the tf of each word (as a key) as a value'''
    return {word:bow.count(word)  for word in bow}

def invert_doc_freq(collection) :
    '''returns a dict with the invert doc frequency of each term in the collection'''
    d = len(collection)
    total = set([w for doc in collection for w in doc])
    idf = {}
    for w in total :
        for doc in collection :
            if w in doc :
                idf[w] = idf.get(w,0) +1
    for 
    return idf

def tf_idf(tf,idf)


bow1 =['bonjour','truc','comment','bonjour','manger','argent','courses','légume','soleil','ratatouille','été','soupe','hasard']
bow2 = ['hugo','cafe','thé','chocolat','café','ostiane','enervé','soleil','sommeil','nana','fatigue','ratatouille','code','python']
bow3 = ['café','clope','caca','chocolat','magnesium', 'antidepresseur','joint','schizophrénie','psychiatre']
collection = [bow1,bow2,bow3]
print(term_frequ(bow1))
print(invert_doc_freq(collection))
