'''
Подвиг 10. (task_8.py)

Объявите в программе класс с именем Box (ящик), объекты которого должны создаваться командой:

box = Box()
А сам класс иметь следующие методы:

add_thing(self, obj) - добавление предмета obj (объект другого класса Thing) в ящик;
get_things(self) - получение списка объектов ящика.

Для описания предметов необходимо объявить еще один класс Thing. Объекты этого класса должны создаваться командой:

obj = Thing(name, mass)
где name - название предмета (строка); mass - масса предмета (число: целое или вещественное). Объекты класса Thing должны поддерживать операторы сравнения:

obj1 == obj2
obj1 != obj2
Предметы считаются равными, если у них одинаковые названия name (без учета регистра) и массы mass.

Также объекты класса Box должны поддерживать аналогичные операторы сравнения:

box1 == box2
box1 != box2
Ящики считаются равными, если одинаковы их содержимое (для каждого объекта класса Thing одного ящика и можно найти ровно один равный объект из второго ящика).

Пример использования классов:

b1 = Box()
b2 = Box()

b1.add_thing(Thing('мел', 100))
b1.add_thing(Thing('тряпка', 200))
b1.add_thing(Thing('доска', 2000))

b2.add_thing(Thing('тряпка', 200))
b2.add_thing(Thing('мел', 100))
b2.add_thing(Thing('доска', 2000))

res = b1 == b2 # True
P.S. В программе только объявить классы, выводить на экран ничего не нужно.


'''


class Box:
    '''Описывает коробку.'''

    def __init__(self):
        self.things = []

    def add_thing(self, obj):
        self.things.append(obj)

    def get_things(self):
        return self.things

    def __eq__(self, other):
        lst_attrs1 = [a.get_tuple_attr() for a in self.things]
        lst_attrs2 = [a.get_tuple_attr() for a in other.get_things()]

        return sorted(lst_attrs1) == sorted(lst_attrs2)


class Thing:
    '''Описывает предмет.'''

    def __init__(self, name: str, mass: int | float):
        self.name = name
        self.mass = mass

    def get_tuple_attr(self):
        return (self.name.lower(), self.mass)

    def __eq__(self, other):
        return self.get_tuple_attr() == other.get_tuple_attr()

# # Для проверки.
# b1 = Box()
# b2 = Box()
#
# b1.add_thing(Thing('мел', 100))
# b1.add_thing(Thing('тряпка', 200))
# b1.add_thing(Thing('доска', 2000))
#
# b2.add_thing(Thing('тряпка', 200))
# b2.add_thing(Thing('мел', 100))
# b2.add_thing(Thing('доска', 2000))
#
# res = b1 == b2  # True
# print(res)