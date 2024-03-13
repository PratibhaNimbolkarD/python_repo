import unittest
from src.find_runnerup_score.util import runner_up

class MyTest(unittest.TestCase):
        def test1(self):
            self.assertEqual(runner_up() , 5)

        """
        5
        2 3 6 6 5
        """

        def test2(self):
            self.assertEqual(runner_up(),  4)

        """
        4
        1 2 5 4
        """

        def test3(self):
            self.assertEqual(runner_up() , 2)

        """
        6
        1 1 2 2 3 3
        """
if __name__ == '__main__':
     unittest.main()