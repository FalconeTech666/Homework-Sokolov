"""
Написать функцию print_n() которая будет печатать переданный текст, 
но при этом перед этим текстом выводить строку с номером отражающим 
какой раз по счету выполняется эта функция. 

"""
counter = 0

def print_n(text:str):
    global counter
    counter = counter+1
    print(counter, text)

print_n('Привет!')
print_n('Привет!')
print_n('Привет!')