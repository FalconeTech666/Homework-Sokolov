"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
а возвращает список из Yes или No для каждого элемента, 
Yes - если число уже встречалось и No, если нет
[1,2,3,1,4] => [no, no, no, yes, no]

если в списке не все целые числа вернуть False.

"""
def yes_or_no(nums):
    for n in nums:
        if not isinstance(n, int): # все ли элементы - целые числа
            return False

    seen = set()      # сюда встреченные числа
    result = []       # сюда ответы "yes"/"no"

    for n in nums:
        if n in seen:
            result.append("yes")
        else:
            result.append("no")
            seen.add(n)

    return result

print(yes_or_no([1, 2, 3, 1, 4]))