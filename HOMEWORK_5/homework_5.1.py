from functools import reduce
# Создаем список со словарями, где лежат результаты тестов
autotests = [
    {"name": "login", "status": "PASS", "time": 0.9},
    {"name": "password", "status": "FAIL", "time": 1.5},
    {"name": "email", "status": "SKIP", "time": 0.5},
    {"name": "age", "status": "PASS", "time": 1.9},
    {"name": "registration", "status": "FAIL", "time": 1.2},
    {"name": "phone", "status": "SKIP", "time": 0.3}
]
# Фильтруем упавшие тесты и сохраняем в список
failed_tests = list(filter(lambda x: x["status"] == "FAIL", autotests))
# Собираем названия упавших тестов
failed_name = list(map( lambda x: x["name"], failed_tests))
# Получаем общее время всех тестов и сохраняем в переменную
result = reduce(lambda x, y: x + y["time"], autotests, 0)
# Считаем количество успешных тестов
passed_tests =  [tests["name"] for tests in autotests if tests["status"] == "PASS"]
# Счетчик по статусам тестов
pass_tests = 0
fail_tests = 0
skip_tests = 0

for test in autotests:
    if test["status"] == "PASS":
        pass_tests += 1
    elif test["status"] == "FAIL":
        fail_tests += 1
    else:
        skip_tests += 1

print("Количество успешных тестов:",pass_tests)
print("Количество упавших тестов:",fail_tests)
print("Количество пропущенных тестов:",skip_tests)
print("Название успешных тестов:", passed_tests)
print("Название упавших тестов:", failed_name)
print("Общее время тестов:", result)
