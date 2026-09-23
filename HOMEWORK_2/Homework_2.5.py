# Результаты автотестов. Статистика пройденных автотестов.

countity = 10
status_pass = 0
status_fail = 0
status_skip = 0

for status in range(countity):
    status = input("Результат теста: ")
    if status == "PASS":
        status_pass += 1
    elif status == "FAIL":
        status_fail += 1
    elif status == "SKIP":
        status_skip += 1
    print("PASS: ", status_pass)
    print("FAIL: ", status_fail)
    print("SKIP: ", status_skip)

print("Количество запущенных тестов: ", countity)
if status_fail > 0:
    print("Есть упавшие автотесты.")
else:
    print("Упавшие автотесты отсутствуют.")
