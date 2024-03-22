import unittest

from src.pilling_up.util import pilling_up

class MyTest(unittest.TestCase):
    def test1(self):

        self.assertEqual(pilling_up(), '''Yes
No
''')
        '''
        sample input 
2
6
4 3 2 1 3 4
3
1 3 2
        '''

    def test2(self):

        self.assertEqual(pilling_up(), '''Yes
No
''')
        '''
        sample input 
2
6
4 3 2 1 3 4
3
1 3 2
        '''

    def test3(self):

        self.assertEqual(pilling_up(), '''No
Yes
''')
        '''
        sample input 
2
3
1 3 2
6
4 3 2 1 3 4
        '''

if __name__ == '__main__':
    unittest.main()