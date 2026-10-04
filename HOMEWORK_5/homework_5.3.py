# Создаём функцию с количество тестов и таймаутом
def tests(retries, timeout):
    # Создаём ошибки на некорректные тесты
    if retries < 0 or retries > 5:
        raise ValueError("Количество повторных тестов должно быть от 0 до 5")
    if timeout <= 0:
        raise ValueError("Таймаут должен быть положительным числом")

autotests = [
    {"retries": 3, "timeout": 3}, #Успешный тест
    {"retries": 4, "timeout": 0}, #Неуспешный тест из-за таймаута
    {"retries": 6, "timeout": 3.5} #Неуспешный тест из-за количества повторений
]
# Перебираем значения в списке
for test in autotests:
    try:
        retries = test["retries"]
        timeout = test["timeout"]
        tests(retries, timeout)

    except ValueError as e:
        print(e)
    else:
        print("Тест прошел успешно!")