# Name: Binh To
# Date: 10/14/2022
# Github: 113943258

import unittest
import functions


class listFunctionTests(unittest.TestCase):
    # Do not modify these tests
    def test_includedOne(self):
        self.assertTrue(functions.areTwoEqual([1, 2, 3, 2], 1, 3))
        self.assertFalse(functions.areTwoEqual([1, 2, 3, 2], 1, 2))

    def test_includedTwo(self):
        self.assertEqual(functions.sumOfThree([1, 2, 3, 2]), 0)
        self.assertEqual(functions.sumOfThree([1, 2]), 0)
        self.assertEqual(functions.sumOfThree([1, 2, 3]), 6)

    def test_includedThree(self):
        self.assertEqual(functions.sumOfUpToThree([1, 2, 3, 2]), 6)
        self.assertEqual(functions.sumOfUpToThree([1, 2]), 3)
        self.assertEqual(functions.sumOfUpToThree([1, 2, 3]), 6)

    def test_includedFour(self):
        self.assertEqual(functions.getFromFirstAsIndex([1, 2, 3, 2]), 2)
        self.assertEqual(functions.getFromFirstAsIndex([2, 2, 3, 2]), 3)
        self.assertEqual(functions.getFromFirstAsIndex([-1, 2, 3, 2]), 2)

    # Write your tests below
    def test_areTwoEqual(self):
        self.assertTrue(functions.areTwoEqual([3, 5, 7, 5], 1, 3))
        self.assertFalse(functions.areTwoEqual([10, 5, 7, 9], 0, 2))

    def test_sumOfThree(self):
        self.assertEqual(functions.sumOfThree([10, 20, 30, 50]), 0)
        self.assertEqual(functions.sumOfThree([15, 15]), 0)

    def test_sumOfUpToThree(self):
        self.assertEqual(functions.sumOfUpToThree([9, 9, 4, 7, 8, 9]), 22)
        self.assertEqual(functions.sumOfUpToThree([7, 8]), 15)

    def test_getFromFirstAsIndex(self):
        self.assertEqual(functions.getFromFirstAsIndex([5, 1, 2, 3, 7, 8]), 8)
        self.assertEqual(functions.getFromFirstAsIndex([4, 1, 2, 6, 8]), 8)

if __name__ == "__main__":
    unittest.main()

