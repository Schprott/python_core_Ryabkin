# Создаём класс
class CreditCard():
    def __init__(self, number, Balance):
        self.number = number
        self.__Balance = Balance
    # Создаём Метод действия (сложение)
    def deposit(self, amount):
        self.__Balance = self.__Balance + amount
        print(f'Баланс пополнен на сумму: {amount} рублей.')
    # Создаём Метод действия (вычитание)
    def withdraw(self, amount):
        self.__Balance = self.__Balance - amount
        if self.__Balance < 0:
            raise ValueError(f'Баланс не может быть отрицательным!')
        else:
            print(f'Баланс уменьшен на сумму: {amount} рублей.')
    # Создаём Метод действия (выгрузка данных по карте)
    def show_info(self):
        print(f'Номер счёта: {self.number}\nТекущий баланс: {self.__Balance} ')
# Создаём переменные(объекты) класса
CardNumber_1 = CreditCard(77777777, 500)
CardNumber_2 = CreditCard(88888888, 1000)
CardNumber_3 = CreditCard(99999999, 2000)
# Запускаем расчёты
CardNumber_1.deposit(300)
CardNumber_2.deposit(900)
CardNumber_3.withdraw(1400)

CardNumber_1.show_info()
CardNumber_2.show_info()
CardNumber_3.show_info()
