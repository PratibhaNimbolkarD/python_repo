import unittest
from src.validating_email_address.util import validating_email

class MyTest(unittest.TestCase):
    def test1(self):

        self.assertEqual(validating_email(), ['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com'])
        '''
    sample input    
3
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com
        '''

    def test2(self):

        self.assertEqual(validating_email(), ['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com'])
        '''
        sample input 
3
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com
        '''

    def test3(self):

        self.assertEqual(validating_email(),['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com'])
        '''
        sample input 
3
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com
        '''

if __name__ == '__main__':
    unittest.main()