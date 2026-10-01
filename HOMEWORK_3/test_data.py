import random


# Генерируем логин пользователя
def generate_login():
    login = random.randint(100000, 999999)
    return login
user_login = generate_login()

# Генерируем возраст пользователя
def generate_age():
    age = random.randint(18, 80)
    return age
user_age = generate_age()

# Генерируем статус пользователя
def generate_status():
    status = ["ACTIVE", "INACTIVE", "BLOCKED"]
    result = random.choice(status)
    return result
user_status = generate_status()

# Генерируем пользователя
def generate_user():
    login = generate_login()
    age = generate_age()
    status = generate_status()
    full_info = {"login": login,
                 "age": age,
                 "status": status}
    return full_info
full_user = generate_user()
