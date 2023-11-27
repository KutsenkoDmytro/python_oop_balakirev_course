'''
Подвиг 9. (task_6.py)

Объявите класс Box3D для представления прямоугольного параллелепипеда (бруска), объекты которого создаются командой:

box = Box3D(width, height, depth)
где width, height, depth - ширина, высота и глубина соответственно (числа: целые или вещественные)

В каждом объекте класса Box3D должны создаваться публичные атрибуты:

width, height, depth - ширина, высота и глубина соответственно.

С объектами класса Box3D должны выполняться следующие операторы:

box1 = Box3D(1, 2, 3)
box2 = Box3D(2, 4, 6)

box = box1 + box2 # Box3D: width=3, height=6, depth=9 (соответствующие размерности складываются)
box = box1 * 2    # Box3D: width=2, height=4, depth=6 (каждая размерность умножается на 2)
box = 3 * box2    # Box3D: width=6, height=12, depth=18
box = box2 - box1 # Box3D: width=1, height=2, depth=3 (соответствующие размерности вычитаются)
box = box1 // 2   # Box3D: width=0, height=1, depth=1 (соответствующие размерности целочисленно делятся на 2)
box = box2 % 3    # Box3D: width=2, height=1, depth=0
При каждой арифметической операции следует создавать новый объект класса Box3D с соответствующими значениями локальных атрибутов.

P.S. В программе достаточно только объявить класс Box3D. На экран ничего выводить не нужно.

'''


class Box3D:
    '''Описывает прямоугольный параллелепипеда (брусок)'''

    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def __setattr__(self, key, value):
        if key in {'width', 'height', 'depth'}:
            self.__check_number(value)
        object.__setattr__(self, key, value)

    def __add__(self, other):
        self.__check_val_obj(other)
        n_width = self.width + other.width
        n_heigh = self.height + other.height
        n_depth = self.depth + other.depth
        return self.__class__(n_width, n_heigh, n_depth)

    def __mul__(self, other):
        self.__check_number(other)
        n_width = self.width * other
        n_heigh = self.height * other
        n_depth = self.depth * other
        return self.__class__(n_width, n_heigh, n_depth)

    def __rmul__(self, other):
        return self * other

    def __sub__(self, other):
        self.__check_val_obj(other)
        n_width = self.width - other.width
        n_heigh = self.height - other.height
        n_depth = self.depth - other.depth
        return self.__class__(n_width, n_heigh, n_depth)

    def __floordiv__(self, other):
        self.__check_number(other)
        n_width = self.width // other
        n_heigh = self.height // other
        n_depth = self.depth // other
        return self.__class__(n_width, n_heigh, n_depth)

    def __mod__(self, other):
        self.__check_number(other)
        n_width = self.width % other
        n_heigh = self.height % other
        n_depth = self.depth % other
        return self.__class__(n_width, n_heigh, n_depth)

    @classmethod
    def __check_val_obj(cls, value):
        if not isinstance(value, cls):
            raise ValueError('Не верный тип данных.')

    @staticmethod
    def __check_number(value):
        if type(value) not in {int, float}:
            raise ValueError('Не верный тип данных.')


# # Для проверки.
# box1 = Box3D(1, 2, 3)
# box2 = Box3D(2, 4, 6)
#
# box = box1 + box2 # Box3D: width=3, height=6, depth=9 (соответствующие размерности складываются)
# box = box1 * 2    # Box3D: width=2, height=4, depth=6 (каждая размерность умножается на 2)
# box = 3 * box2    # Box3D: width=6, height=12, depth=18
# box = box2 - box1 # Box3D: width=1, height=2, depth=3 (соответствующие размерности вычитаются)
# box = box1 // 2   # Box3D: width=0, height=1, depth=1 (соответствующие размерности целочисленно делятся на 2)
# box = box2 % 3    # Box3D: width=2, height=1, depth=0
# print(box.width, box.height, box.depth)