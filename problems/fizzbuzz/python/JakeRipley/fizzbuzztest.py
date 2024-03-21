import unittest
from fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_fizzbuzz(self):
        # Test FizzBuzz
        self.assertEqual(fizzbuzz(15), [
            '1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz',
            '11', 'Fizz', '13', '14', 'FizzBuzz'
        ])
        
        # Test Fizz
        self.assertEqual(fizzbuzz(6), [
            '1', '2', 'Fizz', '4', 'Buzz', 'Fizz'
        ])
        
        # Test Buzz
        self.assertEqual(fizzbuzz(5), [
            '1', '2', 'Fizz', '4', 'Buzz'
        ])

        # Test Other Numbers
        self.assertEqual(fizzbuzz(2), [
            '1', '2'
        ])
        self.assertEqual(fizzbuzz(7), [
            '1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7'
        ])

if __name__ == '__main__':
    unittest.main()

