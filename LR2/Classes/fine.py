class Fine:
    def __init__(self, amount):
        self.__amount = amount
        self.__paid = False

    def pay(self):
        self.__paid = True

    def get_info(self):
        status = "Оплачен" if self.__paid else "Не оплачен"
        return f"Штраф: {self.__amount} руб. ({status})"
    
    def calculate(self, days=None):
        if days is None:
            return self.__amount
        return self.__amount * days

    def add_extra(self, extra):
        return self.__amount + float(extra)
    
    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Fine(self.__amount + other)
        elif isinstance(other, Fine):
            return Fine(self.__amount + other.__amount)
        return NotImplemented

    @property
    def amount(self):
        return self.__amount

    def __str__(self):
        return f"{self.__amount} руб."