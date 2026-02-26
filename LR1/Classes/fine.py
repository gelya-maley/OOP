class Fine:
    def __init__(self, amount):
        self.__amount = None
        self.__paid = False
        self.set_amount(amount)

    def __validate_amount(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number")
        if amount < 0:
            raise ValueError("Amount cannot be negative")

    def set_amount(self, amount):
        self.__validate_amount(amount)
        self.__amount = amount

    def pay(self):
        if not self.__paid:
            self.__paid = True
            return True
        return False

    def get_info(self):
        status = "Оплачен" if self.__paid else "Не оплачен"
        return f"Штраф: {self.__amount} руб. ({status})"