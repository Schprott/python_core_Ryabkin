result = ["PASS", "FAIL", "SKIP", "PASS", "FAIL", "SKIP", "PASS"]

# Создаём функцию с рекурсией
def passed(n):
    # Если функция прошлась по всем элементам, заканчиваем рекурсию
    if n == len(result):
        return 0
    else:
        # При нахождении статуса PASS прибавляем в счётчик + 1 и продолжаем рекурсию
        if result[n] == "PASS":
            return passed(n + 1) + 1
        # При отсутствии статуса PASS, просто продолжаем рекурсию
        if result[n] != "PASS":
            return passed(n + 1)
# Сохраняем функцию в переменную, и указываем индекс откуда начинать функцию
passed_count = passed(0)
print(passed_count)