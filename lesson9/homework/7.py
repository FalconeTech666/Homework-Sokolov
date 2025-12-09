"""
Дан список пользователей след. формата: 
[{"name":"some_name", "login":"some_login", "password":"some_password" },
 ...
]

Отфильтровать используя функцию filter() список на предмет паролей 
которые менее 5 символов.

*Отфильтровать используя функцию filter() список на предмет валидных логинов. 
Валидный логин должен содержать только латинские буквы, цифры и черту подчеркивания. 
Каждому пользователю с плохим логином вывести текст 
"Уважаемый user_name, ваш логин user_login не является корректным."

"""
import re

users = [
    {"name": "John", "login": "john01", "password": "1234", "gender": "m"},
    {"name": "Anna", "login": "annarв88", "password": "qwerty", "gender": "f"},
    {"name": "Bob", "login": "bob77", "password": "pass", "gender": "m"},
]

filtered_users = filter(lambda x: len(x["password"]) < 5, users)

print(list(filtered_users))

valid_users = filter(lambda user: re.match(r"^[A-Za-z0-9_]+$", user["login"]), users)

for user in users:
    if not re.match(r"^[A-Za-z0-9_]+$", user["login"]):
        if user['gender'] == "m":
            greeting = "Уважаемый"
        else:
            greeting = "Уважаемая"
        print(f"{greeting} {user['name']}, ваш логин {user['login']} не является корректным.")