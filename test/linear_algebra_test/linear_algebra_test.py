import unittest

from src.linear_algebra.util import linear_algebra


class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(linear_algebra(), 0.0)

    ''' 2
1.1 1.1
1.1 1.1'''

    def test2(self):
        self.assertEqual(linear_algebra(), 6.0)

    ''' 3
1 2 3
4 5 6
1 2 1'''

    def test3(self):
        self.assertEqual(linear_algebra(), 0.11)

    '''2
1.1 1.1
1.1 1.2'''


if __name__ == '__main__':
    unittest.main()
