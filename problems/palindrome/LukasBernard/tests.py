import unittest as test
import sys
from palindrome import palindrome_check, main

class palindromeTest(test.TestCase):
	def test_PalindromePass(self):
		result = palindrome_check("racecar")
		self.assertTrue(result, "Palindrome is True")

	def test_PalindromeFail(self):
		result = palindrome_check("notpalindrome")
		self.assertFalse(result, "Non Palindrome is False")
	
	def test_OddCase(self):
		result = palindrome_check("12344321")
		self.assertTrue(result, "Number Case is True")

	def test_OddCaseFalse(self):
		result = palindrome_check("12345")
		self.assertFalse(result, "Number Case is False")

if __name__ == '__main__':
    test.main()
