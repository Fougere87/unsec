import os
import glob
from unsec import Email, EmailCollection




collection = EmailCollection()

for f in glob.glob("data/bioinfo_2014-01/*"):
    collection.add_file(f)


print(collection.at(4).get_subject())
