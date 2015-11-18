import os
import glob
from unsec import Email, EmailCollection, Cleaner, TfidfVectorizer, LogicVectorizer




collection = EmailCollection()

collection.add_from_directory("data/bioinfo_2014-01")


cl = Cleaner("fr")

data = []

for i in collection.get_emails():
    data.append(cl.clean(i.get_subject()))





v = LogicVectorizer(data)




# cl = Cleaner("fr")

# data = cl.clean_list(collection.get_subjects())



print(v.vectorize())

