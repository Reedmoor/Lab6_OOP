from Classes.book import Book
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)
        print(f"Книга '{book.title}' добавлена в библиотеку.")

    def list_books(self):
        print("Список книг в библиотеке:")
        for book in self.books:
            print(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.borrow():
                    print(f"Вы взяли книгу: '{title}'")
                    return
                else:
                    print(f"Книга '{title}' недоступна.")
                    return
        print(f"Книга '{title}' не найдена в библиотеке.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.return_book()
                print(f"Вы вернули книгу: '{title}'")
                return
        print(f"Книга '{title}' не найдена в библиотеке.")
