# Name: Binh To
# Date: 10/25/2022
# Github: 113943258

import unittest

import hw3


class AssignmentTests(unittest.TestCase):

    def test_init_1(self):
        test_book = hw3.Book("Heads You Lose", ["Lisa Lutz", "David Hayward"], 2011)
        self.assertEqual(test_book.title, "Heads You Lose")
        self.assertEqual(test_book.authors, ["Lisa Lutz", "David Hayward"])
        self.assertEqual(test_book.year, 2011)

    def test_init_2(self):
        test_book_2 = hw3.Book("Good Omens", ["Neil Gaiman", "Terry Pratchett"], 1990)
        self.assertEqual(test_book_2.title, "Good Omens")
        self.assertEqual(test_book_2.authors, ["Neil Gaiman", "Terry Pratchett"])
        self.assertEqual(test_book_2.year, 1990)

    def test_eq_1(self):
        book_1 = hw3.Book("Good Omens", ["Neil Gaiman", "Terry Pratchett"], 1990)
        book_2 = hw3.Book("Good Omens", ["Neil Gaiman", "Terry Pratchett"], 1990)
        self.assertEqual(book_1, book_2)

    def test_eq_2(self):
        book_1 = hw3.Book("Heads You Lose", ["Lisa Lutz", "David Hayward"], 2011)
        self.assertEqual(book_1, book_1)

# Function 1 Test:
    def test_getBooksByAuthor_1(self):
        book_1 = hw3.Book("B1", ["A", "B"], 2022)
        book_2 = hw3.Book("B2", ["A", "B", "C"], 2010)
        book_3 = hw3.Book("B3", ["B", "C"], 2000)
        list_of_book = [book_1, book_2, book_3]
        list_of_author = ["B", "A"]
        self.assertEqual(hw3.getBooksByAuthors(list_of_author, list_of_book), [book_1, book_2])

    def test_getBooksByAuthors_2(self):
        book_1 = hw3.Book("B1", ["A", "B", "C"], 2000)
        book_2 = hw3.Book("B2", ["C", "B"], 1909)
        book_3 = hw3.Book("B3", ["B", "A"], 2000)
        list_of_book_2 = [book_1, book_2, book_3]
        list_of_author_2 = ["B", "C"]
        self.assertEqual(hw3.getBooksByAuthors(list_of_author_2, list_of_book_2), [book_1, book_2])

    def test_belowAveragePay_1(self):
        employee_1 = hw3.Employee("A", 50, 3099)
        employee_2 = hw3.Employee("B", 60, 3099)
        employee_3 = hw3.Employee("C", 30, 2099)
        employee_4 = hw3.Employee("D", 10, 3099)
        employee_5 = hw3.Employee("E", 70, 3099)
        list_of_employee_test = [employee_1, employee_2, employee_3, employee_4, employee_5]
        list_of_name_test = ["D"]
        self.assertEqual(hw3.belowAveragePay(list_of_employee_test, 3099), list_of_name_test)

    def test_belowAveragePay_2(self):
        list_of_employee_test = []
        list_of_name = []
        self.assertEqual(hw3.belowAveragePay(list_of_employee_test, 100), list_of_name)

    def test_belowAveragePay_3(self):
        employee_1 = hw3.Employee("A", 50, 3099)
        employee_2 = hw3.Employee("B", 60, 3099)
        employee_3 = hw3.Employee("C", 30, 3099)
        employee_4 = hw3.Employee("D", 10, 3099)
        employee_5 = hw3.Employee("E", 70, 2099)
        empty = []
        list_of_employees = [employee_1, employee_2, employee_3, employee_4, employee_5]
        self.assertEqual(hw3.belowAveragePay(list_of_employees, 100), empty)

# A route from Atascadero through Santa Margarita to San Luis Obispo exists.
    def test_validate_route(self):
        p1_test = [["San Luis Obispo", "Santa Margarita"],
                   ["San Luis Obispo", "Pismo Beach"],
                   ["Atascadero", "Santa Margarita"],
                   ["Atascadero", "Creston"]]
        p2_test = ["Creston", "Pismo Beach"]
        self.assertFalse(hw3.validate_route(p1_test, p2_test), False)

# A route from Santa Margarita through San Luis Obispo to Pismo Beach exists
    def test_validate_route_2(self):
        p1_test = [["San Luis Obispo", "Santa Margarita"],
                   ["San Luis Obispo", "Pismo Beach"],
                   ["Atascadero", "Santa Margarita"],
                   ["Atascadero", "Creston"]]
        p2_test = ["Atascadero", "Santa Margarita", "San Luis Obispo", "Pismo Beach"]
        self.assertTrue(hw3.validate_route(p1_test, p2_test), True)

# An empty route is valid
    def test_validate_route_3(self):
        p1_test = [["San Luis Obispo", "Santa Margarita"],
                   ["San Luis Obispo", "Pismo Beach"],
                   ["Atascadero", "Santa Margarita"],
                   ["Atascadero", "Creston"]]
        p2_test = []
        self.assertTrue(hw3.validate_route(p1_test, p2_test), True)

# A single city route is valid
    def test_validate_route_4(self):
        p1_test = [["San Luis Obispo", "Santa Margarita"],
                   ["San Luis Obispo", "Pismo Beach"],
                   ["Atascadero", "Santa Margarita"],
                   ["Atascadero", "Creston"]]
        p2_test = ["San Luis Obispo"]
        self.assertTrue(hw3.validate_route(p1_test, p2_test), True)

# A route straight from Atascadero to Pismo Beach does not exist.
    def test_validate_route_5(self):
        p1_test = [["San Luis Obispo", "Santa Margarita"],
                   ["San Luis Obispo", "Pismo Beach"],
                   ["Atascadero", "Santa Margarita"],
                   ["Atascadero", "Creston"]]
        p2_test = ["Atascadero", "Pismo Beach"]
        self.assertFalse(hw3.validate_route(p1_test, p2_test), False)

    def test_groupIntoThree(self):
        num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(hw3.groupIntoThree(num_list), [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]])

    def test_groupIntoThree_2(self):
        num_list = [10, 11, 12, 13, 14, 15]
        self.assertEqual(hw3.groupIntoThree(num_list), [[10, 11, 12], [13, 14, 15]])

    def test_getLongestRepetition(self):
        test_list = [1, 1, 2, 2, 2, 1, 1, 1, 3]
        self.assertEqual(hw3.getLongestRepetition(test_list), 2)

    def test_getLongestRepetition_2(self):
        test_list = [1, 2, 2, 3, 3, 3]
        self.assertEqual(hw3.getLongestRepetition(test_list), 3)

    def test_getLongestRepetition_3(self):
        test_list = [4, 4, 4, 4, 4, 4, 3, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3]
        self.assertEqual(hw3.getLongestRepetition(test_list), 0)

    def test_getLongestRepetition_4(self):
        test_list = []
        self.assertEqual(hw3.getLongestRepetition(test_list), 0)

    def test_getLongestRepetition_5(self):
        test_list = [4, 3, 3, 3, 2, 2, 1, 3, 3, 3, 3, 3, 3]
        self.assertEqual(hw3.getLongestRepetition(test_list), 7)

    def test_getLongestRepetition_6(self):
        test_list = [1, 1, 2, 2, 2, 2, 1, 1, 1, 3]
        self.assertEqual(hw3.getLongestRepetition(test_list), 2)


if __name__ == "__main__":
    unittest.main()
