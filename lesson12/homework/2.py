"""
Создать класс BookCard, в классе должны быть:

- private атрибут author - автор (тип str)
- private атрибут title - название книги (тип str)
- private атрибут year - год издания (тип int)
- магический метод __init__, который принимает author, title, year
- магические методы сравнения для сортировки книг по году издания
- сеттеры и геттеры к атрибутам author, title, year. В сеттерах сделать проверку
  на тип данных, если тип данных не подходит, то бросить ValueError. Декущего ля года
  издания дополнительно проверить на валидность (> 0, <= тгода).

Аксессоры реализоваться через property.
"""
class BookCard:
    def __init__(self, author, title, year):
        self.author = author
        self.title = title
        self.year = year

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        if not isinstance(value, str):
            raise ValueError("Author must be str")
        self.__author = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if not isinstance(value, int):
            raise ValueError("Year must be int")
        if value <= 0 or value > 2025: 
            raise ValueError("Invalid year")
        self.__year = value

    def __lt__(self, other):
        return self.year < other.year

    def __eq__(self, other):
        return self.year == other.year
    
b1 = BookCard("Толстой", "Война и мир", 1873)
b2 = BookCard("Оруэлл", "1984", 1949)
b3 = BookCard("Роулинг", "Гарри Поттер", 1997)

books = [b1, b2, b3]

for b in sorted(books):
    print(b.__dict__)