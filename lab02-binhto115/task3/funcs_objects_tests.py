import unittest
import objects
import funcs_objects


class TestCases(unittest.TestCase):
   def test_point(self):
      # Add code here to verify that a point is initialized correctly.
      object_point = objects.Point(5.0, 5.0)
      self.assertEqual(object_point.x, 5.0)
      self.assertEqual(object_point.y, 5.0)
      pass

   def test_circle(self):
      # Add code here to verify that a circle is initialized correctly.
      pt = objects.Point(5, 5)
      object_circle = objects.Circle(pt, 5.0)
      self.assertEqual(object_circle.center, pt)
      self.assertEqual(object_circle.radius, 5)
      pass

   # Add other testing functions for distance and circles_overlap.
   def test_distance(self):
      p1 = objects.Point(1, 2)
      p2 = objects.Point(3, 4)
      self.assertEqual(funcs_objects.distance(p1, p2), 2.8284271247461903)
      p1 = objects.Point(2, 2)
      p2 = objects.Point(2, 2)
      self.assertEqual(funcs_objects.distance(p1, p2), 0)


   def test_circles_overlap(self):
   # #1 test:
      center_1 = objects.Point(1.0, 1.0)
      circle_1 = objects.Circle(center_1, 1.0)
      center_2 = objects.Point(2.0, 2.0)
      circle_2 = objects.Circle(center_2, 2.0)
      self.assertTrue(funcs_objects.circles_overlap(circle_1, circle_2))
   # #2 test:
      center_1 = objects.Point(20.0, 20.0)
      circle_1 = objects.Circle(center_1, 2.0)
      center_2 = objects.Point(10.0, 10.0)
      circle_2 = objects.Circle(center_2, 1.0)
      self.assertFalse(funcs_objects.circles_overlap(circle_1, circle_2))
# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

