'''
Подвиг 4. (task_1.py)

С помощью множественного наследования удобно описывать принадлежность объектов к нескольким разным группам. Выполним такой пример.

ИерархияЧисел

Определите в программе классы в соответствии с их иерархией, представленной на рисунке выше:

Digit, Integer, Float, Positive, Negative
Каждый объект этих классов должен создаваться однотипной командой вида:

obj = Имя_класса(value)
где value - числовое значение. В каждом классе следует делать свою проверку на корректность значения value:

в классе Digit: value - любое число;
в классе Integer: value - целое число;
в классе Float: value - вещественное число;
в классе Positive: value - положительное число;
в классе Negative: value - отрицательное число.
Если проверка не проходит, то генерируется исключение командой:

raise TypeError('значение не соответствует типу объекта')
После этого объявите следующие дочерние классы:

PrimeNumber - простые числа; наследуется от классов Integer и Positive;
FloatPositive - наследуется от классов Float и Positive.

Создайте три объекта класса PrimeNumber и пять объектов класса FloatPositive с произвольными допустимыми для них значениями. Сохраните все эти объекты в виде списка digits.

Затем, используя функции isinstance() и filter(), сформируйте следующие списки из указанных объектов:

lst_positive - все объекты, относящиеся к классу Positive;
lst_float - все объекты, относящиеся к классу Float.

P.S. В программе требуется объявить только классы и создать списки. На экран выводить ничего не нужно.

'''
from abc import ABC, abstractmethod


class Digit(ABC):

    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self.check_value(value)
        self._value = value

    @staticmethod
    @abstractmethod
    def check_value(value):
        if not isinstance(value, (int, float)):
            raise TypeError('значение не соответствует типу объекта')


class Integer(Digit):

    def __init__(self, value):
        super().__init__(value)

    @staticmethod
    def check_value(value):
        if not isinstance(value, int):
            raise TypeError('значение не соответствует типу объекта')


class Float(Digit):

    def __init__(self, value):
        super().__init__(value)

    @staticmethod
    def check_value(value):
        if not isinstance(value, float):
            raise TypeError('значение не соответствует типу объекта')


class Positive(Digit):

    def __init__(self, value):
        super().__init__(value)

    @staticmethod
    def check_value(value):
        if not (isinstance(value, (int, float)) and value > 0):
            raise TypeError('значение не соответствует типу объекта')


class Negative(Digit):

    def __init__(self, value):
        super().__init__(value)

    @staticmethod
    def check_value(value):
        if not (isinstance(value, (int, float)) and value < 0):
            raise TypeError('значение не соответствует типу объекта')


class PrimeNumber(Integer, Positive):

    def __init__(self, value):
        super().__init__(value)

    @staticmethod
    def check_value(value):
        Integer.check_value(value)
        Positive.check_value(value)


class FloatPositive(Float, Positive):

    def __init__(self, value):
        super().__init__(value)

    @staticmethod
    def check_value(value):
        Float.check_value(value)
        Positive.check_value(value)


digits  = [PrimeNumber(i) for i in range(1,4)] + [FloatPositive(float(i)) for i in range(1,6)]
lst_positive = list(filter(lambda x: isinstance(x, PrimeNumber), digits))
lst_float = list(filter(lambda x: isinstance(x, FloatPositive), digits))


# # Для проверки:
# for i in lst_positive:
#     print(i.value)
#
# for i in lst_float:
#     print(i.value)

