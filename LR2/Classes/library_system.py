class LibrarySystem:
    def __init__(self, branch):
        self.__branch = branch
        self.__loans = []
        self.__reservations = []
        self.__librarians = []

    def add_loan(self, loan):
        self.__loans.append(loan)

    def add_reservation(self, reservation):
        self.__reservations.append(reservation)

    def add_librarian(self, librarian):
        self.__librarians.append(librarian)

    def get_summary(self):
        return f"Филиал: {self.__branch.get_name()}, Выдач: {len(self.__loans)}"