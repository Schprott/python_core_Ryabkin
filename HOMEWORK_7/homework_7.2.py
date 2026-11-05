# Создаём класс описывающий работу банкомата
class ATM:
    def __init__(self, banknote_20, banknote_50, banknote_100):
        self.banknote_20 = banknote_20
        self.banknote_50 = banknote_50
        self.banknote_100 = banknote_100

    # Функция для загрузки купюр
    def add_money(self, amount_20, amount_50, amount_100):
        self.banknote_20 += amount_20
        self.banknote_50 += amount_50
        self.banknote_100 += amount_100
    # Функция для снятия купюр
    def withdraw(self, amount):
        for amount_100 in range(self.banknote_100, -1, -1):
            for amount_50 in range(self.banknote_50, -1, -1):
                for amount_20 in range(self.banknote_20, -1, -1):

                    # Проверяем общую сумму
                    if (amount_100 * 100 + amount_50 * 50
                            + amount_20 * 20 == amount):
                        # Уменьшаем количество купюр
                        self.banknote_100 -= amount_100
                        self.banknote_50 -= amount_50
                        self.banknote_20 -= amount_20

                        print("Купюр по 100:", amount_100)
                        print("Купюр по 50:", amount_50)
                        print("Купюр по 20:", amount_20)

                        return True

        return False


atm = ATM(10, 5, 4)
atm.add_money(2, 3, 1)

print(atm.withdraw(180))
print(atm.withdraw(320))
print(atm.withdraw(70))
