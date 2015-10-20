import os
from unsec import Email
from unsec.stop_list import *

# for file in os.walk("data/bioinfo_2014-01/*.recoded"):
#     print(file)

# for i in range()
#
e = Email("data/bioinfo_2014-01/2.recoded")
fr1 = create_list("stop_list/french1")
fr2 = create_list("stop_list/french2")
en1 = create_list("stop_list/english1")
en2 = create_list("stop_list/english2")
en3 = create_list("stop_list/english3")
fr = merge_lists(fr1, fr2)
en = merge_lists(en1, en2, en3)
# print(e.tokenBody())
print(Email.remove_stopwords(e.tokenBody(), fr = fr ,en = en))

# print(e.tokenSubject())



# print(e.lemmatizeBody())
