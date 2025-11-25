'''

Дан списк:
['qwertyu','asdfggh','zxcvbnm','yuiop[]','hjklasd','mnbvnbv']
Для каждого элемента в списке 
    - вывести на экран сначала номер элемента 
    - сам элемент 
    - символ данного элемента, соответствующий номеру его позиции в списке. 
Образец:
1 - qwertyu - q
2 - asdfggh - s
3 - zxcvbnm - c
и так далее...


'''
lst = ['qwertyu','asdfggh','zxcvbnm','yuiop[]','hjklasd','mnbvnbv']

for number, word in enumerate(lst, start =1):
    letter = word[number - 1]
    print(f"{number} - {word} - {letter}")