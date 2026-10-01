import test_data

# Пользователь вводит сколько нужно создать пользователей
quantity_users = int(input("Введите количество пользователей для создания:"))
# Пустая строка для будущих пользователей
users = []
# Создание пользователей по заданному количеству + добавление в конец списка users
for create_users in range(quantity_users):
    user = test_data.generate_user()
    users.append(user)

# Счетчик для статусов пользователей
status_active = 0
status_inactive = 0
status_blocked = 0

for x in users:
    print(x)
    if x["status"] == "ACTIVE":
        status_active += 1
    if x["status"] == "INACTIVE":
        status_inactive += 1
    if x["status"] == "BLOCKED":
        status_blocked += 1

print("Статус ACTIVE:", status_active)
print("Статус INACTIVE:", status_inactive)
print("Статус BLOCKED:", status_blocked)
