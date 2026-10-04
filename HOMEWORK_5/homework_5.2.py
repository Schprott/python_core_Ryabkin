import json
# Открываем файл и читаем его
try:
    with open("users.json") as file:
         users = json.load(file)

    # Перебираем всех пользователей в файле и выводим
    for user in users:
        print(user["login"], user["password"], user["expected_result"])
#  Выводим ошибку, если файл не найден
except FileNotFoundError as e:
    print(e)
#  Выводим ошибку, если файл нельзя прочитать
except json.JSONDecodeError as e:
    print(e)
# Выводим ошибку, если у пользователя отсутствует обязательное поле
except KeyError as e:
    print(e)