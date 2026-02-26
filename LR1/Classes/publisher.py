class Publisher:
    def __init__(self, name, country):
        self.__name = None
        self.__country = None
        self.set_name(name)
        self.set_country(country)

    def __validate_non_empty_string(self, value, field_name):
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{field_name} must be a non-empty string")

    def set_name(self, name):
        self.__validate_non_empty_string(name, "Publisher name")
        self.__name = name.strip()

    def set_country(self, country):
        self.__validate_non_empty_string(country, "Country")
        self.__country = country.strip()

    def get_info(self):
        return f"{self.__name} ({self.__country})"