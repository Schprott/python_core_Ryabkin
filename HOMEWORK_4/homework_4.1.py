# Открыаем и читаем файл
with open("numbers.txt") as file:
    numbers = file.read()
result = numbers.split()

if len(result) < 3:
    print("Недопустимое количество чисел!")
else:
    print(result[0])
    print(result[1])
    print(result[-2])
    print(result[-1])
