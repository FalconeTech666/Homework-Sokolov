"""
Создать класс Student.


Определить атрибуты:
    - surname - фамилия
    - name - имя
    - group - номер группы
    - grads - список оценок

Определить методы:
    - инициализатор __init__
    - Методы __eq__, __ne__, __lt__, __gt__, __le__, __ge__, которые будут сравнивать
    студентов по среднему баллу
    - метод add_grade - добавляет в список оценок одну или несколько оценок от 1 до 10
    - метод average_grade -считает и возвращает среднюю оценку ученика

Создать список из 5 студентов класса и вывести его отсортированным по возрастанию
и убыванию.

Вывести студентов, у которых средний балл больше 8
"""
from pprint import pprint

class Student:
    def __init__(self, surname, name, group, grads):
        self.surname = surname
        self.name = name
        self.group = group
        self.grads = grads
    def add_grade(self, grade):
        if isinstance(grade, list):
            self.grads.extend(grade)
        else:
            self.grads.append(grade)
    def average_grade(self):
        if not self.grads:      
            return 0
        total = sum(self.grads)
        count = len(self.grads)
        return total / count
    def __eq__(self, other):
        return self.average_grade() == other.average_grade()
    def __ne__(self, other):
        return self.average_grade() != other.average_grade()
    def __lt__(self, other):
        return self.average_grade() < other.average_grade()
    def __gt__(self, other):
        return self.average_grade() > other.average_grade()
    def __le__(self, other):
        return self.average_grade() <= other.average_grade()
    def __ge__(self, other):
        return self.average_grade() >= other.average_grade()

s1 = Student("Иванов", "Пётр", "9A", [9, 8, 7])
s2 = Student("Сидоров", "Максим", "9A", [5, 6, 7])
s3 = Student("Козлов", "Илья", "9B", [10, 9, 9])
s4 = Student("Смирнова", "Анна", "9B", [8, 9, 10])
s5 = Student("Орлова", "Мария", "9A", [6, 7, 6])

students = [s1, s2, s3, s4, s5]

print("\nПо возрастанию:")
for st in sorted(students):
    pprint(st.__dict__)

print("\nПо убыванию:")
for st in sorted(students, reverse=True):
    pprint(st.__dict__)

print("\nСредний балл > 8:")
for st in students:
    if st.average_grade() > 8:
        pprint(st.__dict__)
