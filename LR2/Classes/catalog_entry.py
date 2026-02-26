class CatalogEntry:
    def __init__(self, book, shelf):
        self.__book = book
        self.__shelf = shelf

    def get_location(self):
        return f"Книга '{self.__book.get_title()}' на полке {self.__shelf}"