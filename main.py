import os
from unsec import Email
from unsec import Stop_list

# for file in os.walk("data/bioinfo_2014-01/*.recoded"):
#     print(file)

# for i in range()
#
e = Email("data/bioinfo_2014-01/9.recoded")
fr1 = Stop_list("stop_list/french1")
fr2 = Stop_list("stop_list/french2")


print(e.tokenSubject())

print(e.tokenBody())
