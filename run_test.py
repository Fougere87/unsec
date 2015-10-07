import unittest 
from test.test_unsec import TestParseEmail

suite = unittest.TestLoader().loadTestsFromTestCase(TestParseEmail)
unittest.TextTestRunner(verbosity=2).run(suite)