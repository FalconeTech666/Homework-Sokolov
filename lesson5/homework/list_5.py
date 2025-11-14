'''
Дан список
['samsung', 'lg', 'xerox', 'bosch']
Удалить элемент с именем 'xerox'
Добавить элемент на 2 место 'indesit'

'''

n = ['samsung', 'lg', 'xerox', 'bosch']

n.remove('xerox')       
n.insert(1, 'indesit')  

print(n)