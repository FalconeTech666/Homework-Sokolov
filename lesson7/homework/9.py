# '''

# *
# В структуре данных из 5 урока задание №2 каждому сотруднику
# добавить к параметру "навык" параметр "мастерство" измеряемый от 0 до 100
#
# Написать программу которая анализирует всю структуру данных и выводит сотрудников
# с наибольшим параметром "мастерство" для каждого существующего навыка.
# Пример вывода:
#     1. Python - Иванов - 98
#     2. JS - Петров  - 74
#     3. Базы данных - Николаев - 87
#     ...
#
#
# ** Пример вывода (перед выводам отсортировать по убыванию "мастерства"):
#
#     --------------------------------------------------
#     | № |   Навык     |       ФИО       | Мастерство |
#     ==================================================
#     | 1 | Python      | Иванов Н.С.     |     98     |
#     | 2 | JS          | Петров В.В.     |     87     |
#     | 3 | Базы данных | Николаев Е.Н.   |     74     |
#     ...
# '''

staff = {
    "Смирнов Алексей Викторович": {
        "position": "Python разработчик",
        "birth_year": 1992,
        "skills": [
            {"skill": "Python", "mastery": 98},
            {"skill": "Django", "mastery": 87},
            {"skill": "SQL", "mastery": 74},
        ],
        "children": [{"name": "Миша", "birth_year": 2018}]
    },

    "Ковалёва Мария Андреевна": {
        "position": "Бизнес-аналитик",
        "birth_year": 1989,
        "skills": [
            {"skill": "Excel", "mastery": 90},
            {"skill": "SQL", "mastery": 82},
            {"skill": "Power BI", "mastery": 95},
        ],
        "children": [
            {"name": "Анна", "birth_year": 2015},
            {"name": "Сергей", "birth_year": 2020},
        ]
    },

    "Жуков Дмитрий Олегович": {
        "position": "DevOps инженер",
        "birth_year": 1985,
        "skills": [
            {"skill": "Docker", "mastery": 80},
            {"skill": "Linux", "mastery": 93},
            {"skill": "Kubernetes", "mastery": 87},
        ],
        "children": [{"name": "Олег", "birth_year": 2012}]
    }
}

# --- Анализ навыков: ищем максимум мастерства по каждой технологии ---
best_by_skill = {}

for name, data in staff.items():
    for item in data["skills"]:
        skill = item["skill"]
        mastery = item["mastery"]

        # если такого навыка ещё нет или текущий сотрудник лучше — обновляем
        if skill not in best_by_skill or mastery > best_by_skill[skill]["mastery"]:
            best_by_skill[skill] = {
                "name": name,
                "mastery": mastery
            }

# Преобразуем в список и сортируем по убыванию мастерства
result = sorted(best_by_skill.items(), key=lambda x: x[1]["mastery"], reverse=True)

# --- Вывод таблицы ---
print("=" * 70)
print(f"| {'№':<3} | {'Навык':<15} | {'ФИО':<30} | {'Мастерство':<11} |")
print("=" * 70)

for i, (skill, info) in enumerate(result, start=1):
    print(f"| {i:<3} | {skill:<15} | {info['name']:<30} | {info['mastery']:<11} |")

print("=" * 70)