from functools import wraps
# Создаём декоратор
def log_test(test):
    @wraps(test)
    def wrapper(*args, **kwargs):
        print(f"Запуск теста: {test.__name__}")
        result = test(*args, **kwargs)
        print(f"Тест завершён: {test.__name__}")
        print(f"Результат: {result}")
        return result

    return wrapper
# Запускаем декоратор с функцией
@log_test
def login_test():
    return "Авторизация прошла успешно"

login_test()