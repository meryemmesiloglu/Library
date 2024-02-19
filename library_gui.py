import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTabWidget, QLabel, QLineEdit, \
    QPushButton, QCheckBox, QListWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox


class BookManager(QMainWindow):
    def __init__(self,filename = "books.txt"):
        self.filename = filename
        self.file = open(self.filename, "a+")
        print(f"Opened {self.filename} successfully.")


        super().__init__()
        self.setGeometry(250, 100, 500, 475)
        self.setWindowTitle("Book Manager")
        self.setStyleSheet("background-color:#87CEFA")

        self.tabs = QTabWidget()
        self.list_books_tab = QWidget()
        self.add_books_tab = QWidget()
        self.remove_books_tab = QWidget()

        self.setup_list_books_tab()
        self.setup_add_books_tab()
        self.setup_remove_books_tab()

        self.tabs.addTab(self.list_books_tab, "List Books")
        self.tabs.addTab(self.add_books_tab, "Add Books")
        self.tabs.addTab(self.remove_books_tab, "Remove Books")
        self.tabs.setStyleSheet(
            "QTabBar::tab { background: transparent;width: 140px;font-size: 20px; padding: 20px 10px;color:#4682B4;}")
        self.tabs.tabBar().setMinimumWidth(300)
        self.setCentralWidget(self.tabs)
    def __del__(self):
        try:
            self.file.close()
            print(f"Closed {self.filename} successfully.")
        except Exception as e:
            print(f"Error: {e}")
    def setup_list_books_tab(self):
        self.list_books_tab.layout = QVBoxLayout()
        self.list_books_tab.setStyleSheet("background: transparent;")
        checkboxes_layout = QHBoxLayout()
        self.title_checkbox = QCheckBox("Title")
        self.author_checkbox = QCheckBox("Author")
        self.year_checkbox = QCheckBox("Year")
        self.pages_checkbox = QCheckBox("Pages")
        self.title_checkbox.setStyleSheet(
            """
            QCheckBox {
                padding: 5px;
                font-size: 20px;
                color: #4682B4;
                font-family: Helvetica;

            }
            """
        )
        self.author_checkbox.setStyleSheet(
            """
            QCheckBox {
                padding: 5px;
                font-size: 20px;
                color: #4682B4;
                font-family: Helvetica;

            }
            """
        )
        self.year_checkbox.setStyleSheet(
            """
            QCheckBox {
                padding: 5px;
                font-size: 20px;
                color: #4682B4;
                font-family: Helvetica;

            }
            """
        )
        self.pages_checkbox.setStyleSheet(
            """
            QCheckBox {
                padding: 5px;
                font-size: 20px;
                color: #4682B4;
                font-family: Helvetica;

            }
            """
        )
        checkboxes_layout.addWidget(self.title_checkbox)
        checkboxes_layout.addWidget(self.author_checkbox)
        checkboxes_layout.addWidget(self.year_checkbox)
        checkboxes_layout.addWidget(self.pages_checkbox)

        self.list_button = QPushButton("List")
        self.list_button.setFixedSize(500, 50)
        self.list_button.setStyleSheet(
            """
            QPushButton {
                background-color: #AFEEEE;
                border-style: solid;
                border-width: 2px;
                border-color: #4682B4;
                border-radius: 10px;
                padding: 5px;
                font-size: 20px;
                color: #4682B4;
                font-family: Helvetica
            }

            QPushButton:hover {
                background-color: #87CEFA;
            }

            QPushButton:pressed {
                background-color: #1E90FF;
            }
            """
        )
        self.list_button.clicked.connect(self.list_books)

        self.list_box = QListWidget()
        self.list_box.setStyleSheet(
            "QListWidget { padding-left: 20px; font-size: 24px; font-family: Helvetica; background: white }")
        self.list_box.setFixedSize(500, 400)
        font = QFont("Helvetica", 24)

        self.title_checkbox.setFont(font)
        self.author_checkbox.setFont(font)
        self.year_checkbox.setFont(font)
        self.pages_checkbox.setFont(font)
        self.list_button.setFont(font)

        self.list_books_tab.layout.addLayout(checkboxes_layout)
        self.list_books_tab.layout.addWidget(self.list_button)
        self.list_books_tab.layout.addWidget(self.list_box)

        self.list_books_tab.setLayout(self.list_books_tab.layout)

    def setup_add_books_tab(self):
        self.add_books_tab.layout = QVBoxLayout()
        self.add_books_tab.setStyleSheet("background: transparent;")
        font = QFont("Helvetica", 24)

        self.title_label = QLabel("Title:")
        self.title_label.setStyleSheet(
            """
            QLabel {
                padding: 5px;
                font-size: 20px;
                color: #4682B4;
                font-family: Helvetica;

            }
            """
        )
        self.title_lineedit = QLineEdit()
        self.title_lineedit.setFixedSize(500, 50)
        self.title_lineedit.setStyleSheet(
            """
            QPushButton, QLineEdit {
                background-color: #AFEEEE;
                border-style: solid;
                border-width: 2px;
                border-color: #4682B4;
                border-radius: 10px;
                padding: 5px;
                font-size: 20px;
                color: #4682B4;
                font-family: Helvetica

            }"""
        )

        self.author_label = QLabel("Author:")
        self.author_label.setStyleSheet(
            """
            QLabel {
                padding: 5px;
                font-size: 20px;
                color: #4682B4;
                font-family: Helvetica;

            }
            """
        )
        self.author_lineedit = QLineEdit()
        self.author_lineedit.setFixedSize(500, 50)
        self.author_lineedit.setStyleSheet(
            """
                 QPushButton, QLineEdit {
                     background-color: #AFEEEE;
                     border-style: solid;
                     border-width: 2px;
                     border-color: #4682B4;
                     border-radius: 10px;
                     padding: 5px;
                     font-size: 20px;
                     color: #4682B4;
                     font-family: Helvetica

                 }"""
        )
        self.year_label = QLabel("Year:")
        self.year_label.setStyleSheet(
            """
            QLabel {
                padding: 5px;
                font-size: 20px;
                color: #4682B4;
                font-family: Helvetica;

            }
            """
        )
        self.year_lineedit = QLineEdit()
        self.year_lineedit.setFixedSize(500, 50)
        self.year_lineedit.setStyleSheet(
            """
                 QPushButton, QLineEdit {
                     background-color: #AFEEEE;
                     border-style: solid;
                     border-width: 2px;
                     border-color: #4682B4;
                     border-radius: 10px;
                     padding: 5px;
                     font-size: 20px;
                     color: #4682B4;
                     font-family: Helvetica

                 }"""
        )

        self.pages_label = QLabel("Pages:")
        self.pages_label.setStyleSheet(
            """
            QLabel {
                padding: 5px;
                font-size: 20px;
                color: #4682B4;
                font-family: Helvetica;

            }
            """
        )
        self.pages_lineedit = QLineEdit()
        self.pages_lineedit.setFixedSize(500, 50)
        self.pages_lineedit.setStyleSheet(
            """
                 QPushButton, QLineEdit {
                     background-color: #AFEEEE;
                     border-style: solid;
                     border-width: 2px;
                     border-color: #4682B4;
                     border-radius: 10px;
                     padding: 5px;
                     font-size: 20px;
                     color: #4682B4;
                     font-family: Helvetica

                 }"""
        )
        self.add_button = QPushButton("Add")
        self.add_button.setFixedSize(500, 50)
        self.add_button.setStyleSheet(
            """
            QPushButton {
                background-color: #AFEEEE;
                border-style: solid;
                border-width: 2px;
                border-color: #4682B4;
                border-radius: 10px;
                padding: 5px;
                font-size: 20px;
                color: #4682B4;
                font-family: Helvetica
            }

            QPushButton:hover {
                background-color: #87CEFA;
            }

            QPushButton:pressed {
                background-color: #1E90FF;
            }
            """
        )
        self.add_button.clicked.connect(self.add_book)
        self.add_button.setFont(font)

        self.add_books_tab.layout.addWidget(self.title_label)
        self.add_books_tab.layout.addWidget(self.title_lineedit)
        self.add_books_tab.layout.addWidget(self.author_label)
        self.add_books_tab.layout.addWidget(self.author_lineedit)
        self.add_books_tab.layout.addWidget(self.year_label)
        self.add_books_tab.layout.addWidget(self.year_lineedit)
        self.add_books_tab.layout.addWidget(self.pages_label)
        self.add_books_tab.layout.addWidget(self.pages_lineedit)
        self.add_books_tab.layout.addWidget(self.add_button)

        self.add_books_tab.setLayout(self.add_books_tab.layout)

    def setup_remove_books_tab(self):
        self.remove_books_tab.layout = QVBoxLayout()
        self.remove_books_tab.setStyleSheet("background: transparent;")

        self.remove_label = QLabel("Enter book title to remove:")
        self.remove_label.setStyleSheet(
            """
            QLabel {
                padding: 5px;
                font-size: 20px;
                color: #4682B4;
                font-family: Helvetica;
            }
            """
        )

        self.remove_lineedit = QLineEdit()
        self.remove_lineedit.setStyleSheet(
            """
            QPushButton, QLineEdit {
                background-color: #AFEEEE;
                border-style: solid;
                border-width: 2px;
                border-color: #4682B4;
                border-radius: 10px;
                padding: 5px;
                font-size: 16px;
            }
            """
        )
        self.remove_lineedit.setFixedSize(500, 50)

        self.remove_button = QPushButton("Remove")
        self.remove_button.setFixedSize(500, 50)
        self.remove_button.setStyleSheet(
            """
            QPushButton {
                background-color: #AFEEEE;
                border-style: solid;
                border-width: 2px;
                border-color: #4682B4;
                border-radius: 10px;
                padding: 5px;
                font-size: 20px;
                color: #4682B4;
                font-family: Helvetica
            }

            QPushButton:hover {
                background-color: #87CEFA;
            }

            QPushButton:pressed {
                background-color: #1E90FF;
            }
            """
        )
        self.remove_button.clicked.connect(self.remove_book)

        self.image_label = QLabel()
        pixmap = QPixmap("bg.png").scaled(300, 300)
        self.image_label.setPixmap(pixmap)
        self.image_label.setAlignment(Qt.AlignCenter)

        self.remove_books_tab.layout.addWidget(self.remove_label)
        self.remove_books_tab.layout.addWidget(self.remove_lineedit)
        self.remove_books_tab.layout.addWidget(self.remove_button)
        self.remove_books_tab.layout.addWidget(self.image_label)
        self.remove_books_tab.layout.addStretch()

        self.remove_books_tab.setLayout(self.remove_books_tab.layout)

    def list_books(self):
        self.list_box.clear()

        selected_fields = []

        if self.title_checkbox.isChecked():
            selected_fields.append("Title")
        if self.author_checkbox.isChecked():
            selected_fields.append("Author")
        if self.year_checkbox.isChecked():
            selected_fields.append("Year")
        if self.pages_checkbox.isChecked():
            selected_fields.append("Pages")

        with open("books.txt", "r") as file:
            for line in file:
                fields = line.strip().split(", ")

                if len(fields) >= 4:
                    display_text = ""
                    for field in selected_fields:
                        if field == "Title":
                            display_text += f"Title: {fields[0]}, "
                        elif field == "Author":
                            display_text += f"Author: {fields[1]}, "
                        elif field == "Year":
                            display_text += f"Year: {fields[2]}, "
                        elif field == "Pages":
                            display_text += f"Pages: {fields[3]}, "

                    self.list_box.addItem(display_text[:-2])
                else:
                    print("Error: Line does not have enough fields")
    def add_book(self):
        title = self.title_lineedit.text()
        author = self.author_lineedit.text()
        year = self.year_lineedit.text()
        pages = self.pages_lineedit.text()

        book_info = f"{title},{author},{year},{pages}\n"

        self.file.seek(0)
        books = self.file.readlines()
        for book in books:
            if book.strip() == book_info.strip():
                msg_box = QMessageBox()
                msg_box.setWindowTitle("Error")
                msg_box.setText("Book alredy exis!")
                msg_box.exec_()
                return
        self.file.write(book_info)
        self.title_lineedit.clear()
        self.author_lineedit.clear()
        self.year_lineedit.clear()
        self.pages_lineedit.clear()
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Success")
        msg_box.setText("Book successfully added!")
        msg_box.exec_()
    def remove_book(self):
        title_to_remove = self.remove_lineedit.text()
        self.file.seek(0)
        books = self.file.readlines()

        index_to_remove = -1
        for i, book in enumerate(books):
            if title_to_remove in book:
                index_to_remove = i
                break

        if index_to_remove == -1:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Error")
            msg_box.setText("Book does not found!")
            msg_box.exec_()
            self.remove_lineedit.clear()
            return

        del books[index_to_remove]

        self.file.seek(0)
        self.file.truncate()

        for book in books:
            if title_to_remove not in book:
                self.file.write(book)

        msg_box = QMessageBox()
        msg_box.setWindowTitle("Success")
        msg_box.setText("Book Successfuly removed!")
        msg_box.exec_()
        self.remove_lineedit.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BookManager()
    window.show()
    sys.exit(app.exec_())
