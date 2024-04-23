import unittest

from fizzbuzz import getValue


class TestFizzBuzz(unittest.TestCase):
    def test_3(self):
        """
        Test that correct string output is printed for 3
        """
        num = 3
        result = getValue(num)
        self.assertEqual(result, "Fizz")

    def test_5(self):
        """
        Test that correct string output is printed for 5
        """
        num = 5
        result = getValue(num)
        self.assertEqual(result, "Buzz")

    def test_15(self):
        """
        Test that correct string output is printed for 15
        """
        num = 15
        result = getValue(num)
        self.assertEqual(result, "FizzBuzz")
        
if __name__ == '__main__':
    unittest.main()