import unittest
from unsec import Email
import glob

class TestParseEmail(unittest.TestCase):


	def test_parser(self):
		for file in glob.glob("data/bioinfo_2014-01/*.recoded"):
			e = Email(file)
			print(file+"\n"+str(e.sender))

			self.assertNotEqual(e.subject, None, msg="subject is empty")
			#self.assertNotEqual(e.sender, None, msg="email is empty")
			#self.assertNotEqual(e.sender, None, msg="email is empty")








if __name__ == '__main__':
    unittest.main()