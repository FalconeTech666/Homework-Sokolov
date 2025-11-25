'''
Запросить высоту елочки - число от 3 до 20. 
Напечатать на экране елочку где ее высота равна числу строк. 
Пример елочки из 4 строк:
   *
  ***
 *****
*******

* - елочка со снегом
'''

# Простая елочка
height = int(input("Введите высоту елочки от 3 до 20: "))

if 3 <= height <= 20:                            # выставляю диапазон
    for i in range(1, height + 1):
        stars = "*" * (2*i - 1)                  # количество звездочек
        spaces = " " * (height - i)              # пробелы слева
        print(spaces + stars)                    # печать строки ёлки
else:
    print("Ошибка! Введите высоту от 3 до 20") 


# Елочка со снегом
height = int(input("Введите высоту елочки от 3 до 20: "))

if 3 <= height <= 20:

    for i in range(1, height + 1):
        stars = "*" * (2*i - 1)                        # звезды (ветки ёлки)
        spaces = " " * (height - i)                    # пробелы слева
        snow_left = "." * (height - i)                 # снег слева
        snow_right = "." * (height - i)                # снег справа

        print(snow_left + spaces + stars + snow_right) # собрал все

else:
    print("Ошибка! Введите высоту от 3 до 20")

# Елочка со снегом и ножкой

height = int(input("Введите высоту елочки от 3 до 20: "))

if 3 <= height <= 20:

    for i in range(1, height + 1):
        width = 2*i - 1                        # ширина ветки
        spaces = " " * (height - i)            # отступ слева

        line = ""

        for pos in range(width):
            if pos == 0 or pos == width - 1:
                line += "."                    # снег по краям
            elif pos % 2 == 1:
                line += "*"                    # звездочки
            else:
                line += "."                    # снег внутри
        print(spaces + line)

    # ножка для елки
    trunk_width = 3                             # ширина ножки
    trunk_spaces = " " * (height - 2)           # чтобы ножка была по центру

    for _ in range(2):                          # высота ножки (2 строки)
        print(trunk_spaces + "***")             # ножка из трёх звёздочек

else:
    print("Ошибка! Введите число от 3 до 20")