import unittest
import mini_app
from mini_app import upperString    # needed for test of value
from mini_app import startstring

class TestUpperfunction(unittest.TestCase):

    # Test of value 'upperString'
    def test_upperString_value(self):
        self.assertTrue(upperString.isupper())

    def test_Uppercase(self):
        self.assertEqual(upperString, startstring.upper())
        self.assertEqual(startstring, startstring.upper())    # Fehlerfall

if __name__ == "__main__":
    unittest.main()