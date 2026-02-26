class LibraryBranch:
    def __init__(self, name):
        self.__name = name
        self.__books = []

    def add_book(self, book):
        self.__books.append(book)

    def get_name(self):
        return self.__name

    def get_books_count(self):
        return len(self.__books)