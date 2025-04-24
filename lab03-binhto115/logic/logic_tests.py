import unittest
import logic


class TestCases(unittest.TestCase):
    def test_case(self):
        # Replace pass with the test code.
        self.assertEqual(logic.is_even(2), True)
        self.assertEqual(logic.is_even(1), False)
        self.assertEqual(logic.is_even(100), True)
        self.assertEqual(logic.is_even(55), False)

    def test_in_an_interval(self):
        self.assertTrue(logic.in_an_interval(2.0), True)
        self.assertFalse(logic.in_an_interval(9), False)
        self.assertTrue(logic.in_an_interval(8.7), True)

        self.assertFalse(logic.in_an_interval(35), False)
        self.assertFalse(logic.in_an_interval(47), False)
        self.assertFalse(logic.in_an_interval(92), False)
        self.assertTrue(logic.in_an_interval(50), True)

        self.assertFalse(logic.in_an_interval(12), False)
        self.assertTrue(logic.in_an_interval(15), True)
        self.assertTrue(logic.in_an_interval(19), True)

        self.assertTrue(logic.in_an_interval(101), True)
        self.assertTrue(logic.in_an_interval(103), True)
        self.assertFalse(logic.in_an_interval(100), False)
        self.assertTrue(logic.in_an_interval(102.666666), True)

# Run the unit tests.
if __name__ == '__main__':
    unittest.main()

