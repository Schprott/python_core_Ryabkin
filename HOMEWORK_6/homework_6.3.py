
def log_test(test):
    def wrapper(*args, **kwargs):
        print("Запуск авторизации")
        result = test()
        print("Конец авторизации")
        print(result)
        return result
    return wrapper

@log_test
def login_test():
    return "Авторизация прошла успешно"

login_test()