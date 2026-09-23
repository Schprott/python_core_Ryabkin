# Секретное число. Поиск секретного числа с подсказками больше - меньше.

secret = 37

for number in range(1,99999):
    user = int(input("Введите число: "))
    number = number + 1
    if user == secret:
         print("Вы угадали!")
         print(f"Количество попыток: {number - 1}")
         break
    elif user > secret:
        print("Вы ввели число больше секретного.")
    elif user < secret:
        print("Вы ввели число меньше секретного.")