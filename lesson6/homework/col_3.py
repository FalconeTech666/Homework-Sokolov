"""
дан словарь
d = {'one':11, 'two':22, 'hello':'python', True:False}
запросить номер элемента и удалить его из словаря с помощью del.

"""
d = {'one':11, 'two':22, 'hello':'python', True:False}

lst = list(d.keys()) # только ключи словаря сделать списком 
print("0:", lst[0])
print("1:", lst[1])
print("2:", lst[2])
print("3:", lst[3])

num = int(input("Введите номер элемента для удаления: "))
element = lst[num]

del d[element]

print(d)

