import unittest
from palindrome import isPalindrome

class TestPalindromeChecker(unittest.TestCase):

    def test_is_palindrome(self):
        self.assertEqual(isPalindrome("racecar"), "This is a Palindrome")
        self.assertEqual(isPalindrome("level"), "This is a Palindrome")
        self.assertEqual(isPalindrome("radar"), "This is a Palindrome")

    def test_is_not_palindrome(self):
        self.assertEqual(isPalindrome("hello"), "NOT a Palindrome")
        self.assertEqual(isPalindrome("python"), "NOT a Palindrome")
        self.assertEqual(isPalindrome("I am not a palindrome"), "NOT a Palindrome")

    def test_invalid_argument(self):
        self.assertEqual(isPalindrome(123), "ERROR: Argument is not a String")
        self.assertEqual(isPalindrome(3.00), "ERROR: Argument is not a String")

if __name__ == '__main__':
    unittest.main()
