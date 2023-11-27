'''
Подвиг 5. (task_3.py)

Объявите в программе следующие классы без содержимого (используйте оператор pass):

Protists, Plants, Animals, Mosses, Flowering, Worms, Mammals, Human, Monkeys
и постройте схему наследования в соответствии со следующей иерархией древа жизни:

TreeLife

Затем, объявите в программе классы:

Monkey - наследуется от Monkeys и служит для описания обезьян;
Person - наследуется от Human и служит для описания человека;
Flower - наследуется от Flowering и служит для описания цветка;
Worm - наследуется от Worms и служит для описания червей.

Объекты этих классов должны создаваться командами:

obj = Monkey(name, weight, old)
obj = Person(name, weight, old)
obj = Flower(name, weight, old)
obj = Worm(name, weight, old)
где name - наименование (или имя) объекта (строка); weight - вес (вещественное число); old - возраст (целое число). В каждом объекте любого из этих классов должны создаваться соответствующие атрибуты: name, weight, old.

Создайте в программе следующие объекты и сохраните их в виде списка lst_objs:

Monkey: "мартышка", 30.4, 7
Monkey: "шимпанзе", 24.6, 8
Person: "Балакирев", 88, 34
Person: "Верховный жрец", 67.5, 45
Flower: "Тюльпан", 0.2, 1
Flower: "Роза", 0.1, 2
Worm: "червь", 0.01, 1
Worm: "червь 2", 0.02, 1
Затем, используя функции isinstance() и генератор списков (List comprehensions), сформируйте следующие списки из указанных объектов:

lst_animals - все объекты, относящиеся к животным (Animals);
lst_plants - все объекты, относящиеся к растениям (Plants);
lst_mammals - все объекты, относящиеся к млекопитающим (Mammals).

P.S. В программе на экран выводить ничего не нужно.

'''


class Protists:
    '''Протисты.'''

    def __init__(self, name=None, weight=None, old=None):
        self.name = name
        self.weight = weight
        self.old = old


class Plants(Protists):
    '''Растения.'''
    pass


class Mosses(Plants):
    '''Мхи.'''
    pass


class Flowering(Plants):
    '''Цветковые.'''
    pass


class Animals(Protists):
    '''Животные.'''
    pass


class Worms(Animals):
    '''Черви.'''
    pass


class Mammals(Animals):
    '''Млекопитающие.'''
    pass


class Human(Mammals):
    '''Человек.'''
    pass


class Monkeys(Mammals):
    '''Обезяны.'''
    pass


###############


class Monkey(Monkeys):
    '''Описание обезяны.'''
    pass


class Person(Human):
    '''Описание человека.'''
    pass


class Flower(Flowering):
    '''Описание цветка.'''
    pass


class Worm(Worms):
    '''Описание червя.'''
    pass


mn1 = Monkey("мартышка", 30.4, 7)
mn2 = Monkey("шимпанзе", 24.6, 8)
pr1 = Person("Балакирев", 88, 34)
pr2 = Person("Верховный жрец", 67.5, 45)
fl1 = Flower("Тюльпан", 0.2, 1)
fl2 = Flower("Роза", 0.1, 2)
wr1 = Worm("червь", 0.01, 1)
wr2 = Worm("червь 2", 0.02, 1)

lst_objs = [mn1, mn2, pr1, pr2, fl1, fl2, wr1, wr2]

lst_animals = [obj for obj in lst_objs if isinstance(obj, Animals)]
lst_plants = [obj for obj in lst_objs if isinstance(obj, Plants)]
lst_mammals = [obj for obj in lst_objs if isinstance(obj, Mammals)]
