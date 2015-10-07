import os
from unsec import Email


# for file in os.walk("data/bioinfo_2014-01/*.recoded"):
#     print(file)

# for i in range()
#
e = Email("data/bioinfo_2014-01/9.recoded")


print(e.tokenSubject())

print(e.tokenBody())

print(e.lemmatizeBody())
