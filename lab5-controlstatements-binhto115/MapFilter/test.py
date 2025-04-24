# Name: 113943258
# Date: 10/19/2022
# Github: 113943258

import unittest
import objects
import functions


class MapFilterTest(unittest.TestCase):
    def test_getAuthors(self):
        # First Test:
        book_1 = objects.Book("1984", "George Orwell", 1949)
        book_2 = objects.Book("Harry Potter and the Chamber of Secret", "J.K. Rowling", 1998)
        book_3 = objects.Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 1997)
        list_of_books = [book_1, book_2, book_3]
        list_of_authors = ["George Orwell", "J.K. Rowling", "J.K. Rowling"]
        self.assertEqual(functions.getAuthors(list_of_books), list_of_authors)
        #Second Test:
        book_4 = objects.Book("Harry Potter and the Goblet of Fire", "J.K. Rowling", 2000)
        book_5 = objects.Book("Harry Potter and the Order of Phoenix", "J.K. Rowling", 2003)
        book_6 = objects.Book("Harry Potter and the Prisoner of Azkaban", "J.K. Rowling", 1999)
        book_7 = objects.Book("Harry Potter and the Half-Blood Prince", "J.K. Rowling", 2005)
        list_of_books_2 = [book_4, book_5, book_6, book_7]
        list_of_authors_2 = ["J.K. Rowling", "J.K. Rowling", "J.K. Rowling", "J.K. Rowling"]
        self.assertEqual(functions.getAuthors(list_of_books_2), list_of_authors_2)

    def test_getBooksBeforeYear(self):
        # First Test:
        book_1 = objects.Book("1984", "George Orwell", 1949)
        book_2 = objects.Book("Harry Potter and the Chamber of Secret", "J.K. Rowling", 1998)
        book_3 = objects.Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 1997)
        book_4 = objects.Book("Harry Potter and the Goblet of Fire", "J.K. Rowling", 2000)
        list_of_books = [book_1, book_2, book_3, book_4]
        books = [book_1, book_2, book_3]
        self.assertEqual(functions.getBooksBeforeYear(list_of_books, 2000), books)
        # Second Test:
        book_5 = objects.Book("Harry Potter and the Deathly Hallows", "J.K. Rowling", 2007)
        book_6 = objects.Book("Harry Potter and the Order of Phoenix", "J.K. Rowling", 2003)
        book_7 = objects.Book("Harry Potter and the Prisoner of Azkaban", "J.K. Rowling", 1999)
        book_8 = objects.Book("Harry Potter and the Half-Blood Prince", "J.K. Rowling", 2005)
        list_of_books_2 = [book_5, book_6, book_7, book_8]
        books_2 = [book_5, book_6, book_7, book_8]
        self.assertEqual(functions.getBooksBeforeYear(list_of_books_2, 2022), books_2)

    def test_getAuthorsLC(self):
        # Test 1:
        book_1 = objects.Book("Harry Potter and the Deathly Hallows", "J.K. Rowling", 2007)
        book_2 = objects.Book("1984", "George Orwell", 1949)
        book_3 = objects.Book("Harry Potter and the Prisoner of Azkaban", "J.K. Rowling", 1999)
        list_of_books = [book_1, book_2, book_3]
        list_of_authors = ["J.K. Rowling", "George Orwell", "J.K. Rowling"]
        self.assertEqual(functions.getAuthors(list_of_books), list_of_authors)
        # Test 2:
        book_4 = objects.Book("Harry Potter and the Goblet of Fire", "J.K. Rowling", 2000)
        book_5 = objects.Book("Harry Potter and the Order of Phoenix", "J.K. Rowling", 2003)
        book_6 = objects.Book("Harry Potter and the Half-Blood Prince", "J.K. Rowling", 2005)
        list_of_books_2 = [book_4, book_5, book_6]
        list_of_authors_2 = ["J.K. Rowling", "J.K. Rowling", "J.K. Rowling"]
        self.assertEqual(functions.getAuthors(list_of_books_2), list_of_authors_2)

    def test_getBooksBeforeYearLC(self):
        # First Test:
        book_1 = objects.Book("1984", "George Orwell", 1949)
        list_of_books = [book_1]
        books = [book_1]
        self.assertEqual(functions.getBooksBeforeYear(list_of_books, 1950), books)

        # Second Test:
        book_5 = objects.Book("Harry Potter and the Deathly Hallows", "J.K. Rowling", 2007)
        book_6 = objects.Book("Harry Potter and the Order of Phoenix", "J.K. Rowling", 2003)
        book_7 = objects.Book("Harry Potter and the Prisoner of Azkaban", "J.K. Rowling", 1999)
        book_8 = objects.Book("Harry Potter and the Half-Blood Prince", "J.K. Rowling", 2005)
        list_of_books_2 = [book_5, book_6, book_7, book_8]
        books_2 = [book_5, book_6, book_7, book_8]
        self.assertEqual(functions.getBooksBeforeYear(list_of_books_2, 2022), books_2)


if __name__ == "__main__":
    unittest.main()
