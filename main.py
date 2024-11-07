from Classes.author import Author
from Classes.book import Book
from Classes.library import Library
# Создание авторов
author1 = Author("Джордж Оруэлл", 1903)
author2 = Author("Харпер Ли", 1926)

# Создание книг
book1 = Book("1984", author1, 1949)
book2 = Book("Убить пересмешника", author2, 1960)

# Создание библиотеки и добавление книг
library = Library()
library.add_book(book1)
library.add_book(book2)

# Вывод списка книг
library.list_books()

# Взятие книги на чтение
library.borrow_book("1984")

# Попытка повторного взятия той же книги
library.borrow_book("1984")

# Возврат книги
library.return_book("1984")

# Снова вывод списка книг
library.list_books()
