#  Есть два списка для тестов

test_cases = ["Login", "Registration", "Checkout", "Logout"]
statuses = ["PASS", "FAIL", "PASS", "SKIP"]

# Функция принимает списки и выводит отчёт
def print_report(test_cases, statuses):
# Создаём счётчик
    result_pass = 0
    result_fail = 0
    result_skip = 0
# Начинаем перебор значений соеденённых методом zip
    for test, result in zip(test_cases, statuses):
        print(test, "-", result)
        if result == "PASS":
            result_pass += 1
        if result == "FAIL":
            result_fail += 1
        if result == "SKIP":
            result_skip += 1
# Проверяем весь прогон на наличие упавших тестов
    if result_fail > 0:
        print("!!!Запуск неуспешный!!!")
    else:
        print("!!!Запуск успешный!!!")
# Выводим значение функции НАРУЖУ (за функцию, чтобы можно было использовать вне функции)
    return result_pass, result_fail
# Кладём из функции получившиеся значения в переменные (test_cases = result_pass, statuses = result_fail)
result_pass, result_fail = print_report(test_cases, statuses)

print("Успешных запусков:", result_pass)
print("Неуспешных запусков:", result_fail)