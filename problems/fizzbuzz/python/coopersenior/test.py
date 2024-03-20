import unittest

from fizzbuzz import fizzBuzz


class TestFizzBuzz(unittest.TestCase):
    def test_3(self):
        """
        Test that correct string output is printed for 3
        """
        num = 3
        result = fizzBuzz(num)
        self.assertEqual(result, "1\n2\nFizz")

    def test_5(self):
        """
        Test that correct string output is printed for 5
        """
        num = 5
        result = fizzBuzz(num)
        self.assertEqual(result, "1\n2\nFizz\n4\nBuzz")

    def test_15(self):
        """
        Test that correct string output is printed for 15
        """
        num = 15
        result = fizzBuzz(num)
        self.assertEqual(result, "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz")
        
if __name__ == '__main__':
    unittest.main()