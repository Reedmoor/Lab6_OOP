from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys
from datetime import datetime
from Lab6_OOP.Classes.author import Author
from Lab6_OOP.Classes.book import Book
from Lab6_OOP.Classes.library import Library


class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(550, 410)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Main)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 100, 531, 44))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.SearchGroup = QtWidgets.QGridLayout(self.horizontalLayoutWidget)
        self.SearchGroup.setContentsMargins(0, 0, 0, 0)
        self.SearchGroup.setObjectName("SearchGroup")
        self.SearchEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.SearchEdit.setText("")
        self.SearchEdit.setObjectName("SearchEdit")
        self.SearchGroup.addWidget(self.SearchEdit, 1, 0, 1, 1)
        self.SearchButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.SearchButton.setObjectName("SearchButton")
        self.SearchGroup.addWidget(self.SearchButton, 1, 1, 1, 1)
        self.SearchLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.SearchLabel.setObjectName("SearchLabel")
        self.SearchGroup.addWidget(self.SearchLabel, 0, 0, 1, 1)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Main)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 30, 531, 70))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.AddGroup = QtWidgets.QGridLayout(self.horizontalLayoutWidget_2)
        self.AddGroup.setContentsMargins(0, 0, 0, 0)
        self.AddGroup.setObjectName("AddGroup")
        self.NameEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.NameEdit.setText("")
        self.NameEdit.setObjectName("NameEdit")
        self.AddGroup.addWidget(self.NameEdit, 1, 0, 1, 1)
        self.GenreEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.GenreEdit.setText("")
        self.GenreEdit.setObjectName("GenreEdit")
        self.AddGroup.addWidget(self.GenreEdit, 1, 2, 1, 1)
        self.DateEdit = QtWidgets.QDateEdit(self.horizontalLayoutWidget_2)
        self.DateEdit.setObjectName("DateEdit")
        self.AddGroup.addWidget(self.DateEdit, 1, 3, 1, 1)
        self.AddLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.AddLabel.setObjectName("AddLabel")
        self.AddGroup.addWidget(self.AddLabel, 0, 0, 1, 1)
        self.AuthorEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.AuthorEdit.setText("")
        self.AuthorEdit.setObjectName("AuthorEdit")
        self.AddGroup.addWidget(self.AuthorEdit, 1, 1, 1, 1)
        self.SubmitButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.SubmitButton.setObjectName("SubmitButton")
        self.AddGroup.addWidget(self.SubmitButton, 2, 0, 1, 4)
        self.label_4 = QtWidgets.QLabel(Main)
        self.label_4.setGeometry(QtCore.QRect(240, 10, 71, 16))
        self.label_4.setObjectName("label_4")
        self.gridLayoutWidget = QtWidgets.QWidget(Main)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 150, 531, 251))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.BooksGroup = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.BooksGroup.setContentsMargins(0, 0, 0, 0)
        self.BooksGroup.setObjectName("BooksGroup")
        self.BookLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.BookLabel.setObjectName("BookLabel")
        self.BooksGroup.addWidget(self.BookLabel, 1, 0, 1, 1)
        self.BookTable = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.BookTable.setObjectName("BookTable")
        self.BookTable.setColumnCount(5)
        self.BookTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.BookTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.BookTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.BookTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.BookTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.BookTable.setHorizontalHeaderItem(4, item)
        self.BooksGroup.addWidget(self.BookTable, 2, 0, 1, 1)

        # Set up the table for context menu
        self.BookTable.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "БД Библиотека"))
        self.SearchEdit.setPlaceholderText(_translate("Main", "Введите название книги"))
        self.SearchButton.setText(_translate("Main", "Поиск"))
        self.SearchLabel.setText(_translate("Main", "Поиск книг:"))
        self.NameEdit.setPlaceholderText(_translate("Main", "Введите название книги"))
        self.GenreEdit.setPlaceholderText(_translate("Main", "Введите жанр книги"))
        self.AddLabel.setText(_translate("Main", "Добавление книги в базу данных:"))
        self.AuthorEdit.setPlaceholderText(_translate("Main", "Введите имя автора"))
        self.SubmitButton.setText(_translate("Main", "Добавить запись"))
        self.label_4.setText(_translate("Main", "БИБЛИОТЕКА"))
        self.BookLabel.setText(_translate("Main", "Имеющиеся книги в базе данных:"))
        item = self.BookTable.horizontalHeaderItem(0)
        item.setText(_translate("Main", "№ книги"))
        item = self.BookTable.horizontalHeaderItem(1)
        item.setText(_translate("Main", "Название книги"))
        item = self.BookTable.horizontalHeaderItem(2)
        item.setText(_translate("Main", "Автор книги"))
        item = self.BookTable.horizontalHeaderItem(3)
        item.setText(_translate("Main", "Жанр книги"))
        item = self.BookTable.horizontalHeaderItem(4)
        item.setText(_translate("Main", "Дата публикации"))


class LibraryApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Main()
        self.ui.setupUi(self)

        # Initialize library
        self.library = Library()
        self.library.load_from_file()

        # Connect signals
        self.ui.SubmitButton.clicked.connect(self.add_book)
        self.ui.SearchButton.clicked.connect(self.search_books)
        self.ui.SearchEdit.returnPressed.connect(self.search_books)
        self.ui.BookTable.customContextMenuRequested.connect(self.show_context_menu)

        # Set current date as default
        self.ui.DateEdit.setDate(QtCore.QDate.currentDate())

        # Update table
        self.update_book_table()

    def add_book(self):
        """Add a new book to the library."""
        title = self.ui.NameEdit.text().strip()
        author_name = self.ui.AuthorEdit.text().strip()
        genre = self.ui.GenreEdit.text().strip()
        date = self.ui.DateEdit.date().toString("yyyy")

        if not all([title, author_name, genre]):
            QMessageBox.warning(self, "Ошибка", "Все поля должны быть заполнены!")
            return

        # Create author and book objects
        author = Author(author_name, 0)  # Birth year set to 0 as it's not in UI
        book = Book(title, author, int(date))

        # Add book to library
        self.library.add_book(book)
        self.library.save_to_file()

        # Clear input fields
        self.ui.NameEdit.clear()
        self.ui.AuthorEdit.clear()
        self.ui.GenreEdit.clear()
        self.ui.DateEdit.setDate(QtCore.QDate.currentDate())

        # Update table
        self.update_book_table()
        QMessageBox.information(self, "Успех", "Книга успешно добавлена!")

    def update_book_table(self, books=None):
        """Update the book table with all or filtered books."""
        if books is None:
            books = self.library.books

        self.ui.BookTable.setRowCount(len(books))
        for row, book in enumerate(books):
            self.ui.BookTable.setItem(row, 0, QtWidgets.QTableWidgetItem(str(row + 1)))
            self.ui.BookTable.setItem(row, 1, QtWidgets.QTableWidgetItem(book.title))
            self.ui.BookTable.setItem(row, 2, QtWidgets.QTableWidgetItem(book.author.name))
            self.ui.BookTable.setItem(row, 3, QtWidgets.QTableWidgetItem(""))  # Genre not in Book class
            self.ui.BookTable.setItem(row, 4, QtWidgets.QTableWidgetItem(str(book.year)))

    def search_books(self):
        """Search for books by title."""
        search_text = self.ui.SearchEdit.text().lower().strip()
        if not search_text:
            self.update_book_table()
            return

        filtered_books = [book for book in self.library.books
                          if search_text in book.title.lower()]
        self.update_book_table(filtered_books)

    def show_context_menu(self, position):
        """Show context menu for book operations."""
        menu = QtWidgets.QMenu()
        borrow_action = menu.addAction("Взять книгу")
        return_action = menu.addAction("Вернуть книгу")
        delete_action = menu.addAction("Удалить книгу")

        action = menu.exec_(self.ui.BookTable.mapToGlobal(position))

        if action:
            row = self.ui.BookTable.currentRow()
            if row >= 0:
                title = self.ui.BookTable.item(row, 1).text()

                if action == borrow_action:
                    self.library.borrow_book(title)
                elif action == return_action:
                    self.library.return_book(title)
                elif action == delete_action:
                    self.delete_book(row)

                self.library.save_to_file()
                self.update_book_table()

    def delete_book(self, row):
        """Delete a book from the library."""
        reply = QMessageBox.question(self, 'Подтверждение',
                                     'Вы уверены, что хотите удалить эту книгу?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            del self.library.books[row]
            self.library.save_to_file()
            QMessageBox.information(self, "Успех", "Книга удалена!")


def main():
    app = QApplication(sys.argv)
    window = LibraryApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()