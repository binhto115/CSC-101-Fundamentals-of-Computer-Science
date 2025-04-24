import hw1
import unittest
import math


class TestCases(unittest.TestCase):
    # this function gets the prices from def __init__ and prints
    # out the prices using __string__
    def test_Price_1(self):
        price = hw1.Price(1, 20)
        self.assertEqual(price.dollars, 1)
        self.assertEqual(price.cents, 20)

    def test_Price_2(self):
        price = hw1.Price(4, 19)
        self.assertEqual(price.dollars, 4)
        self.assertEqual(price.cents, 19)

    # This func compares the prices from __init__ using the function __eq__
    def test_Price_eq_1(self):
        price1 = hw1.Price(1, 20)
        price2 = hw1.Price(1, 20)
        self.assertEqual(price1, price2)

    def test_Price_eq_2(self):
        price1 = hw1.Price(1, 20)
        self.assertEqual(price1, price1)

    def test_Price_eq_3(self):
        price1 = hw1.Price(1, 20)
        price2 = hw1.Price(2, 20)
        self.assertNotEqual(price1, price2)

    def test_Price_eq_4(self):
        price1 = hw1.Price(1, 20)
        price2 = 1.20
        self.assertNotEqual(price1, price2)

    # Part 1:
    # This function gets the Prices from class Price and prints out a new price
    def test_add_prices(self):
        price1 = hw1.Price(1, 50)
        price2 = hw1.Price(1, 800)
        self.assertEqual(hw1.add_prices(price1, price2), hw1.Price(10, 50))

        price3 = hw1.Price(3, 30)
        price4 = hw1.Price(3, 70)
        self.assertEqual(hw1.add_prices(price3, price4), hw1.Price(7, 00))

    # Part 2 & Part 3:
    # This function compares prices of x and y
    def test_point(self):
        pt_1 = hw1.Point(2.0, 2.0)
        self.assertEqual(pt_1.x, 2.0)
        self.assertEqual(pt_1.y, 2.0)
        pt_2 = hw1.Point(3.0, 4.0)
        self.assertEqual(pt_2.x, 3.0)
        self.assertEqual(pt_2.y, 4.0)

    # This function gets points from class Point to compare points to points
    def test_point_eq(self):
        point1 = hw1.Point(1.0, 1.0)
        point2 = hw1.Point(1.0, 1.0)
        self.assertEqual(point1, point2)
        point3 = hw1.Point(1.0, 1.0)
        point4 = hw1.Point(2.0, 1.0)
        self.assertNotEqual(point3, point4)

    # This function checks points from class Rectangle
    def test_rectangle(self):
        rectangle_top_left_pt1 = hw1.Point(1.0, 2.0)
        rectangle_bottom_right_pt2 = hw1.Point(3.0, 4.0)
        rec_pt1_pt2 = hw1.Rectangle(rectangle_top_left_pt1, rectangle_bottom_right_pt2)
        rec_result1 = hw1.Point(1.0, 2.0)
        rec_result2 = hw1.Point(3.0, 4.0)
        rec_result_1_2 = hw1.Rectangle(rec_result1, rec_result2)
        self.assertEqual(rec_pt1_pt2, rec_result_1_2)

        rectangle_top_left_pt1 = hw1.Point(1.0, 2.0)
        rectangle_bottom_right_pt2 = hw1.Point(3.0, 4.0)
        rec_pt1_pt2 = hw1.Rectangle(rectangle_top_left_pt1, rectangle_bottom_right_pt2)
        rec_result1 = hw1.Point(2.0, 5.0)
        rec_result2 = hw1.Point(6.0, 2.0)
        rec_result_1_2 = hw1.Rectangle(rec_result1, rec_result2)
        self.assertNotEqual(rec_pt1_pt2, rec_result_1_2)

    # This function compares points from class Rectangle
    def test_rectangle_eq(self):
        top_left_pt = hw1.Point(1.0, 1.0)
        bottom_right_pt = hw1.Point(2.0, 2.0)
        top_bottom_pt = hw1.Rectangle(top_left_pt, bottom_right_pt)
        top_left_pt2 = hw1.Point(1.0, 1.0)
        bottom_right_pt2 = hw1.Point(2.0, 2.0)
        top_bottom_pt2 = hw1.Rectangle(top_left_pt2, bottom_right_pt2)
        self.assertEqual(top_bottom_pt, top_bottom_pt2)

        top_left_pt3 = hw1.Point(1.0, 2.0)
        bottom_right_pt3 = hw1.Point(3.0, 3.0)
        top_bottom_pt3 = hw1.Rectangle(top_left_pt3, bottom_right_pt3)
        top_left_pt4 = hw1.Point(3.0, 3.0)
        bottom_right_4 = hw1.Point(1.0, 2.0)
        top_bottom_pt4 = hw1.Rectangle(top_left_pt4, bottom_right_4)
        self.assertNotEqual(top_bottom_pt3, top_bottom_pt4)

    # This function checks the circle's points
    def test_circle(self):
        point = hw1.Point(5, 5)
        point_circle = hw1.Circle(point, 5.0)
        self.assertEqual(point_circle.center, point)
        self.assertEqual(point_circle.radius, 5)

        point = hw1.Point(10, 10)
        point_circle = hw1.Circle(point, 7.0)
        self.assertEqual(point_circle.center, point)
        self.assertEqual(point_circle.radius, 7.0)

    # This function compares two circles
    def test_circle_eq(self):
        circle_point1 = hw1.Point(1.0, 1.0)
        circle1 = (circle_point1, 5.0)
        circle_point2 = hw1.Point(1.0, 1.0)
        circle2 = (circle_point2, 5.0)
        self.assertEqual(circle1, circle2)

        circle_point3 = hw1.Point(2.0, 2.0)
        circle3 = hw1.Circle(circle_point3, 10.0)
        circle_point4 = hw1.Point(4.0, 4.0)
        circle4 = hw1.Circle(circle_point4, 20.0)
        self.assertNotEqual(circle3, circle4)

    # Part 4:
    # This function checks if the function rectangle_perimeter returns the perimeter
    def test_rectangle_perimeter(self):
        top_left_point = hw1.Point(2.0, 3.0)
        bottom_right_point = hw1.Point(4.0, 6.0)
        rectangle_point = hw1.Rectangle(top_left_point, bottom_right_point)
        self.assertEqual(hw1.rectangle_perimeter(rectangle_point), 10)

    # Part 5:
    # This function checks if the function rectangle_lower_half returns the bottom half of a rectangle
    def test_rectangle_lower_half(self):
        old_top_left_points = hw1.Point(1.0, 5.0)
        old_bottom_right_points = hw1.Point(6.0, 1.0)
        new_lower_half_rectangle = hw1.Rectangle(old_top_left_points, old_bottom_right_points)
        new_top_left_pts = (1.0, 3.0)
        new_bottom_left_pts = (6.0, 1.0)
        new_pts = (new_top_left_pts, new_bottom_left_pts)
        self.assertEqual(hw1.rectangle_lower_half(new_lower_half_rectangle), new_pts)

        old_top_left_points2 = hw1.Point(2.0, 10.0)
        old_bottom_right_points2 = hw1.Point(5.0, 2.0)
        new_lower_half_rectangle2 = hw1.Rectangle(old_top_left_points2, old_bottom_right_points2)
        new_top_left_pts2 = (2.0, 6.0)
        new_bottom_left_pts2 = (5.0, 2.0)
        new_pts2 = (new_top_left_pts2, new_bottom_left_pts2)
        self.assertEqual(hw1.rectangle_lower_half(new_lower_half_rectangle2), new_pts2)

    # Part 6:
    # This function checks if a rectangle is a square with points
    def test_is_square(self):
        top_left_pt = hw1.Point(2.0, 4.0)
        bottom_right_pt = hw1.Point(4.0, 2.0)
        is_square_pt = hw1.Rectangle(top_left_pt, bottom_right_pt)
        self.assertTrue(hw1.is_square(is_square_pt), True)

        top_left_pt2 = hw1.Point(1.0, 3.0)
        bottom_right_pt = hw1.Point(3.0, 2.0)
        is_square_pt = hw1.Rectangle(top_left_pt2, bottom_right_pt)
        self.assertFalse(hw1.is_square(is_square_pt), False)

    # Part 7:
    # Using the points, this function checks if the circle is completely inside the rectangle
    def test_circle_within_rectangle(self):
        # Tests to check if the function returns True
        # when the circle is completely inside the rectangle
        top_left_point_1 = hw1.Point(1.0, 5.0)
        bottom_right_point_1 = hw1.Point(6.0, 1.0)
        rectangle_point = hw1.Rectangle(top_left_point_1, bottom_right_point_1)
        circle_center_1 = hw1.Point(3.0, 3.0)
        circle = hw1.Circle(circle_center_1, 1.0)
        self.assertTrue(hw1.circle_within_rectangle(circle, rectangle_point), True)
        # Tests to check if the function returns False when the center of the circle
        #  is close to a side of the rectangle
        top_left_point_2 = hw1.Point(2.0, 6.0)
        bottom_right_point_2 = hw1.Point(6.0, 2.0)
        rectangle_point_2 = hw1.Rectangle(top_left_point_2, bottom_right_point_2)
        circle_center_2 = hw1.Point(1.0, 3.0)
        circle_2 = hw1.Circle(circle_center_2, 2.0)
        self.assertFalse(hw1.circle_within_rectangle(circle_2, rectangle_point_2), False)
        # Tests to check if the function returns False when the circle collides with the rectangle
        top_left_point_3 = hw1.Point(1.0, 5.0)
        bottom_right_point_3 = hw1.Point(6.0, 1.0)
        rectangle_point_3 = hw1.Rectangle(top_left_point_3, bottom_right_point_3)
        circle_center_3 = hw1.Point(5.0, 4.0)
        circle_3 = hw1.Circle(circle_center_3, 4.0)
        self.assertFalse(hw1.circle_within_rectangle(circle_3, rectangle_point_3), False)

    # Part 8:
    # This function uses points to yield the circle's centered points
    # and its radius that is equal to the distance from the center to one of the corner points.
    def test_circle_bound(self):
        length = hw1.Point(1.0, 6.0)
        width = hw1.Point(5.0, 2.0)
        rectangle_pt = hw1.Rectangle(length, width)
        circle_pt = hw1.Point(3.0, 4.0)
        circle_final_test = hw1.Circle(circle_pt, math.sqrt(8))
        self.assertEqual(hw1.circle_bound(rectangle_pt), circle_final_test)

        length_2 = hw1.Point(3.0, 6.0)
        width_2 = hw1.Point(6.0, 2.0)
        rectangle_pt_2 = hw1.Rectangle(length_2, width_2)
        circle_pt_2 = hw1.Point(4.5, 4.0)
        circle_final_test_2 = hw1.Circle(circle_pt_2, 2.5)
        self.assertEqual(hw1.circle_bound(rectangle_pt_2), circle_final_test_2)


if __name__ == '__main__':
    unittest.main()
