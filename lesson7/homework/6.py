"""
1. Запросить у пользователей имя и отзыв о магазине. 
Программа должна запрашивать данные пока не введено слово "stop". 
Все данные сложить в словарь.
    -распечатать количество отзывов
    -распечатать отдельно имена пользователей
    -распечатать отдельно отзывы

"""
data = {}

while True:
    key = input("Введите ваше имя: ")
    if key == "stop":
        break

    value = input("Оставьте свой отзыв о магазине: ")
    if value == "stop":
        break

    data[key] = value      # автоматически добавляет пару key:value

from pprint import pprint

print("Имена пользователей:")
for name in data.keys():
    print("-", name)

print("\nКоличество отзывов:", len(data))

print("\nОтзывы:")
for review in data.values():
    print("-", review)