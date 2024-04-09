import unittest

import fizzbuzz as fb

class TestFizzBuzz(unittest.TestCase):
    def test_fizzBuzz(self):
        result = fb.fizzbuzz(15)[0]
        self.assertEqual(result, "FizzBuzz ")

    def test_fizz(self):
        result = fb.fizzbuzz(3)[0]
        self.assertEqual(result, "Fizz ")

    def test_buzz(self):
        result = fb.fizzbuzz(5)[0]
        self.assertEqual(result, "Buzz ")

    def test_int(self):
        result = fb.fizzbuzz(2)[0]
        self.assertEqual(result, "2 ")

if __name__ == '__main__':
    unittest.main()
