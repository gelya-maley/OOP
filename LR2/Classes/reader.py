class Reader:
    def __init__(self, name):
        self.__name = name
        self.__books = []

    def take_book(self, book):
        if len(self.__books) < self.get_books_limit() and book.borrow():
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
    
    def get_books_limit(self):
        return 3


class Student(Reader):
    def get_books_limit(self):
        return 5


class Teacher(Reader):
    def get_books_limit(self):
        return 10