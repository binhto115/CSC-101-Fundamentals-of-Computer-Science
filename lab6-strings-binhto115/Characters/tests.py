# Name: Binh To
# Date: 10/24/2022
# GitHub: 113943258

import unittest
import functions


class CharacterTest(unittest.TestCase):
    def test_isEnglishUpper(self):
        # Test 1:
        self.assertTrue(functions.isEnglishUpper("Hello"), True)
        # Test 2:
        self.assertTrue(functions.isEnglishUpper("World"), True)
        # Test 3:
        self.assertTrue(functions.isEnglishUpper("Zephyrus"), True)
        # Test 4:
        self.assertFalse(functions.isEnglishUpper("yes"), False)

if __name__ == "__main__":
    unittest.main()
