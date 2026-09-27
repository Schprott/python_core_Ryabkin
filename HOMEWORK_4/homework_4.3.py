# Открываем файл с дробными числами
with open("float_numbers.txt", 'r') as file:
    new_float_numbers = file.read()
    chunks = new_float_numbers.split()
# Создаём переменную для записи изменённых чисел
float_numbers = []
for x in chunks:
    chunks_float_number = float(x)
    # Возводим в квадрат и записываем в переменную каждое новое число в конец
    float_numbers.append(pow(chunks_float_number, 2))
# Открываем и перезаписываем исходные числа на возведенные в квадрат
with open('float_numbers.txt', 'w') as file:
    file.write(str(float_numbers))
# Не понял, надо ли переводить новые файлы в числа, и если надо то как...

