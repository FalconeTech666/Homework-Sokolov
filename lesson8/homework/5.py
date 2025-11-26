'''
Написать функцию count_char, которая принимает строковое значение,
из которого создает и возвращает словарь, следующего вида:
{'буква': 'количество-вхождений-в-строку'}
Нельзя пользоваться collections.Counter!

'''
def count_char(text):
    result = {}                    

    for char in text:              # в цикле делаю логику - если буква впервые в списке - то вход 1, если нет, то вход +1
        if char in result:         
            result[char] += 1      
        else:                      
            result[char] = 1       

    return result  

print(count_char("привет"))