from functools import reduce
import json

try:
    # Открываем JSON файл
    with open("test.json") as file:
        tests = json.load(file)

    # Проверяем наличие элементов в файле
    for test in tests:
        if "name" in test and "status" in test and "time" in test:
            print(test["name"], test["status"], test["time"])
        else:
            # Не найден элемент для тестирования
            raise KeyError(f"Выбранный тест {test} - не найден!")

except FileNotFoundError as e:  # Файл отсутствует
    print(e)
    raise SystemExit # Завершает выполнение программы
except json.JSONDecodeError as e:  # JSON невозможно распарсить
    print(e)
    raise SystemExit
except KeyError as e:  # Некорректный тест
    print(e)
    raise SystemExit

total_tests = len(tests)
# Поиск тестов по статусам
passed_tests = list(filter(lambda test: test["status"] == "PASS", tests))
failed_tests = list(filter(lambda test: test["status"] == "FAIL", tests))
skipped_tests = list(filter(lambda test: test["status"] == "SKIP", tests))
# Количество тестов по статусам
passed_result = len(passed_tests)
failed_result = len(failed_tests)
skipped_result = len(skipped_tests)
# Названия упавших тестов
failed_name = [test["name"] for test in tests if test["status"] == "FAIL"]
# Максимальное время теста
max_time = max(tests, key=lambda test: test["time"])
# Общее время теста
total_time = reduce(
    lambda total, test: total + test["time"],
    tests,
    0
)
# Отчёт по тестам
report = {
    "total_tests": total_tests,
    "passed": passed_result,
    "failed": failed_result,
    "skipped": skipped_result,
    "fail_name_tests": failed_name,
    "max_time_tests": {
        "name": max_time["name"],
        "time": max_time["time"]
    },
    "total_time_tests": total_time
}
# Созданеие файла с отчетом
with open("report.json", "w") as file:
    json.dump(report, file)