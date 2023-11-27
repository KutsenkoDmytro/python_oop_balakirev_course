'''
Подвиг 8. (task_5.py)

Вам необходимо создать простую программу по учету семейного бюджета. Для этого в программе объявите два класса с именами:

Budget - для управления семейным бюджетом; Item - пункт расходов бюджета.

Объекты класса Item должны создаваться командой:

it = Item(name, money)
где name - название статьи расхода; money - сумма расходов (вещественное или целое число).

Соответственно, в каждом объекте класса Item должны формироваться локальные атрибуты name и money с переданными значениями. Также с объектами класса Item должны выполняться следующие операторы:

s = it1 + it2 # сумма для двух статей расходов
и в общем случае:

s = it1 + it2 + ... + itN # сумма N статей расходов
При суммировании оператор + должен возвращать число - вычисленную сумму по атрибутам money соответствующих объектов класса Item.

Объекты класса Budget создаются командой:

my_budget = Budget()
А сам класс Budget должен иметь следующие методы:

add_item(self, it) - добавление статьи расхода в бюджет (it - объект класса Item);
remove_item(self, indx) - удаление статьи расхода из бюджета по его порядковому номеру indx (индексу: отсчитывается с нуля);
get_items(self) - возвращает список всех статей расходов (список из объектов класса Item).

Пример использования классов (эти строчки в программе писать не нужно):

my_budget = Budget()
my_budget.add_item(Item("Курс по Python ООП", 2000))
my_budget.add_item(Item("Курс по Django", 5000.01))
my_budget.add_item(Item("Курс по NumPy", 0))
my_budget.add_item(Item("Курс по C++", 1500.10))

# вычисление общих расходов
s = 0
for x in my_budget.get_items():
    s = s + x
P.S. В программе требуется только объявить класс. На экран ничего выводить не нужно.

'''

class Item:

    def __init__(self, name, money):
        self.name = name
        self.money = money

    def __setattr__(self, key, value):
        if key == 'name':
            self.__check_val_str(value)
        elif key == 'money':
            self.__check_val_num(value)
        object.__setattr__(self, key, value)

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.money + other.money
        else:
            raise ValueError('Не верный тип данных.')

    def __radd__(self, other):
        self.__check_val_num(other)
        return other + self.money

    @staticmethod
    def __check_val_str(value):
        if not isinstance(value, str):
            raise ValueError('Не верный тип данных.')

    @staticmethod
    def __check_val_num(value):
        if type(value) not in {int, float}:
            raise ValueError('Не верный тип данных.')

class Budget:

    def __init__(self):
        self.items = []

    def add_item(self, it):
        self.items.append(it)

    def remove_item(self, indx):
        self.items.pop(indx)

    def get_items(self):
        return self.items


# # Для проверки.
# my_budget = Budget()
# my_budget.add_item(Item("Курс по Python ООП", 2000))
# my_budget.add_item(Item("Курс по Django", 5000.01))
# my_budget.add_item(Item("Курс по NumPy", 0))
# my_budget.add_item(Item("Курс по C++", 1500.10))
#
# # вычисление общих расходов
# s = 0
# for x in my_budget.get_items():
#     s = s + x
#
# print(s)

