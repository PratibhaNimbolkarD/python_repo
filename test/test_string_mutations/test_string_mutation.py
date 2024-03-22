import unittest
from src.string_mutations.util import mutate_string

class MyTest(unittest.TestCase):
      def test1(self):
        self.assertEqual(mutate_string() , "abrackdabra")

      """abracadabra ,
        5 k"""

      def test2(self):
         self.assertEqual(mutate_string() , "heblo")
      """ hello
      2 b
      """

      def test3(self):
          self.assertEqual(mutate_string() , "horld")

      """world
      0 h"""
if __name__ == '__main__' :
    unittest.main()