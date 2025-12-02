'''
*
Написать рекурсивную функцию, которая принимает список 
и печатает каждых элемент на новой строке. 
Если элемент списка - список, то его элементы должны выводиться 
с отступом относительно родительского на 2 символа. 
Символ для отступа передать дополнительными необязательным параметром.

** написать такую же функцию но без рекурсии

Пример1: some_list = [1, 2, 3, [4, [5, 6], 7], 8, 9]
1
2
3
--4
----5
----6
--7
8
9

Пример2: some_list=[1,[2,[[3],4]],5,[[[6,7]]],8,[[[[9,10]],11]],12]
1
--2
------3
----4
5
------6
------7
8
--------9
--------10
----11
12

'''

# Рекурсивная функция

def print_nested(lst, indent=0, symbol="--"):
    for element in lst:
        if isinstance(element, list):
            print_nested(element, indent+1, symbol)
        else:
            print(symbol * indent + str(element))

print_nested([1, 2, 3, [4, [5, 6], 7], 8, 9])

# Функция без рекурсии

def print_nested_iter(lst, symbol="--"):
    stack = [(lst, 0)]
    while stack:
        element, indent = stack.pop()
        if isinstance(element, list):
            for child in reversed(element):
                stack.append((child, indent + 1))
        else:
           print(symbol * indent + str(element))
print_nested_iter([1,[2,[[3],4]],5,[[[6,7]]],8,[[[[9,10]],11]],12])