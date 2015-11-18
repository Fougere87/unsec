import os
import glob
from unsec import Email, EmailCollection




collection = EmailCollection()

collection.add_from_directory("data/bioinfo_2014-01")


print(collection)
