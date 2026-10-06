# Создаём декоратор
def retry(count):
    def inner(func):
        def wrapper(*args, **kwargs):
            for x in range(count):
                print(f'Попытка: {x + 1}')
                result = func(*args, **kwargs)
                if result == True:
                    print(f'Запуск закончен из за успешного результата - "TRUE".')
                    break # Останавливаем запуск при ответе True
            else:
                print(f'Запуск завершён из за ограничений по количеству прогонов. Результат - "FALSE"')
            return result
        return wrapper
    return inner

# Создаём счетчик количества запусков
count_test = [0]

# Запускаем декоратор с функцией
@retry(3)
def test():
    if count_test[0] == 2:
        return True
    else:
        count_test[0] += 1
        return False

test()

