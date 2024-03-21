import unittest
from sum import isPrime

class TestIsPrime(unittest.TestCase):

    def test_prime_number(self):
        self.assertTrue(isPrime(2))
        self.assertTrue(isPrime(3))
        self.assertTrue(isPrime(5))
        self.assertTrue(isPrime(7))
        self.assertTrue(isPrime(11))
        self.assertTrue(isPrime(13))
        self.assertTrue(isPrime(17))
        self.assertTrue(isPrime(19))

    def test_non_prime_number(self):
        self.assertFalse(isPrime(1))
        self.assertFalse(isPrime(4))
        self.assertFalse(isPrime(6))
        self.assertFalse(isPrime(8))
        self.assertFalse(isPrime(9))
        self.assertFalse(isPrime(10))
        self.assertFalse(isPrime(12))
        self.assertFalse(isPrime(15))
        self.assertFalse(isPrime(20))

    def test_negative_number(self):
        self.assertFalse(isPrime(-1))
        self.assertFalse(isPrime(-2))
        self.assertFalse(isPrime(-3))
        self.assertFalse(isPrime(-4))
        self.assertFalse(isPrime(-5))

if __name__ == '__main__':
    unittest.main()


