# Читаем первый файл и сохраняем в переменную
with open("random_file_1.txt") as file:
    random_file_1 = file.read()
# Читаем второй файл и сохраняем в переменную
with open("random_file_2.txt") as file:
    random_file_2 = file.read()
# Перезаписываем первый файл данными из переменной
with open("random_file_1.txt", "w") as file:
    file.write(random_file_2)
# Перезаписываем второй файл данными из переменной
with open('random_file_2.txt', "w") as file:
    file.write(random_file_1)