'''
Запросить любое число. Заменить каждую цифру этого числа буквой, 
у которой номер в алфавите равен этой цифре. 
Алфавит считаем от 0. a-0, b-1, c-3 и т.д.
Например: 13520 -> bdfca.
'''

az = "abcdefghijklmnopqrstuvwxyz"

number = input("Введите любое число: ")
cod_e = []

for i in number:
    index = int(i)
    cod_e += az[index]

print("".join(cod_e))




