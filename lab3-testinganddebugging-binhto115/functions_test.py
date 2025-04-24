# Name: Binh To
# Date: 10/10/2022
# Github: binhto115

import unittest
# Import the functions.py file here

class LabTest(unittest.TestCase):
    # The following test is an example of using the unittest framework for the
    #   addValues function.
    def testAddValues(self):
        self.assertEqual(addValues(2, 3), 5)
        self.assertEqual(addValues(6, 3), 9)
        self.assertEqual(addValues(-19, 34), 15)

    # Write your tests following this comment. An empty test is given as
    #   an example. This function's name should be appropriately changed and
    #   the included "pass" statement is place-holder code that may be removed
    #   once your test is implemented.
    def testEmpty(self):
        pass

if __name__ == "__main__":
    unittest.main()
