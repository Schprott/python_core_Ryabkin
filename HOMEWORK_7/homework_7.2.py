
# НЕ ЗНАЮ КАК ДАЛЬШЕ


class ATM:
    def __init__(self, banknote_20, banknote_50, banknote_100):
        self.banknote_20 = banknote_20
        self.banknote_50 = banknote_50
        self.banknote_100 = banknote_100

    def add_money(self, amount_20, amount_50, amount_100):
        self.banknote_20 += amount_20
        self.banknote_50 += amount_50
        self.banknote_100 += amount_100

    def withdraw(self, amount):
