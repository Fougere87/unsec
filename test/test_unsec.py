import unittest
from unsec import Email

class TestParseEmail(unittest.TestCase):


	def test_sender(self):
		e = Email("data/bioinfo_2014-01/9.recoded")
		print(e.sender)
		self.assertNotEqual(e.sender, None)






if __name__ == '__main__':
    unittest.main()