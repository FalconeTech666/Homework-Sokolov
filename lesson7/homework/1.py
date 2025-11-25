"""
Запросить у учителя оценки ученика по одной до тех пор пока он не введет 0. 
Выдать средний бал ученика.

"""
sum_grades = 0       
sum_counts = 0 

while True:
    grade = int(input("Введите оценку ученика: "))
    print("Для окончания работы программы введите 0")
    if grade == 0:
        break

    sum_grades += grade
    sum_counts += 1

avg_grades = sum_grades/sum_counts

print("Средний балл ученика:", avg_grades)