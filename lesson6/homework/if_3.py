'''
Запросить 3 числа. Вывести наибольшее  из них. Решить используя if.
'''

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

largest = a  

if b > largest:
    largest = b

if c > largest:
    largest = c

print("Наибольшее число:", largest)