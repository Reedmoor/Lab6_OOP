# main.py
from Lab6_OOP.Classes.author import Author
from Lab6_OOP.Classes.book import Book
from Lab6_OOP.Classes.library import Library


def main():
    # Создание библиотеки
    library = Library()

    # Попытка загрузить данные из файла
    library.load_from_file()

    # Если библиотека пуста (после загрузки), добавляем книги вручную
    if len(library.books) == 0:
        # Создание авторов
        author1 = Author("Джордж Оруэлл", 1903)
        author2 = Author("Харпер Ли", 1926)

        # Создание книг
        book1 = Book("1984", author1, 1949)
        book2 = Book("Убить пересмешника", author2, 1960)

        # Добавление книг в библиотеку
        library.add_book(book1)
        library.add_book(book2)

    # Вывод списка книг
    library.list_books()

    # Взятие книги на чтение
    library.borrow_book("1984")

    # Попытка повторного взятия той же книги
    library.borrow_book("1984")

    # Возврат книги
    # library.return_book("1984")

    # Снова вывод списка книг
    library.list_books()

    # Сохранение состояния библиотеки в файл
    library.save_to_file()

if __name__ == "__main__":
    main()
