class Reader:
    def __init__(self, name):
        self.__name = None
        self.__books = []
        self.set_name(name)

    def __validate_non_empty_string(self, value, field_name):
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{field_name} must be a non-empty string")

    def set_name(self, name):
        self.__validate_non_empty_string(name, "Name")
        self.__name = name.strip()

    def take_book(self, book):
        from Classes.book import Book
        if not isinstance(book, Book):
            raise TypeError("Can only take Book instances")
        if book.borrow():
            self.__books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self.__books:
            book.return_book()
            self.__books.remove(book)
            return True
        return False

    def get_name(self):
        return self.__name

    def get_books_count(self):
        return len(self.__books)