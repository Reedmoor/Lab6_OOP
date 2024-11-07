import json
from Lab6_OOP.Classes.author import Author
from Lab6_OOP.Classes.book import Book

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

    def save_to_file(self, filename="library.json"):
        """Сохраняет данные библиотеки в файл JSON."""
        data = []
        for book in self.books:
            data.append({
                "title": book.title,
                "author": book.author.name,
                "year": book.year,
                "available": book.available
            })

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print("Данные библиотеки сохранены в файл.")

    def load_from_file(self, filename="library.json"):
        """Загружает данные библиотеки из файла JSON."""
        try:
            with open(filename, "r", encoding="utf-8") as file:
                content = file.read().strip()
                if not content:  # Проверка на пустой файл
                    print(f"Файл '{filename}' пустой. Создаём пустую библиотеку.")
                    return
                data = json.loads(content)
            for book_data in data:
                author = Author(book_data["author"], 0)  # Для примера, год рождения можно не учитывать
                book = Book(book_data["title"], author, book_data["year"], book_data["available"])
                self.add_book(book)
            print("Данные библиотеки загружены из файла.")
        except FileNotFoundError:
            print(f"Файл '{filename}' не найден. Создана пустая библиотека.")
        except json.JSONDecodeError:
            print(f"Ошибка при разборе данных в файле '{filename}'. Возможно, файл повреждён.")
