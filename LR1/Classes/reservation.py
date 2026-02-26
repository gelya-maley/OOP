class Reservation:
    def __init__(self, book, reader):
        self.__book = book
        self.__reader = reader
        self.__active = True

    def cancel(self):
        self.__active = False

    def get_status(self):
        return "Активна" if self.__active else "Отменена"

    def get_info(self):
        return f"Бронь: {self.__book.get_title()} для {self.__reader.get_name()}"