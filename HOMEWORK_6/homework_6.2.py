max_time = 15
# Создаём функцию с замыканием
def create_time_checker(max_time):
    def inner(x):
        if x > max_time:
            print("Превышен установленный лимит!")
        else:
            print("Установленный лимит не превышен!")
    return inner
# Первое замыкание
actual_time = create_time_checker(max_time)
# Второе независимое замыкание
current_time = create_time_checker(20)

actual_time(7)
current_time(27)

