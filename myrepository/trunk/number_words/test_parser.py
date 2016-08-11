import unittest
from parser import Parser 

class test_number_parser(unittest.TestCase):

	def test_one_to_ten(self):
		parser=Parser()
		result = parser.parse(1)
		self.assertEqual("one", result)
	def test_return_two(self):
		parser=Parser()
		result = parser.parse(2)
		self.assertEqual("two", result)
	def test_return_more_than_ten(self):
		parser=Parser()
		result = parser.parse(13)
		self.assertEqual("thirteen", result)
	def test_return_more_than_twenty(self):
		parser=Parser()
		result = parser.parse(53)
		self.assertEqual("fiftythree",result) 

if __name__ == "__main__":
	unittest.main()
