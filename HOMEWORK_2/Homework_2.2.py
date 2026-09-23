# Проверка пароля. Программа на авторизацию.
Password = "Python123"

for number in range(3):
    user_login = input("Введите пароль: ")
    if user_login == Password:
        print("Успешная авторизация")
        break
    elif user_login != Password:
        print("Неправильный пароль, повторите попытку.")
else:
    print("Доступ заблокирован")