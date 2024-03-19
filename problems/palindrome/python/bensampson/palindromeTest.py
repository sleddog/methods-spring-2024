import unittest
from palindrome import isPalindrome

class TestPalindrome(unittest.TestCase):
    
    def test_correct_palindrome(self):
        self.assertTrue(isPalindrome("kayak"), "True")
        self.assertTrue(isPalindrome("racecar"), "True")
        self.assertTrue(isPalindrome(""), "True")
        
    def test_incorrect_palindrome(self):
        self.assertFalse(isPalindrome("track"), "False")
        self.assertFalse(isPalindrome("cat"), "False")
        self.assertFalse(isPalindrome("This is for sure NOT a palindrome"), "False")
        
if __name__ == '__main__':
    unittest.main()