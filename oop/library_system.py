#!/usr/bin/env python3
"""
library_system.py: Defines classes Book, EBook, PrintBook (Inheritance)
and Library (Composition) to model a library system.
"""

# --- Base Class: Book (Demonstrates Base Functionality) ---
class Book:
    """Base class for all types of books."""
    def __init__(self, title: str, author: str):
        """Initializes the book with title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """Returns a string representation of the Book."""
        return f"Book: {self.title} by {self.author}"

# --- Derived Class: EBook (Demonstrates Inheritance) ---
class EBook(Book):
    """Represents an electronic book, inheriting from Book."""
    def __init__(self, title: str, author: str, file_size: int):
        """Initializes EBook, calling base class init and setting file size."""
        # Call the base class constructor
        super().__init__(title, author)
        self.file_size = file_size # Unique attribute

    def __str__(self):
        """Overrides the base class method to include EBook details."""
        # Use super().__str__() for the inherited part, or format manually
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

# --- Derived Class: PrintBook (Demonstrates Inheritance) ---
class PrintBook(Book):
    """Represents a physical printed book, inheriting from Book."""
    def __init__(self, title: str, author: str, page_count: int):
        """Initializes PrintBook, calling base class init and setting page count."""
        # Call the base class constructor
        super().__init__(title, author)
        self.page_count = page_count # Unique attribute

    def __str__(self):
        """Overrides the base class method to include PrintBook details."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

# --- Composition Class: Library (Demonstrates Composition) ---
class Library:
    """
    Manages a collection of Book objects (Composition).
    The Library 'has a' collection of Books.
    """
    def __init__(self):
        """Initializes the library with an empty list to store books."""
        # The 'books' attribute is a list containing instances of Book, EBook, or PrintBook.
        self.books = []
        # 

    def add_book(self, book: Book):
        """Adds a Book, EBook, or PrintBook instance to the library collection."""
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Error: Item is not a valid book type.")

    def list_books(self):
        """Prints the details of each book in the library using their __str__ method."""
        for book in self.books:
            # The polymorphism means book.__str__() calls the correct method 
            # (Book, EBook, or PrintBook) based on the object's actual type.
            print(book)

# End of library_system.py
