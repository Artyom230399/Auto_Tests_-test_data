################################################################################################

print("\n \n Пример 1:")

with open("ex1.txt", "r", encoding="utf-8") as file:  # Менеджер контекста сам закроет файл
    print(file.read())

################################################################################################

print("\n \n Пример 2:")

with open("ex2.txt", "w", encoding="utf-8") as file:
    for n in range(1, 101):
        file.write(str(n) + "\n")

################################################################################################

print("\n \n Пример 3:")

# Пишем в .json
import json

data = {
    "users": [
        {"login": "Alisa", "email": "alisa@mail.ru"},
        {"login": "Artyom", "email": "dan.1000@mail.ru"},
        {"login": "Katharina", "email": "yazceva199819@mail.ru"}
    ]
}
with open("ex3.json", "w") as f:
    json.dump(data, f, indent=4)

################################################################################################

print("\n \n Пример 4:")

# Читаем .json

import json

with open("ex3.json", "r") as f:
    users = json.load(f)

for user in users['users']:
    print(user)

################################################################################################