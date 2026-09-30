def tests(retries, timeout):

    if retries < 0 or retries > 5:
        raise ValueError("Количество повторных тестов должно быть от 0 до 5")
    if timeout <= 0:
        raise ValueError("Таймаут должен быть положительным числом")

autotests = [
    {"retries": 3, "timeout": 3}, #Успешный тест
    {"retries": 4, "timeout": 0}, #Неуспешный тест из-за таймаута
    {"retries": 6, "timeout": 3.5} #Неуспешный тест из-за количества повторений
]

try:
    for test in autotests:
        retries = test["retries"]
        timeout = test["timeout"]
except ValueError as e:
    print(e)