# Name: Binh To
# Date: 10/19/2022
# Github: 113943258

class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self) -> str:
        return f"Book({self.title},{self.author},{self.year})"

    def __eq__(self, other) -> bool:
        return (other is self or
                type(other) == Book and
                self.title == other.title and
                self.author == other.author and
                self.year == other.year)
