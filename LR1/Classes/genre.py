class Genre:
    def __init__(self, name):
        self.__name = None
        self.set_name(name)

    def __validate_non_empty_string(self, value, field_name):
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{field_name} must be a non-empty string")

    def set_name(self, name):
        self.__validate_non_empty_string(name, "Genre name")
        self.__name = name.strip()

    def get_name(self):
        return self.__name