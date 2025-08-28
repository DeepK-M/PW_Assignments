class LibraryBook:
    def __init__(self, book_name, author):
        # Encapsulated attributes (private)
        self.__book_name = book_name
        self.__author = author
        self.__is_available = True  # Initially available

    # Getter methods
    def get_book_name(self):
        return self.__book_name

    def get_author(self):
        return self.__author

    def is_available(self):
        return self.__is_available

    # Methods for borrowing book
    def borrow_book(self):
        if self.__is_available:
            self.__is_available = False
            print(f"'{self.__book_name}' has been borrowed.")
        else:
            print(f"'{self.__book_name}' is currently not available.")

    # Methods for returning book
    def return_book(self):
        if not self.__is_available:
            self.__is_available = True
            print(f"'{self.__book_name}' has been returned and is now available.")
        else:
            print(f"'{self.__book_name}' was not borrowed.")

    # Display book details
    def display_info(self):
        status = "Available" if self.__is_available else "Not Available"
        print(f"Book: {self.__book_name}, Author: {self.__author}, Status: {status}")


# ----------- Testing with sample data -----------

book1 = LibraryBook("The Alchemist", "Paulo Coelho")
book2 = LibraryBook("Python Programming", "John Zelle")

# Display initial info
book1.display_info()
book2.display_info()

# Borrowing books
book1.borrow_book()
book1.display_info()

# Trying to borrow the same book again
book1.borrow_book()

# Returning book
book1.return_book()
book1.display_info()

# Borrowing second book
book2.borrow_book()
book2.display_info()


# Sample output
# Book: The Alchemist, Author: Paulo Coelho, Status: Available
# Book: Python Programming, Author: John Zelle, Status: Available
# 'The Alchemist' has been borrowed.
# Book: The Alchemist, Author: Paulo Coelho, Status: Not Available
# 'The Alchemist' is currently not available.
# 'The Alchemist' has been returned and is now available.
# Book: The Alchemist, Author: Paulo Coelho, Status: Available
# 'Python Programming' has been borrowed.
# Book: Python Programming, Author: John Zelle, Status: Not Available