class LibraryBranch:
    def __init__(self, name):
        self.__name = None
        self.__books = []
        self.set_name(name)

    def __validate_non_empty_string(self, value, field_name):
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{field_name} must be a non-empty string")

    def set_name(self, name):
        self.__validate_non_empty_string(name, "Branch name")
        self.__name = name.strip()

    def add_book(self, book):
        self.__books.append(book)

    def get_name(self):
        return self.__name

    def get_books_count(self):
        return len(self.__books)