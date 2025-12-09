"""
Написать функцию dict_from_args, которая принимает неограниченное
количество позиционных аргументов и неограниченное количество аргументов
ключевых-слов.

Если все позиционные аргументы - целые числа, то рассчитать их сумму. Если
нет, то кинуть ошибку TypeError("Все позиционные аргументы должны быть целыми").

Если все именованные аргументы - ключевые слова являются строками, то найти максимальную
длину слова. Если нет, то кинуть ошибку TypeError("Все аргументы - ключевые
слова должны быть строками").

Функция должна вернуть словарь, вида:
{
    "args_sum": 13,
    "kwargs_max_len": 7
}
"""
def dict_from_args(*args, **kwargs):
    if all(isinstance(key, str) for key in kwargs.keys()):
        kwargs_max_len = max(len(k) for k in kwargs.keys())
    else:
        raise TypeError("Все аргументы - ключевые слова должны быть строками")
    
    if all(isinstance(x, int) for x in args):
        args_sum = sum(args)
    else:
        raise TypeError("Все позиционные аргументы должны быть целыми")
    return {
        "args_sum": args_sum,
        "kwargs_max_len": kwargs_max_len
    }

dict_from_args