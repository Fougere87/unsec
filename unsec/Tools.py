import unsec 

def stop_list(lang):

	
	filename = unsec.STOP_LIST_PATH + lang 
	try:
		with open(filename, 'r') as myfile:
			mylist = myfile.read().split("\n")
		return(mylist)
	except:
		return []