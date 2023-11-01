import os
import csv

class LibraryManagementSystem:
    
    def __init__(self):
        self.book_list = []
        self.load_books()

    def load_books(self):
        try:
            with open('books.csv', mode='r', newline='') as file:
                reader = csv.reader(file)
                self.book_list = [row for row in reader]
        except FileNotFoundError:
            print("No previous data found.")

    def save_books(self):
        with open('books.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(self.book_list)
            
    def clearScreen(self):
        if os.name == 'posix':
            os.system('clear')
        else:
            os.system('cls')
            
    def isValidBookDetails(self, book_id, book_title, book_author):
        return book_id and book_title and book_author

    def addBook(self):
        self.clearScreen()
        print("Add Book")

        book_id = input("\nEnter Book ID: ")
        book_title = input("Enter Book Title: ")
        book_author = input("Enter Book Author: ")

        if not self.isValidBookDetails(book_id, book_title, book_author):
            print("Invalid book details.")
        else:
            self.book_list.append([book_id, book_title, book_author])
            print(f"\n{book_title} added successfully ")
            self.save_books()

    def deleteBook(self):
        self.clearScreen()
        print("Remove Book")

        book_id = input("\nEnter Book ID to delete: ")
        
        for book in self.book_list:
            if book[0] == book_id:
                self.book_list.remove(book)
                print("Book deleted successfully!")
                self.save_books()
                return
        print("\nBook ID does not exist.")

    def searchBook(self):
        self.clearScreen()
        print("Search Book")

        book_id = input("\nEnter Book ID to search: ")
        for book in self.book_list:
            if book[0] == book_id:
                print(f"Book found: ID:{book[0]}, Title:{book[1]}, Author:{book[2]}")
                return
        print("\nBook ID does not exist.")

    def updateBook(self):
        self.clearScreen()
        print("Update Book")
        book_id = input("\nEnter Book ID to update: ")
        for book in self.book_list:
            if book[0] == book_id:
                new_title = input("Enter new title: ")
                new_author = input("Enter new author: ")
                if not self.isValidBookDetails(book_id, new_title, new_author):
                    print("Invalid details. Try again.")
                    return
                book[1] = new_title
                book[2] = new_author
                print("Book updated successfully!")
                self.save_books()
                return
        print("\nBook ID does not exist.")

    def viewAllBooks(self):
        for book in self.book_list:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}")

    def runMenu(self):
        while True:
            print("\nLibrary Management System")
            print("\n1. Add book")
            print("2. Update book")
            print("3. List all book")
            print("4. Search book")
            print("5. Remove book")
            print("6. Exit")

            choice = input("\nEnter your choice: ")

            if choice == '1':
                self.addBook()
            elif choice == '2':
                self.updateBook()
            elif choice == '3':
                self.viewAllBooks()
            elif choice == '4':
                self.searchBook()
            elif choice == '5':
                self.deleteBook()
            elif choice == '6':
                print("\nExiting system.")
                break
            else:
                print("\nInvalid choice. Try again.")

            input("\nPress Enter to continue...")
            self.clearScreen()

if __name__ == "__main__":
    system = LibraryManagementSystem()
    system.runMenu()
