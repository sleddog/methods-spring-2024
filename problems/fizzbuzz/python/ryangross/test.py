import unittest

import fizzbuzz as fb

class TestFizzBuzz(unittest.TestCase):
    def test_fizzBuzz(self):
        result = fb.fizzbuzz(15)[1]
        self.assertEqual(result[1], "FizzBuzz ")

    def test_fizz(self):
        result = fb.fizzbuzz(3)[1]
        self.assertEqual(result, "Fizz ")

    def test_buzz(self):
        result = fb.fizzbuzz(5)[1]
        self.assertEqual(result, "Buzz ")

    def test_int(self):
        result = fb.fizzbuzz(2)[1]
        self.assertEqual(result, "2 ")

if __name__ == '__main__':
    unittest.main()
