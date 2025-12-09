"""
Написать функцию которая принимает строку в которой есть 
круглые скобки и возвращает True или False анализируя все ли скобки 
являются закрытыми и расставлены в правильном порядке.
Примеры:
    (()()) -> True
    (()()() -> False
    (hello(2)ver()(33)python) -> True
    (hello(2()ver(33)python)) -> True
    (hello(2()ver(33)python) -> False

"""

def bool_ckecker(string):
    stack = []
    for char in string:
        if char ==  "(":
            stack.append("(")
        elif char == ")":
            if stack == []:
                return False
            else:
                stack.pop()

    if stack == []:
        return True
    else:
        return False