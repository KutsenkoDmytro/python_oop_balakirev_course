'''
Подвиг 4. (task_3.py)

Вам необходимо написать программу по работе с массивом однотипных данных (например, только числа или строки и т.п.). Для этого нужно объявить класс с именем Array, объекты которого создаются командой:

ar = Array(max_length, cell)
где max_length - максимальное количество элементов в массиве; cell - ссылка на класс, описывающий отдельный элемент этого массива (см. далее, класс Integer). Начальные значения в ячейках массива (в объектах класса Integer) должны быть равны 0.

Для работы с целыми числами объявите в программе еще один класс с именем Integer, объекты которого создаются командой:

cell = Integer(start_value)
где start_value - начальное значение ячейки (в данном случае - целое число).

В классе Integer должно быть следующее свойство (property):

value - для изменения и считывания значения из ячейки (само значение хранится в локальной приватной переменной; имя придумайте сами).

При попытке присвоить не целое число должно генерироваться исключение командой:

raise ValueError('должно быть целое число')
Для обращения к отдельным элементам массива в классе Array необходимо определить набор магических методов для следующих операций:

value = ar[0] # получение значения из первого элемента (ячейки) массива ar
ar[1] = value # запись нового значения во вторую ячейку массива ar
Если индекс не целое число или число меньше нуля или больше либо равно max_length, то должно генерироваться исключение командой:

raise IndexError('неверный индекс для доступа к элементам массива')
Пример использования классов (эти строчки в программе не писать):

ar_int = Array(10, cell=Integer)
print(ar_int[3])
print(ar_int) # должны отображаться все значения массива в одну строчку через пробел
ar_int[1] = 10
ar_int[1] = 10.5 # должно генерироваться исключение ValueError
ar_int[10] = 1 # должно генерироваться исключение IndexError
P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.

P.P.S. В качестве дополнительного домашнего задания: объявите еще один класс Float для работы с вещественными числами и создайте массив, используя тот же класс Array, с этим новым типом данных.

'''


class Integer:

    def __init__(self, start_value=0):
        self.__value = start_value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        if not isinstance(val, int):
            raise ValueError('должно быть целое число')
        self.__value = val


class Array:

    def __init__(self, max_length, cell=Integer):
        self.max_length = max_length
        self.cells = [cell() for i in range(max_length)]

    def __str__(self):
        st = ' '.join([str(obj.value) for obj in self.cells])
        return st

    def __getitem__(self, item):
        self.__check_value(item)
        return self.cells[item].value

    def __setitem__(self, key, value):
        self.__check_value(key)
        self.cells[key].value = value

    def __check_value(self, value):
        if not (isinstance(value, int) and 0 <= value < self.max_length):
            raise IndexError('неверный индекс для доступа к элементам массива')


# Для проверки.
ar_int = Array(10, cell=Integer)
print(ar_int[3])
print(
    ar_int)  # должны отображаться все значения массива в одну строчку через пробел
ar_int[1] = 10
print(ar_int)
# ar_int[1] = 10.5 # должно генерироваться исключение ValueError
# ar_int[10] = 1 # должно генерироваться исключение IndexError



# ДОМАШНЕЕ ЗАДАНИЕ:
class Float:

    def __init__(self, start_value=0.0):
        self.__value = start_value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        if not isinstance(val, float):
            raise ValueError('должно быть вещественное число')
        self.__value = val

print('==================')

# Для проверки.
ar_float = Array(10, cell=Float)
print(ar_float[3])
print(ar_float)  # должны отображаться все значения массива в одну строчку через пробел
ar_float[1] = 10.0
print(ar_float)
# ar_float[1] = 10.5 # должно генерироваться исключение ValueError
# ar_float[10] = 1 # должно генерироваться исключение IndexError