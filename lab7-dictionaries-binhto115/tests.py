# Name: Binh To
# Date: 10/25/2022
# Github: 113943258


import unittest
import histogram


class AssignmentTest(unittest.TestCase):

    def test_getHistogram_1(self):
        input_str = "OMG OMG OMG OMG OMG YES YES NO NO"
        dictionary = {"OMG": 5,
                      "YES": 2,
                      "NO": 2}
        self.assertEqual(histogram.getHistogram(input_str), dictionary)

    def test_getHistogram_2(self):
        input_str = "Peter Piper picked a perk of pickled peppers. " \
                    "A peck of pickled peppers Peter Piper picked. " \
                    "If Peter Piper picked a peck of pickled peppers," \
                    " Where's the peck of pickled peppers Peter Piper pickled"
        dictionary = {"Peter": 4,
                      "Piper": 4,
                      "picked": 2,
                      "a": 2,
                      "perk": 1,
                      "of": 4,
                      "pickled": 5,
                      "peppers.": 1,
                      "A": 1,
                      "peck": 3,
                      "peppers": 2,
                      "If": 1,
                      "peppers,": 1,
                      "picked.": 1,
                      "Where's": 1,
                      "the": 1}
        self.assertEqual(histogram.getHistogram(input_str), dictionary)


if __name__ == "__main__":
    unittest.main()