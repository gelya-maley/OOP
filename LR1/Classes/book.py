class Book:
    def __init__(self, title, author, year):
        self.__title = None
        self.__author = None
        self.__year = None
        self.__is_available = True
        self.__genre = None
        self.__publisher = None
        
        self.set_title(title)
        self.set_author(author)
        self.set_year(year)

    def __validate_non_empty_string(self, value, field_name):
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{field_name} must be a non-empty string")

    def __validate_year(self, year):
        if not isinstance(year, int) or year < 1000 or year > 2100:
            raise ValueError(f"Year {year} is invalid")

    def __mark_as_unavailable(self):
        self.__is_available = False

    def __mark_as_available(self):
        self.__is_available = True

    def set_title(self, title):
        self.__validate_non_empty_string(title, "Title")
        self.__title = title.strip()

    def set_author(self, author):
        self.__validate_non_empty_string(author, "Author")
        self.__author = author.strip()

    def set_year(self, year):
        self.__validate_year(year)
        self.__year = year

    def set_genre(self, genre):
        from Classes.genre import Genre
        if genre is not None and not isinstance(genre, Genre):
            raise TypeError("Genre must be a Genre instance or None")
        self.__genre = genre

    def set_publisher(self, publisher):
        from Classes.publisher import Publisher
        if publisher is not None and not isinstance(publisher, Publisher):
            raise TypeError("Publisher must be a Publisher instance or None")
        self.__publisher = publisher

    def borrow(self):
        if self.__is_available:
            self.__mark_as_unavailable()
            return True
        return False

    def return_book(self):
        self.__mark_as_available()

    def get_title(self):
        return self.__title

    def is_available(self):
        return self.__is_available

    def get_info(self):
        return f"{self.__title} ({self.__year})"