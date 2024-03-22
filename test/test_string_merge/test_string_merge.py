import unittest
from src.string_merge.util import merge_the_tools


class  MyTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(merge_the_tools() , """AB
CA
AD
""")

    '''AABCAAADA
       3 '''

    def test2(self):
            self.assertEqual(merge_the_tools(), """AB
CD
""")

    '''ABCD
      2'''
    def test3(self):
        self.assertEqual(merge_the_tools(), """ABC
ABC
ABC
ABC
""")

    '''ABCABCABCABC
       3'''

    if __name__ == '__main__':
        unittest.main()