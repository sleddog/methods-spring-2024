import unittest
from palindromeCheck import is_palindrome

class TestPalindromeCheck(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("A man, a plan, a canal, Panama!"))
        self.assertFalse(is_palindrome("hello"))

if __name__ == "__main__":
    unittest.main()