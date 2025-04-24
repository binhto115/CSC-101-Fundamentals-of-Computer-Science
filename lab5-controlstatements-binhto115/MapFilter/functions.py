# Name: Binh To
# Date: 10/19/2022
# Github: 113943258

import objects
Book = objects.Book


def getAuthors(p: list[Book]) -> list[str]:
    list_author = []
    for book in p:
        author_list = book.author
        list_author.append(author_list)
    return list_author


def getBooksBeforeYear(p1: list[Book], p2: int) -> list[Book]:
    book_list = []
    for book in p1:
        book_title = book.title
        book_author = book.author
        book_year = book.year
        if book_year < p2:
            book_input = Book(book_title, book_author, book_year)
            book_list.append(book_input)
    return book_list


def getAuthorsLC(p: list[Book]) -> list[str]:
    authors_list = [i.author for i in p]
    return authors_list


def getBooksBeforeYearLC(p: list[Book], p2: int) -> list[Book]:
    book_list = [Book(i.title, i.author, i.year) for i in p if i.year < p2]
    return book_list
