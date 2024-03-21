import unittest
import uniquecharacters as uc

class TestUniqueChars(unittest.TestCase):
    def test_UniqueChars(self):
        self.assertTrue(uc.uniqueChars("abc"))

    def test_UniqueSymbols(self):
        self.assertTrue(uc.uniqueChars("123"))
        self.assertTrue(uc.uniqueChars("!@#"))

    def test_NotUnique(self):
        self.assertFalse(uc.uniqueChars("abb"))
        self.assertFalse(uc.uniqueChars("122"))
        self.assertFalse(uc.uniqueChars("*!*"))
    
    def test_Spaces(self):
        self.assertTrue(uc.uniqueChars("ab cd"))
        self.assertFalse(uc.uniqueChars("ab bc"))

if __name__ == '__main__':
    unittest.main()