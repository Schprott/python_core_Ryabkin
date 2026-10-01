import random

tests = [
"test_login",
"test_logout",
"test_registration",
"test_profile",
"test_payment",
"test_search"
]
# Пользователь вводит число тестов
quantity_tests = int(input("Введите количество тестов для запуска:"))
# Все возможные результаты тестов
status = ["PASS", "FAIL", "SKIP"]

def print_report(tests):
    # При вводе числа больше чем количество доступных тестов, выводим ошибку
    if quantity_tests > len(tests):
        print("Количество тестов превышает допустимую норму")
    else:
        # Выбираем рандомные элементы из списка, в количестве указанном пользователем
        result = random.sample(tests, quantity_tests)
        for x in result:
            # Выбираем случайный статус к выбранным элементам из списка
            statuses = random.choice(status)
            print(x, "-", statuses)
# Вызываем функцию
print_report(tests)
