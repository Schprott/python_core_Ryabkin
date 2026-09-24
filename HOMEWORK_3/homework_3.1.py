#Пользователь написал строку с результатами
status = "PASS FAIL PASS SKIP PASS FAIL"
#Переводим строку в список
status_2 = status.split()

#Создаём функцию с подсчётами
def get_test_statistics(results):
    status_pass = 0 #счётчики статусов
    status_fail = 0
    status_skip = 0
#Перебор каждого статуса из списка status_2
    for x in status_2:
        if x == "PASS":
            status_pass += 1
        elif x == "FAIL":
            status_fail += 1
        elif x == "SKIP":
            status_skip += 1
#Выводим результат счётчика в словарь
    results = {"PASS": status_pass,
               "FAIL": status_fail,
               "SKIP": status_skip}
#Закрыть функцию
    return results
#Словарь записываем в переменную
name = get_test_statistics(status_2)

print("Всего тестов:", len(status_2))
print("PASS:", name["PASS"])
print("FAIL:", name["FAIL"])
print("SKIP:", name["SKIP"])

success = name["PASS"] / len(status_2) * 100
print(success,"%")

