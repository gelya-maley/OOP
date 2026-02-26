class Book:
    def __init__(self, title, author, year):
        self.__title = title
        self.__author = author
        self.__year = year
        self.__is_available = True
        self.__genre = None
        self.__publisher = None

    def set_genre(self, genre):
        self.__genre = genre

    def set_publisher(self, publisher):
        self.__publisher = publisher

    def borrow(self):
        if self.__is_available:
            self.__is_available = False
            return True
        return False

    def return_book(self):
        self.__is_available = True

    def get_title(self):
        return self.__title

    def is_available(self):
        return self.__is_available

    def get_info(self):
        return f"{self.__title} ({self.__year})"
    
    
class PrintedBook(Book):
    def __init__(self, title, author, year, pages):
        super().__init__(title, author, year)
        self.__pages = pages

    def get_info(self):  
        return f"Печатная книга: {self.get_title()}, {self.__pages} стр."


class EBook(Book):
    def __init__(self, title, author, year, file_size):
        super().__init__(title, author, year)
        self.__file_size = file_size

    def get_info(self):
        return f"Электронная книга: {self.get_title()}, {self.__file_size} MB"