import unittest
import point


class TestCases(unittest.TestCase):
    def test_point_one(self):
        pt = point.Point(1, 2)
        self.assertAlmostEqual(pt.x, 1)
        self.assertAlmostEqual(pt.y, 2)

    def test_point_two(self):
        pt = point.Point(-4.7, 19.2)
        self.assertAlmostEqual(pt.x, -4.7)
        self.assertAlmostEqual(pt.y, 19.2)

    def test_equality_one(self):
        # Replace pass with the test code.8
        point1 = point.Point(2.0, 2.0)
        point2 = point.Point(2.0, 2.0)
        self.assertEqual(point1, point2)

    def test_equality_two(self):
        # Replace pass with the test code.
        point3 = point.Point(1.0, 1.0)
        point4 = point.Point(1.0, 1.0)
        self.assertEqual(point3, point4)

# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
