"""
Написать декоратор который позволит не останавливать программу 
в случае если любая декорируемая функция выбрасывает ошибку, 
а выводить имя функции в которой произошла ошибка и информацию об ошибке в. 
Имя функции можно узнать использовав свойство __name__ ( print(func.__name__))

* сделать настраиваемы параметр который определяет печать в консоль или в файл
и если в файл передать название фала
"""

# def call_funkc(func):
#     def wrapper(*args, **kwargs):
#         try:
#             return func(*args,**kwargs)
#         except Exception as error:
#             print(func.__name__)
#             print(error)
#     return wrapper


def call_funkc(mode="console", filename=None):
    def dekorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args,**kwargs)
            except Exception as error:
                message = f"Ошибка в функции {func.__name__}: {error}"
                if mode == "console":
                    print(message)
                elif mode == "file":
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(message + "\n")

        return wrapper
    
    return dekorator