#  Запуск тестов для пользователей. Перебор чисел с пропусками и вынужденной остановкой.

for user in range(1,21):
    if user == 5:
        continue
    if user == 10:
        continue
    if user == 15:
         continue
    print(user)
    if user == 18:
          break