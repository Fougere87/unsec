import os
from unsec import Email
from unsec import Tools
from unsec import Collection


e = Email("data/bioinfo_2014-01/2.recoded")



print(e.clean_body())