import unittest
from  src.find_percentage.util import find_percentage

class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(find_percentage(),26.50)

    """
    2
Harsh 25 26.5 28
Anurag 26 28 30
Harsh
    """
    def test2(self):
        self.assertEqual(find_percentage(),56.00)
        """
        3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
"""
    def test3(self):
        self.assertEqual(find_percentage(),90.00)


"""
2
Pratibha 75 80 85
Kuldeep 90 85 95
Kuldeep
"""

if __name__ == '__main__':
    unittest.main()

