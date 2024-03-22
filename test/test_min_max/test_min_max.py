import unittest
from src.min_max.util import min_max

class MyTest(unittest.TestCase):
        def test1(self):
            self.assertEqual(min_max() , 3)

        """
        4 2
2 5
3 7
1 3
4 0
        """

        def test2(self):
            self.assertEqual(min_max(),  7)

        """
        4 2
2 5
8 7
1 4
4 0
        """

        def test3(self):
            self.assertEqual(min_max() , 2)

        """
        3 2
2 5
1 4
4 0
        """
if __name__ == '__main__':
     unittest.main()