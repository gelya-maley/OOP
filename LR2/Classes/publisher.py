class Publisher:
    def __init__(self, name, country):
        self.__name = name
        self.__country = country

    def get_info(self):
        return f"{self.__name} ({self.__country})"