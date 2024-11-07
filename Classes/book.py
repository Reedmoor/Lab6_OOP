from Lab6_OOP.Classes.author import Author
class Book:
    def __init__(self, title, author: Author, year, available=True):
        self.title = title
        self.author = author
        self.year = year
        self.available = available

    def __str__(self):
        status = "Доступна" if self.available else "Недоступна"
        return f"'{self.title}' by {self.author}, {self.year} - {status}"

    def borrow(self):
        if self.available:
            self.available = False
            return True
        return False

    def return_book(self):
        self.available = True
