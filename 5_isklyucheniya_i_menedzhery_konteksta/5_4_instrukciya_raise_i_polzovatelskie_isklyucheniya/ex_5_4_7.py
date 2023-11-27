'''
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/wLaOyNN8x7E

Значимый подвиг 7. Вам поручается разработать класс TupleData, элементами которого могут являются только объекты классов: CellInteger, CellFloat и CellString.



Вначале в программе нужно объявить класс CellInteger, CellFloat и CellString, объекты которых создаются командами:

cell_1 = CellInteger(min_value, max_value)
cell_2 = CellFloat(min_value, max_value)
cell_3 = CellString(min_length, max_length)

где min_value, max_value - минимальное и максимальное допустимое значение в ячейке; min_length, max_length - минимальная и максимальная допустимая длина строки в ячейке.

В каждом объекте этих классов должны формироваться локальные атрибуты с именами _min_value, _max_value или _min_length, _max_length и соответствующими значениями.

Запись и считывание текущего значения в ячейке должно выполняться через объект-свойство (property) с именем:

value - для записи и считывания значения в ячейке (изначально возвращает значение None).

Если в момент записи новое значение не соответствует диапазону [min_value; max_value] или [min_length; max_length], то генерируется исключения командами:

raise CellIntegerException('значение выходит за допустимый диапазон')  # для объектов класса CellInteger
raise CellFloatException('значение выходит за допустимый диапазон')    # для объектов класса CellFloat
raise CellStringException('длина строки выходит за допустимый диапазон')  # для объектов класса CellString

Все три класса исключений должны быть унаследованы от одного общего класса:

CellException

Далее, объявите класс TupleData, объекты которого создаются командой:

ld = TupleData(cell_1, ..., cell_N)

где cell_1, ..., cell_N - объекты классов CellInteger, CellFloat и CellString (в любом порядке и любом количестве).

Обращение к отдельной ячейке должно выполняться с помощью оператора:

value = ld[index] # считывание значения из ячейке с индексом index
ld[index] = value # запись нового значения в ячейку с индексом index

Индекс index отсчитывается с нуля (для первой ячейки) и является целым числом. Если значение index выходит за диапазон [0; число ячеек-1], то генерировать исключение IndexError.

Также с объектами класса TupleData должны выполняться следующие функции и операторы:

res = len(ld) # возвращает общее число элементов (ячеек) в объекте ld
for d in ld:  # перебирает значения ячеек объекта ld (значения, а не объекты ячеек)
    print(d)

Все эти классы в программе можно использовать следующим образом:

ld = TupleData(CellInteger(0, 10), CellInteger(11, 20), CellFloat(-10, 10), CellString(1, 100))

try:
    ld[0] = 1
    ld[1] = 20
    ld[2] = -5.6
    ld[3] = "Python ООП"
except CellIntegerException as e:
    print(e)
except CellFloatException as e:
    print(e)
except CellStringException as e:
    print(e)
except CellException:
    print("Ошибка при обращении к ячейке")
except Exception:
    print("Общая ошибка при работе с объектом TupleData")


P.S. Данная программа должна быть выполнена штатно, без ошибок. На экран отображать ничего не нужно.
 Memory limit: 256 MBTime limit: 15 seconds

'''
from abc import ABC, abstractmethod

class CellException(Exception):
    '''Базовый класс исключений для ячейки.'''

class CellIntegerException(CellException):
    '''Исключения для целочисленного типа.'''

class CellFloatException(CellException):
    '''Исключения для вещественного типа.'''

class CellStringException(CellException):
    '''Исключения для строкового типа.'''



class CellBase(ABC):
    '''Базовый класс для представления ячейки.'''

    def __init__(self, min_value = None, max_value = None, min_length = None, max_length = None):
        self._min_value = min_value
        self._max_value = max_value
        self._min_length = min_length
        self._max_length = max_length
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    @abstractmethod
    def value(self, value):
        self._value = value

    @abstractmethod
    def _check_value(self,value):
        '''Проверяет корректность переданного значения.'''

class CellInteger(CellBase):
    '''Представляет ячейку целочисленного типа.'''

    def __init__(self,min_value, max_value):
        super().__init__(min_value=min_value,max_value=max_value)

    @CellBase.value.setter
    def value(self, value):
        if not self._check_value(value):
            raise CellIntegerException('значение выходит за допустимый диапазон')
        self._value = value

    def _check_value(self, value):
        return getattr(self,'_min_value') <= value <= getattr(self,'_max_value')


class CellFloat(CellBase):
    '''Представляет ячейку вещественного типа.'''

    def __init__(self,min_value, max_value):
        super().__init__(min_value=min_value,max_value=max_value)

    @CellBase.value.setter
    def value(self, value):
        if not self._check_value(value):
            raise CellFloatException('значение выходит за допустимый диапазон')
        self._value = value

    def _check_value(self, value):
        return getattr(self,'_min_value') <= value <= getattr(self,'_max_value')


class CellString(CellBase):
    '''Представляет ячейку строкового типа.'''

    def __init__(self,min_length, max_length):
        super().__init__(min_length=min_length, max_length=max_length)

    @CellBase.value.setter
    def value(self, value):
        if not self._check_value(value):
            raise CellStringException('длина строки выходит за допустимый диапазон')
        self._value = value

    def _check_value(self, value):
        return getattr(self,'_min_length') <= len(value) <= getattr(self,'_max_length')


class TupleData:

    def __init__(self,*args):
        lst = list(args) if args else []
        self.cells = lst

    def __getitem__(self, item):
        self.__check_index(item)
        return self.cells[item].value

    def __setitem__(self, key, value):
        self.__check_index(key)
        self.cells[key].value = value

    def __len__(self):
        return len(self.cells)

    def __iter__(self):
        for d in self.cells:
            yield d.value

    def __check_index(self,indx):
        if not (type(indx) is int and 0 <= indx <= len(self.cells)-1):
            raise IndexError


#Для проверки.
ld = TupleData(CellInteger(0, 10), CellInteger(11, 20), CellFloat(-10, 10), CellString(1, 100))

try:
    ld[0] = 1
    ld[1] = 20
    ld[2] = -5.6
    ld[3] = "Python ООП"
except CellIntegerException as e:
    print(e)
except CellFloatException as e:
    print(e)
except CellStringException as e:
    print(e)
except CellException:
    print("Ошибка при обращении к ячейке")
except Exception:
    print("Общая ошибка при работе с объектом TupleData")


# ld = TupleData(CellInteger(0, 10), CellInteger(11, 20), CellFloat(-10, 10), CellString(1, 100))
#
#
# try:
#     ld[0] = 1
#     ld[1] = 20
#     ld[2] = -5.6
#     ld[3] = "a"
# except CellIntegerException as e:
#     print(e)
# except CellFloatException as e:
#     print(e)
# except CellStringException as e:
#     print(e)
# except CellException:
#     print("Ошибка при обращении к ячейке")
# except Exception:
#     print("Общая ошибка при работе с объектом TupleData")
#
# t = TupleData(CellInteger(-10, 10), CellInteger(0, 2), CellString(5, 10))
#
# d = (1, 0, 'sergey')
# t[0] = d[0]
# t[1] = d[1]
# t[2] = d[2]
# for i, x in enumerate(t):
#     assert x == d[i], "объект класса TupleData хранит неверную информацию"
#
# assert len(t) == 3, "неверное число элементов в объекте класса TupleData"
#
# cell = CellFloat(-5, 5)
# try:
#     cell.value = -6.0
# except CellFloatException:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение CellFloatException"
#
# cell = CellInteger(-1, 7)
# try:
#     cell.value = 8
# except CellIntegerException:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение CellIntegerException"
#
# cell = CellString(5, 7)
# try:
#     cell.value = "hello world"
# except CellStringException:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение CellStringException"
#
# assert issubclass(CellIntegerException, CellException) and issubclass(CellFloatException, CellException) and issubclass(
#     CellStringException,
#     CellException), "классы CellIntegerException, CellFloatException, CellStringException должны наследоваться от класса CellException"