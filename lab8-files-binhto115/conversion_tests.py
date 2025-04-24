# Name: Binh To
# Date: 11/07/2022
# Github: 113943258
import unittest

import conversion


class TestCases(unittest.TestCase):
    def test_stringToFloat(self):
        self.assertEqual(conversion.stringToFloat("6.5"), 6.5)

    def test_stringToFloat_2(self):
        self.assertEqual(conversion.stringToFloat("Hellow World"), None)
if __name__ =='__main__':
    unittest.main()