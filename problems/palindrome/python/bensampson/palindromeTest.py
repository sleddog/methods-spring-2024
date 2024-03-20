import unittest
import palindrome

class TestPalindrome(unittest.TestCase):
    
    def test_correct_palindrome(self):
        self.assertTrue(palindrome("kayak"), "True")
        self.assertTrue(palindrome("racecar"), "True")
        self.assertTrue(palindrome(""), "True")
        
    def test_incorrect_palindrome(self):
        self.assertFalse(palindrome("track"), "False")
        self.assertFalse(palindrome("cat"), "False")
        self.assertFalse(palindrome("This is for sure NOT a palindrome"), "False")
        
if __name__ == '__main__':
    unittest.main()