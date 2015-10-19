import os
from unsec import Email
from unsec.Stop_list import *

# for file in os.walk("data/bioinfo_2014-01/*.recoded"):
#     print(file)

# for i in range()
#
e = Email("data/bioinfo_2014-01/2.recoded")
fr1 = create_list("stop_list/french1")
fr2 = create_list("stop_list/french2")
# print("type fr1 ", type(fr1))
# print("fr2 ", fr2)
print(len(fr1))
print (len(fr2))

print(len(merge_lists(fr1,fr2))) # a tester
print(e.lang)
# print(e.tokenSubject())

# print(e.tokenBody())

# print(e.lemmatizeBody())
