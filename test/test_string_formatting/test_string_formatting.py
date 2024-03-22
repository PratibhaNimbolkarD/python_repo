import unittest
from src.string_formatting.util import string_formatting

class MyTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(string_formatting() , '''1 1 1 1
''')
    ''' 1 '''

    def test2(self):
        self.assertEqual(string_formatting(), '''  1   1   1   1
  2   2   2  10
  3   3   3  11
  4   4   4 100
  5   5   5 101
''')
    ''' 5'''

    def test3(self):
            self.assertEqual(string_formatting(), ''' 1  1  1  1
 2  2  2 10
 3  3  3 11
''')
'''3'''

if __name__ == '__main__' :
         unittest.main()
