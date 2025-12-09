'''
1.Открыть и обработать файл students_grades.txt.
2.Собрать все данные в словарь ниже приведенного формата.
3.Записать в файл "excellent_students.txt" учеников из каждого класса с наибольшим балом.
{
    "9A":[
        {'fio':'fio', 
         'objects':{
            'mathematics':[4, 9, 7],
            'physics':[8, 9, 8, 6],
            ...:...
            }
        },
        ...        
    ],
    "9Б":[
        ...
    ]
}

'''

with open("students_grades.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    parts = lines.split(", ")
