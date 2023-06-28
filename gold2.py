#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Book:
    def init(self, b_id, b_title, b_author):
        self.book_id = b_id
        self.title = b_title
        self.author = b_author
        self.is_available = True

class Library:
    def init(self, lib_name):
        self.name = lib_name
        self.collection = []

    def add_book(self, book):
        self.collection.append(book)

    def remove_book(self, book):
        self.collection.remove(book)

    def display_books(self):
        for book in self.collection:
            availability = "Available" if book.is_available else "Not Available"
            print(f"Book ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Availability: {availability}")

    def search_book(self, book_title):
        found_books = []
        for book in self.collection:
            if book_title.lower() in book.title.lower():
                found_books.append(book)
        if found_books:
            print(f"Found {len(found_books)} book(s) with matching title:")
            for book in found_books:
                availability = "Available" if book.is_available else "Not Available"
                print(f"Book ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Availability: {availability}")
        else:
            print("No books found with matching title.")

    def borrow_book(self, book_id):
        for book in self.collection:
            if book.book_id == book_id:
                if book.is_available:
                    book.is_available = False
                    print("Book borrowed successfully.")
                else:
                    print("Book is not available for borrowing.")
                return
        print("Book not found.")

    def return_book(self, book_id):
        for book in self.collection:
            if book.book_id == book_id:
                if not book.is_available:
                    book.is_available = True
                    print("Book returned successfully.")
                else:
                    print("Book is already available.")
                return
        print("Book not found.")


# Example usage
library = Library("My Library")

# Add books to the library
book1 = Book(1, "Python Crash Course", "Eric Matthes")
book2 = Book(2, "Learn Python the Hard Way", "Zed Shaw")
book3 = Book(3, "Automate the Boring Stuff with Python", "Al Sweigart")
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Display all books in the library
library.display_books()

# Search for a book by title
library.search_book("Python")

# Borrow a book
library.borrow_book(2)

# Return a book
library.return_book(2)

# Display all books in the library after borrowing and returning
library.display_books()

