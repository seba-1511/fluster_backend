import unittest
import parse

expected = 'Parse me, you naughty boy.'


class TestParser(unittest.TestCase):

    def test_parse_docx(self):
        returned = parse.parse('test.docx')
        self.assertEqual(expected, returned)

    def test_parse_pdf(self):
        returned = parse.parse('test.pdf')
        self.assertEqual(expected, returned)

    def test_parse_txt(self):
        returned = parse.parse('test.txt')
        self.assertEqual(expected, returned)

    def test_parse_py(self):
        returned = parse.parse('test.py')
        self.assertEqual(expected, returned)

if __name__ == '__main__':
    unittest.main()
