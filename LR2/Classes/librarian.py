class Librarian:
    def __init__(self, name):
        self.__name = name
        self.__can_issue = False

    def enable_issue(self):
        self.__can_issue = True

    def issue_book(self, book, reader):
        if self.__can_issue:
            return reader.take_book(book)
        return False

    def get_name(self):
        return self.__name