'''
Написать функцию которая принимает 2 стороны прямоугольника 
и возвращает либо площадь либо периметр в зависимости от дополнительного параметра.

'''
# Функция для вычисления площади
def area(a, b):
    return a * b

# Функция для вычисления периметра
def perimeter(a, b):
    return 2 * (a + b)

# Главная функция, которая выбирает, что возвращать
def rectangle(a, b, param="area"):
    try:
        if param == "area":
            return area(a, b)

        elif param == "perimeter":
            return perimeter(a, b)

        # если неверный параметр ввели
        raise ValueError("Неверный параметр mode")

    except ValueError as error:
        return f"Ошибка: {error}"

side1 = float(input("Введите первую сторону прямоугольника: "))
side2 = float(input("Введите вторую сторону прямоугольника: "))
param  = input("Что вычислить? (area / perimeter): ")

print(rectangle(side1, side2, param))