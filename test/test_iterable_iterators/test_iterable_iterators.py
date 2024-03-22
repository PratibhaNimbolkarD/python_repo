import unittest
from src.iterable_and_iterators.util import iterable_iterators

class IterablesIterators(unittest.TestCase):
    def test1(self):
        self.assertEqual(iterable_iterators(),0.8333333333333334)
        '''4
 a a c d
 2'''
    def test2(self):
         self.assertEqual(iterable_iterators(), 0.7222222222222222)
         '''9
 a b c a d b z e o
 4'''

    def test3(self):
        self.assertEqual(iterable_iterators(), 0.3333333333333333)
        '''9
a b c b e b z e o
3'''