# Name: Binh To
# Date: 10/19/2022
# Github: 113943258

import unittest
import objects
import functions


class FoldTest(unittest.TestCase):
    def test_getMinium(self):
        # First Test:
        list_of_number = [1, 17, 90, 6, 8, 100, 40]
        self.assertEqual(functions.getMinimum(list_of_number), 1)
        # Second Test:
        list_of_number_2 = [90, 27, 100, 50, 3, 5, -2]
        self.assertEqual(functions.getMinimum(list_of_number_2), -2)

    def test_areAllTrue(self):
        # First Test:
        list_of_number = [True, True, True, True]
        self.assertTrue(functions.areAllTrue(list_of_number), True)
        # Second Test:
        list_of_number_2 = [True, False, False, False]
        self.assertFalse(functions.areAllTrue(list_of_number_2), True)

    def test_getCenterPoint(self):
        # Test 1:
        point_1 = objects.Point(3, 5)
        point_2 = objects.Point(5, 7)
        point_3 = objects.Point(8, 9)
        points_list = [point_1, point_2, point_3]
        self.assertEqual(functions.getCenterPoint(points_list), objects.Point(5.333333333333333, 7.0))
        # Test 2:
        point_4 = objects.Point(10, 20)
        point_5 = objects.Point(15, 20)
        point_6 = objects.Point(2, 5)
        point_list_2 = [point_4, point_5, point_6]
        self.assertEqual(functions.getCenterPoint(point_list_2), objects.Point(9.0, 15.0))

    def test_countLessThanFour(self):
        # Test 1:
        test_list_of_str = ["Helloe", "Hi", "Monkey", "Yup", "She"]
        self.assertEqual(functions.countLessThanFour(test_list_of_str), 3)
        # Test 2:
        test_list_of_str_2 = ["He", "Him", "They", "Ben", "No", "yes"]
        self.assertEqual(functions.countLessThanFour(test_list_of_str_2), 5)


if __name__ == "__main__":
    unittest.main()
