import unittest
import palindrome as pal

class Testing(unittest.TestCase):
    def test_ignore_puncuation(self):
        palindrome = "A man, a plan, a canal, Panama!"
        palindrome_all_alnum = "A man a plan a canal Panama"
        result1 = pal.isPalindrome(palindrome, 0, len(palindrome)-1)
        result2 = pal.isPalindrome(palindrome_all_alnum, 0, len(palindrome_all_alnum)-1)
        self.assertEqual(result1, result2)

    def test_ignore_spaces(self):
        palindrome = "A man, a plan, a canal, Panama!"
        palindrome_no_spaces = "Aman,aplan,acanal,Panama!"
        result1 = pal.isPalindrome(palindrome, 0, len(palindrome)-1)
        result2 = pal.isPalindrome(palindrome_no_spaces, 0, len(palindrome_no_spaces)-1)
        self.assertEqual(result1, result2)

    def test_ignore_capitalization(self):
        palindrome = "RaCeCaR"
        palindrome_all_lower_case = "racecar"
        result1 = pal.isPalindrome(palindrome, 0, len(palindrome)-1)
        result2 = pal.isPalindrome(palindrome_all_lower_case, 0, len(palindrome_all_lower_case)-1)
        self.assertEqual(result1, result2)


if __name__ == '__main__':
    unittest.main()