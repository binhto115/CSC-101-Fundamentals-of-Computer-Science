# Name: Binh To
# Date: 10/24/2022
# GitHub: 113943258

import unittest
import functions


class StringTest(unittest.TestCase):
    def test_swapCase(self):
        # Test 1:
        self.assertEqual(functions.swapCase("hello!"), "HELLO!")
        # Test 2:
        self.assertEqual(functions.swapCase("hI eVeRy1, mY nAmE iS bInH!"), "Hi EvErY1, My NaMe Is BiNh!")
        # Test 3:
        self.assertEqual(functions.swapCase("Æ is a weird one"), "Æ IS A WEIRD ONE")

    def test_replaceChar(self):
        # Test 1:
        self.assertEqual(functions.replaceChar("Hello Binh!", "h", "g"), "Hello Bing!")
        # Test 2:
        self.assertEqual(functions.replaceChar("Hellow Lyan2", "l", "r"), "Herrow Lyan2")
        # Test 3:
        self.assertEqual(functions.replaceChar("Yellow Peril", "ll", "w"), "Yellow Peril")
        # Test 4:
        self.assertEqual(functions.replaceChar("You are a good boy", "o", "tt"), "You are a good boy")
        # Test 5:
        self.assertEqual(functions.replaceChar("You are a bad boy", "o", "u"), "Yuu are a bad buy")
        # Test 6:
        self.assertEqual(functions.replaceChar("Nooooo", "o", "uu"), "Nooooo")
        # Test 7:
        self.assertEqual(functions.replaceChar("Yessss", "oo", "tt"), "Yessss")


if __name__ == "__main__":
    unittest.main()
