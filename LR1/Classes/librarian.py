class Librarian:
    def __init__(self, name):
        self.__name = None
        self.__can_issue = False
        self.set_name(name)

    def __validate_non_empty_string(self, value, field_name):
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{field_name} must be a non-empty string")

    def set_name(self, name):
        self.__validate_non_empty_string(name, "Name")
        self.__name = name.strip()

    def enable_issue(self):
        self.__can_issue = True

    def issue_book(self, book, reader):
        if self.__can_issue:
            return reader.take_book(book)
        return False

    def get_name(self):
        return self.__name