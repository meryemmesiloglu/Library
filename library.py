import time
class Library:
    def __init__(self,filename="books.txt"):
        self.filename = filename
        self.file = open(self.filename, "a+")
        print(f"Opened {self.filename} successfully.")

    def __del__(self):
        self.file.close()
        print(f"Closed {self.filename} successfully.")

    def list_books(self):
        self.file.seek(0)
        books = self.file.readlines()
        if not books:
            print("No books available.")
        else:
            print("List of books:")
            for book in books[1:]:
                book = book.split(",")
                print("Book name: ", book[0], "Author: ", book[1])


    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        year = input("Enter first release year: ")
        pages = input("Enter number of pages: ")

        book_info = f"{title},{author},{year},{pages}\n"

        self.file.seek(0)
        books = self.file.readlines()
        for book in books:
            if book.strip() == book_info.strip():
                print("The book already exists.")
                return
        self.file.write(book_info)
        print("Book added successfully.")

    def remove_book(self):
        title_to_remove = input("Enter the title of the book to remove: ")
        self.file.seek(0)
        books = self.file.readlines()

        index_to_remove = -1
        for i, book in enumerate(books):
            if title_to_remove in book:
                index_to_remove = i
                break

        if index_to_remove == -1:
            print("Book not found.")
            return

        del books[index_to_remove]

        self.file.seek(0)
        self.file.truncate()

        for book in books:
            if title_to_remove not in book:
                self.file.write(book)

        print("Book removed successfully.")


if __name__ == "__main__":
    lib = Library()

    while True:
        print("*** MENU***")
        print("1) List Books")
        print("2) Add Book")
        print("3) Remove Book")
        print("4) Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            lib.list_books()
            time.sleep(2)
        elif choice == '2':
            lib.add_book()
            time.sleep(2)
        elif choice == '3':
            lib.remove_book()
            time.sleep(2)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")