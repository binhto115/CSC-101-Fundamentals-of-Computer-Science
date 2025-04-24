import unittest

# How can we access the definition of Line?
# Import the line module here.
import line
class LineTests(unittest.TestCase):
    def test_line(self):
        # The following line should show a warning on the value "shoe".
        result = line.Line("shoe", 2, 3, 4)
        self.assertEqual(result.x1, 1)
        self.assertEqual(result.y1, 2)
        self.assertEqual(result.x2, 3)
        self.assertEqual(result.y2, 4)

    def test_line_again(self):
        # Add code here.
        # 1) Create a Line with x1, y1, x2, y2 values of your choice.
        # 2) Use assertEqual on each field in the new Line to verify
        #    that it holds the expected value.
        result_2 = line.Line(5, 6, 7, 8)
        self.assertEqual(result_2.x1, 5)
        self.assertEqual(result_2.y1, 6)
        self.assertEqual(result_2.x2, 7)
        self.assertEqual(result_2.y2, 8)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()
