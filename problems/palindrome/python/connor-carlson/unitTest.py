import unittest
import palindrome as pal

class Testing(unittest.TestCase):
    def test_ignore_puncuation(self):
        palindrome = "A man, a plan, a canal, Panama!"
        palindrome_all_alnum = "A man a plan a canal Panama"
        result1 = pal.checkInput(palindrome_all_alnum)
        result2 = pal.checkInput(palindrome)
        self.assertEqual(result1, result2)

    def test_ignore_spaces(self):
        palindrome = "A man, a plan, a canal, Panama!"
        palindrome_no_spaces = "Aman,aplan,acanal,Panama!"
        result1 = pal.checkInput(palindrome_no_spaces)
        result2 = pal.checkInput(palindrome)
        self.assertEqual(result1, result2)

    def test_ignore_capitalization(self):
        palindrome = "RaCeCaR"
        palindrome_all_lower_case = "racecar"
        result1 = pal.checkInput(palindrome_all_lower_case)
        result2 = pal.checkInput(palindrome)
        self.assertEqual(result1, result2)


if __name__ == '__main__':
    unittest.main()