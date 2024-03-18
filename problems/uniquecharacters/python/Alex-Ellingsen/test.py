import unittest
import uniqueStrings

class testUnique(unittest.TestCase):
    
    def testUniqueChars(self):
        self.assertEqual(uniqueStrings.uniqueString("abcde"), True, "Should be True")

    def testUniqueNums(self):
        self.assertEqual(uniqueStrings.uniqueString("123456"), True, "Should be True")

    def testNonUnique(self):
        self.assertEqual(uniqueStrings.uniqueString("abcdefa"), False, "Should be False")

if  __name__ == "__main__":
    unittest.main()