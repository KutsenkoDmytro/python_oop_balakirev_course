'''
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/0vmRMf5f4Iw

Подвиг 10. Объявите в программе класс FloatValidator, объекты которого создаются командой:

fv = FloatValidator(min_value, max_value)

где min_value, max_value - минимальное и максимальное допустимое значение (диапазон [min_value; max_value]).

Объекты этого класса предполагается использовать следующим образом:

fv(value)

где value - проверяемое значение. Если value не вещественное число или не принадлежит диапазону [min_value; max_value], то генерируется исключение командой:

raise ValueError('значение не прошло валидацию')

По аналогии, объявите класс IntegerValidator, объекты которого создаются командой:

iv = IntegerValidator(min_value, max_value)

и используются командой:

iv(value)

Здесь также генерируется исключение:

raise ValueError('значение не прошло валидацию')

если value не целое число или не принадлежит диапазону [min_value; max_value].

После этого объявите функцию с сигнатурой:

def is_valid(lst, validators): ...

где lst - список из данных; validators - список из объектов-валидаторов (объектов классов FloatValidator и IntegerValidator).

Эта функция должна отбирать из списка все значения, которые прошли хотя бы по одному валидатору. И возвращать новый список с элементами, прошедшими проверку.

Пример использования классов и функции (эти строчки в программе не писать):

fv = FloatValidator(0, 10.5)
iv = IntegerValidator(-10, 20)
lst_out = is_valid([1, 4.5, -10.5, 100, True, 'abc', (1, 2)], validators=[fv, iv])   # [1, 4.5]

P.S. В программе нужно только объявить классы и функцию. На экран ничего выводить не нужно.Memory limit: 256 MBTime limit: 15 seconds


'''
from abc import ABC, abstractmethod


class ValidatorValue(ABC):
    '''Базовый класс валидатора.'''

    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value, *args, **kwargs):
        self._check_value(value)
        return value

    @abstractmethod
    def _check_value(self, value):
        '''Осуществляет проверку переданного значения.'''


class FloatValidator(ValidatorValue):
    '''Осуществляет проверку вещественных чисел.'''

    def __init__(self, min_value, max_value):
        super().__init__(min_value, max_value)

    def _check_value(self, value):
        if not (isinstance(value, float) and\
                self.min_value <= value <= self.max_value):
            raise ValueError('значение не прошло валидацию')

class IntegerValidator(ValidatorValue):
    '''Осуществляет проверку целых чисел.'''

    def __init__(self, min_value, max_value):
        super().__init__(min_value, max_value)

    def _check_value(self, value):
        if not (type(value) is int and \
                self.min_value <= value <= self.max_value):
            raise ValueError('значение не прошло валидацию')

def is_valid(lst, validators):
    '''Возвращает список значений которые прошли валидацию (хотя бы по одному валидатору.)'''
    lst_current = []
    for i in lst:
        for v in validators:
            try:
                lst_current.append(v(i))
                break
            except:
                continue
    return lst_current

fv = FloatValidator(0, 10.5)
iv = IntegerValidator(-10, 20)
lst_out = is_valid([1, 4.5, -10.5, 100, True, 'abc', (1, 2)], validators=[fv, iv])# [1, 4.5]
print(lst_out)