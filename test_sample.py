import unittest
from functions import get_formatted_name

""" Inherit from the testing class"""
class NamesTestCase(unittest.TestCase):

    """Test case for formatted names"""

    """Tests must start with the word test"""
    def test_first_last_name1(self):
        formatted_name = get_formatted_name("John","james")
        self.assertEqual(formatted_name, 'John James')
    def test_first_last_name2(self):
        formatted_name = get_formatted_name("joHn","james")
        self.assertEqual(formatted_name, 'John James')

""" This enables us to run the test at the shell via python3 test_sample.py"""
if __name__ == '__main__':
    unittest.main()