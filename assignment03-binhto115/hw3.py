# Name: Binh To
# Date: 10/25/2022
# Github: 113943258

from typing import List
from typing import Optional


class Employee:
    def __init__(self, name: str, pay_rate: int, job_code: int):
        self.name = name
        self.pay_rate = pay_rate
        self.job_code = job_code

    def __repr__(self):
        return f"Employee({self.name},{self.pay_rate},{self.job_code})"

    def __eq__(self, other):
        return (other is self or
                type(other) == Employee and
                self.name == other.name and
                self.pay_rate == other.pay_rate and
                self.job_code == other.job_code)


# Part 1:
class Book:
    """The class Book's __init__ initiates a book's attributes:
     title, a list of authors, and the year the boo was published.
    The __repr__ allows us to return the objects in string format.
    The __eq__ allows us to compare between two book objects"""
    def __init__(self, title: str, authors: List[str], year: int):
        self.title = title
        self.authors = authors
        self.year = year

    def __repr__(self) -> str:
        return f"Book({self.title},{self.authors},{self.year})"

    def __eq__(self, other) -> bool:
        return (other is self or
                type(other) == Book and
                self.title == other.title and
                self.authors == other.authors and
                self.year == other.year)


def getBooksByAuthors(p1: List[str], p2: List[Book]) -> List[Book]:
    """The function getBooksByAuthors returns a list of books
    written by the specified list of inputted authors"""
    book_list = []
    for i in p2:
        book_name = i.title
        book_author = i.authors
        book_year = i.year
        sorted_list = all(j in book_author for j in p1)
        if sorted_list:
            book = Book(book_name, book_author, book_year)
            book_list.append(book)
    return book_list


# Part 2
def belowAveragePay(p1: List[Employee], p2: int) -> List[str]:
    """This function returns a list of employees with matching job_code
    whose pay_rate is under the average pay_rate
    If none of the employees' job_code matches the input job_code
    or the list is empty, then return empty list"""
    sum_of_pay_rate = 0
    list_of_sorted_employee = []
    list_of_sorted_pay_rate = []
    empty_list = []
    output_empty_list = []
    list_of_names = []
    # Sort out the list to find average
    for i in p1:
        name = i.name
        pay_rate = i.pay_rate
        job_code = i.job_code
        if job_code == p2:
            employee = Employee(name, pay_rate, job_code)
            list_of_sorted_employee.append(employee)
            list_of_sorted_pay_rate.append(pay_rate)

    for a in p1:
        if a == empty_list:
            return output_empty_list
    # Find the average
    for j in list_of_sorted_pay_rate:
        sum_of_pay_rate += j

    for c in list_of_sorted_employee:
        length_of_list = len(list_of_sorted_pay_rate)
        average = sum_of_pay_rate / length_of_list
        c_pay_rate = c.pay_rate
        if c_pay_rate < average:
            name = c.name
            list_of_names.append(name)
    return list_of_names


# Part 3:
def validate_route(p1: List[List[str]], p2: List[str]) -> bool:
    """Determine if a route exists.
     A route of a single city or an empty route exists
     A route is not exist if there is no intermediate city between the route"""
    empty = []
    if p2 == empty or len(p2) == 1:
        return True
    for i in p1:
        if all(item in p2 for item in i):
            return True
        else:
            return False


# Part 4:
def groupIntoThree(p: List[int]) -> List[List[int]]:
    """Group the first three elements to a list,
    then group the next elements into a list
    of three, and so on. If the last elements are less than three,
    then also group those elements"""
    list_of_grouped = []
    for i in range(0, len(p), 3):
        sublist = p[i:i+3]
        list_of_grouped.append(sublist)
    return list_of_grouped


# Part 5:
def getLongestRepetition(p: List[int]) -> Optional[int]:
    """Return the index of the longest repeated number in a list
    if the list is empty then return 0, or nothing"""
    empty_list = []
    index_of_longest_repetition = 0
    current_length = 0
    longest_length = 0
    temp_index = 0
    for i in range(len(p)):
        if i == empty_list:
            return None
        elif p[i] != p[i - 1]:
            if current_length > longest_length:
                longest_length = current_length
                index_of_longest_repetition = temp_index
            current_length = 1
            temp_index = ist
    if current_length > longest_length:
        longest_length = current_length
        index_of_longest_repetition = temp_index
        print("The current length is " + str(current_length))
        print("The longest length is " + str(longest_length))
        print("The index of the longest repetition is " + str(index_of_longest_repetition))
    return index_of_longest_repetition

