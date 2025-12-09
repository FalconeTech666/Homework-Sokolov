'''
Дан список содержащий в себе различные типы данных, отфильтровать таким
образом, чтобы 
 - остались только строки.
 - остался только логический тип.
 
'''

data = [1, "hello", True, 3.14, "python", False, 10]

data_filtered_str = filter(lambda x: isinstance(x, str), data)
data_filtered_bool = filter(lambda x: isinstance(x, bool), data)

print(list(data_filtered_str))
print(list(data_filtered_bool))
