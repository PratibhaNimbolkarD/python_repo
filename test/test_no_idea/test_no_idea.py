import unittest
from src.no_idea.util import no_idea

class MyTest(unittest.TestCase):
        def test1(self):
            self.assertEqual(no_idea() , 1)

        """
        3 2
1 5 3
3 1
5 

        """

        def test2(self):
            self.assertEqual(no_idea(),  1)

        """
        5 5
1 2 3 4 5
1 3 5 7 9
2 4 6 8 10
        """

        def test3(self):
            self.assertEqual(no_idea() , 1)

        """
        3 2
1 5 3
3 1
5 7
        """
if __name__ == '__main__':
     unittest.main()