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
        # Перебираем возможное количество купюр по 100
        for amount_100 in range(
            min(amount // 100, self.banknote_100), -1, -1
        ):
            remaining_100 = amount - amount_100 * 100

            # Перебираем возможное количество купюр по 50
            for amount_50 in range(
                min(remaining_100 // 50, self.banknote_50), -1, -1
            ):
                remaining_50 = remaining_100 - amount_50 * 50

                # Остаток должен полностью состоять из купюр по 20
                if remaining_50 % 20 == 0:
                    amount_20 = remaining_50 // 20

                    # Проверяем, хватает ли купюр по 20
                    if amount_20 <= self.banknote_20:
                        self.banknote_100 -= amount_100
                        self.banknote_50 -= amount_50
                        self.banknote_20 -= amount_20

                        print(f"100 рублей: {amount_100} шт.")
                        print(f"50 рублей: {amount_50} шт.")
                        print(f"20 рублей: {amount_20} шт.")

                        return True

        return False