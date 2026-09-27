# Открываем файл с целыми числами
with open("numbers.txt") as file:
    number = file.read()
result = number.split()
# Создаём переменные для четных и нечетных числе
plus_numbers = [] # Четные числа
minus_numbers = [] # Нечетные числа

for x in result:
    # Переводим str в int
    new_numbers = int(x)
    # Выявляем четные и нечетные
    if new_numbers % 2 == 0:
        plus_numbers.append(new_numbers)
    else:
        minus_numbers.append(new_numbers)
# Создаем два новых файла с четными и нечетными числами
with open("plus_numbers.txt","w") as file:
    file.write(str(plus_numbers))
with open("minus_numbers.txt","w") as file:
    file.write(str(minus_numbers))
# Не понял, надо ли переводить новые файлы в числа, и если надо то как...