import unittest
import conditional

class TestCases(unittest.TestCase):
    def test_case(self):
        # Replace pass with the test code.
        self.assertEqual(conditional.max_101(60.0, 60.1), 60.1)
        self.assertEqual(conditional.max_101(5.0, 4.9), 5.0)
    def test_max_of_three(self):
        self.assertEqual(conditional.max_of_three(1.2, 2.3, 2), 2.3)
        self.assertEqual(conditional.max_of_three(5.2, 2.3, 5.19), 5.2)
        self.assertEqual(conditional.max_of_three(2.89, 2.3, 2.9), 2.9)
        self.assertEqual(conditional.max_of_three(1.0, 1.0, 1.0), 1.0)

    def test_rental_late_fee(self):
        self.assertEqual(conditional.rental_late_fee(25), 100)
        self.assertEqual(conditional.rental_late_fee(24), 19)
        self.assertEqual(conditional.rental_late_fee(15), 7)
        self.assertEqual(conditional.rental_late_fee(9), 5)
        self.assertEqual(conditional.rental_late_fee(0), 0)

    # Run the unit tests.
if __name__ == '__main__':
    unittest.main()

