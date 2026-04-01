import unittest
from ReturnTrueIfLessThan20 import checkValue

class TestReturnTrueIfLessThan20(unittest.TestCase):
    def test_less_than_20(self):
        self.assertTrue(checkValue(19))

    def test_equal_to_20(self):
        self.assertFalse(checkValue(20))

    def test_greater_than_20(self):
        self.assertFalse(checkValue(21))

if __name__ == '__main__':
    unittest.main()