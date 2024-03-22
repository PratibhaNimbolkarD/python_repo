import unittest
from src.floor_ceil_rint.util import floor_ceil_rint

class MyTest(unittest.TestCase):
    def test1(self):
        self.assertEquals(floor_ceil_rint(),    '''[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
[  2.   3.   4.   5.   6.   7.   8.   9.  10.]
[  1.   2.   3.   4.   6.   7.   8.   9.  10.]''')
    '''1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9'''


    def test2(self):
        self.assertEquals(floor_ceil_rint(), '''[ 2.  3.  4.  5.  6.  7.  8.]
[ 3.  4.  5.  6.  7.  8.  9.]
[ 2.  3.  4.  6.  7.  8.  9.]''')

    '''2.2 3.3 4.4 5.5 6.6 7.7 8.8
'''

    def test3(self):
        self.assertEquals(floor_ceil_rint(), '''[ 1.  2.  3.  4.  5.  6.  7.  8.]
[ 2.  3.  4.  5.  6.  7.  8.  9.]
[ 1.  2.  3.  4.  6.  7.  8.  9.]''')
    '''1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8'''