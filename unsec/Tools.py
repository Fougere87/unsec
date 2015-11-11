import unsec
from unsec import Email
from unsec import Collection

# def stop_list(lang):
#
#
# 	filename = unsec.STOP_LIST_PATH + lang
# 	try:
# 		with open(filename, 'r') as myfile:
# 			mylist = myfile.read().split("\n")
# 		return(mylist)
# 	except:
# 		return []


class StopLists(object):
	def __init__(self, email):
		self.stop_lists = list()
		for stop_list in self.get_stop_list(directory):
			self.stop_lists.append(StopList.stop_list)
		self.language = StopLists.language(self, email)

	def get_stop_list(directory):
		for stop_list in glob.glob(directory+"/*"):
			yield stop_list

	def language(args):
		lang = list()
		# args = get_stop_list(directory)
		for email in Collection.Collection.get_email("data/"):
			for i in range(len(args)-1):
				if Email.language_detection(email) == Email.language_detection(i):
					lang = set(args[i] + args[i+1])
		print(len(lang))
		return(lang)
