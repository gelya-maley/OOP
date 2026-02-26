from datetime import datetime


class Loan:
    def __init__(self, book, reader):
        self.__book = book
        self.__reader = reader
        self.__date = datetime.now()
        self.__is_returned = False

    def mark_returned(self):
        self.__is_returned = True

    def get_status(self):
        if self.__is_returned:
            return "Возвращена"
        return "Активна"

    def get_summary(self):
        return f"Выдача: {self.__book.get_title()} -> {self.__reader.get_name()}"