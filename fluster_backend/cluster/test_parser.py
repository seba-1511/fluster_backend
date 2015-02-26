import unittest
import parse

expected = 'Parse me, you naughty boy.'

class TestParser(unittest.TestCase):
	
	def test_parse_docx():
		returned = parse.parse('test.docx')
		assertEqual(expected, returned)

	def test_parse_pdf():
		returned = parse.parse('test.pdf')
		assertEqual(expected, returned)

	def test_parse_txt():
		returned = parse.parse('test.txt')
		assertEqual(expected, returned)

	
