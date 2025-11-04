'''
Программа должна запросить несколько цифр через пробел 
    - выдать их общую сумму
    - выдать максимальную цифру
    - выдать среднее арифметическое

'''
integer = input("Введите несколько цифр через пробел:").split()
integer = list(map(int, integer))
print(sum(integer))
print(max(integer))
print(sum(integer)/len(integer))