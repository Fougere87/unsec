import os
import glob
from unsec import Email, EmailCollection, Cleaner




collection = EmailCollection()

collection.add_from_directory("data/bioinfo_2014-01")


cleaner = Cleaner("en")

for i in cleaner.clean_collection(collection.get_subjects()):
    print(i)
