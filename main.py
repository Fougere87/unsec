import os
import glob 
from unsec import Email
from unsec import Tools
from unsec import Collection




for file in glob.glob("data/bioinfo_2014-01/*") : 
	print(file)
	e = Email(file)

	print(e.message.get_charsets())
	print(e.body())


	input()



#print(e.clean_body())