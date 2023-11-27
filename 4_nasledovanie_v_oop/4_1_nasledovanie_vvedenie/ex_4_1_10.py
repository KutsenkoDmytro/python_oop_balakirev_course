'''
Подвиг 10 (на повторение). (task_7.py)

Объявите в программе класс Vector, объекты которого создаются командой:

v = Vector(x1, x2, ..., xN)
где x1, x2, ..., xN - координаты радиус-вектора (числа: целые или вещественные).

С объектами этого класса должны выполняться команды:

v1 = Vector(1, 2, 3)
v2 = Vector(3, 4, 5)
v = v1 + v2 # формируется новый вектор (объект класса Vector) с соответствующими координатами
v = v1 - v2 # формируется новый вектор (объект класса Vector) с соответствующими координатами
Если размерности векторов v1 и v2 не совпадают, то генерировать исключение:

raise TypeError('размерности векторов не совпадают')
В самом классе Vector объявите метод с именем get_coords, который возвращает кортеж из текущих координат вектора.

На основе класса Vector объявите дочерний класс VectorInt для работы с целочисленными координатами:

v = VectorInt(1, 2, 3, 4)
v = VectorInt(1, 0.2, 3, 4) # ошибка: генерируется исключение raise ValueError('координаты должны быть целыми числами')
При операциях сложения и вычитания с объектом класса VectorInt:

v = v1 + v2  # v1 - объект класса VectorInt
v = v1 - v2  # v1 - объект класса VectorInt
должен формироваться объект v как объект класса Vector, если хотя бы одна координата является вещественной. Иначе, v должен быть объектом класса VectorInt.

P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.

'''


class Vector:

    def __init__(self, *args):
        self.coords = list(args) if args else []

    def __check_dimens(self, other):
        if len(self.coords) != len(other.coords):
            raise TypeError('размерности векторов не совпадают')

    def __add__(self, other):
        self.__check_dimens(other)
        new_coords = tuple(map(lambda x, y: x + y, self.coords, other.coords))
        return self.create_new_obj(new_coords)

    def __sub__(self, other):
        self.__check_dimens(other)
        new_coords = tuple(map(lambda x, y: x - y, self.coords, other.coords))
        return self.create_new_obj(new_coords)

    def create_new_obj(self, coords):
        return self.__class__(*coords)

    def get_coords(self):
        return tuple(self.coords)


class VectorInt(Vector):

    def __init__(self, *args):
        lst = list(args) if args else []
        if not self.__check_int(lst):
            raise ValueError('координаты должны быть целыми числами')
        super().__init__(*args)

    @staticmethod
    def __check_int(value: list | tuple):
        return all(type(i) is int for i in value)

    def create_new_obj(self,coords):  # Переопределяем метод базового класса, чтобы при передачи координаты вещественного типа формировался екз. базового класса.
        if self.__check_int(coords):
            return self.__class__(*coords)
        else:
            return Vector(*coords)



# Test
v1 = Vector(1, 2, 3)
v2 = Vector(3, 4, 5)

assert (v1 + v2).get_coords() == (4, 6, 8), "операция сложения дала неверные значения (или некорректно работает метод get_coords)"
assert (v1 - v2).get_coords() == (-2, -2, -2), "операция вычитания дала неверные значения (или некорректно работает метод get_coords)"

v = VectorInt(1, 2, 3, 4)
assert isinstance(v, Vector), "класс VectorInt должен наследоваться от класса Vector"

try:
    v = VectorInt(1, 2, 3.4, 4)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError для команды v = VectorInt(1, 2, 3.4, 4)"


v1 = VectorInt(1, 2, 3, 4)
v2 = VectorInt(4, 2, 3, 4)
v3 = Vector(1.0, 2, 3, 4)

v = v1+v2
assert type(v) == VectorInt, "при сложении вектором с целочисленными координатами должен формироваться объект класса VectorInt"
v = v1+v3
assert type(v) == Vector, "при сложении вектором с вещественными координатами должен формироваться объект класса Vector"
