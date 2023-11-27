'''
Подвиг 7. Объявите класс с именем RadiusVector для описания и работы с n-мерным вектором (у которого n координат).
Объекты этого класса должны создаваться командами:

# создание 5-мерного радиус-вектора с нулевыми значениями координат (аргумент - целое число больше 1)
vector = RadiusVector(5)  # координаты: 0, 0, 0, 0, 0

# создание 4-мерного радиус-вектора с координатами: 1, -5, 3.4, 10 (координаты - любые целые или вещественные числа)
vector = RadiusVector(1, -5, 3.4, 10)
То есть, при передаче одного значения, оно интерпретируется, как размерность нулевого радиус-вектора.
Если же передается более одного числового аргумента, то они интерпретируются, как координаты радиус-вектора.

Класс RadiusVector должен содержать методы:

set_coords(coord_1, coord_2, ..., coord_N) - для изменения координат радиус-вектора;
get_coords() - для получения текущих координат радиус-вектора (в виде кортежа).

Также с объектами класса RadiusVector должны поддерживаться следующие функции:

len(vector) - возвращает число координат радиус-вектора (его размерность);
abs(vector) - возвращает длину радиус-вектора (вычисляется как: sqrt(coord_1*coord_1 + coord_2*coord_2 + ...
+ coord_N*coord_N) - корень квадратный из суммы квадратов координат).

Пример использования класса RadiusVector (эти строчки в программе писать не нужно):

vector3D = RadiusVector(3)
vector3D.set_coords(3, -5.6, 8)
a, b, c = vector3D.get_coords()
vector3D.set_coords(3, -5.6, 8, 10, 11) # ошибки быть не должно, последние две координаты игнорируются
vector3D.set_coords(1, 2) # ошибки быть не должно, меняются только первые две координаты
res_len = len(vector3D) # res_len = 3
res_abs = abs(vector3D)
P.S. На экран ничего выводить не нужно, только объявить класс RadiusVector.

'''
from math import sqrt


class RadiusVector:
    '''Класс для описания и работы с n-мерным вектором (у которого n координат).'''

    def __init__(self, *args):
        lst = []
        if len(args) == 1 and type(args[0]) is int:
            lst = [0] * args[0]
        elif len(args) > 1:
            for arg in args:
                self.check_number(arg)  # проверка на тип данных
                lst.append(arg)
        self.coords = lst

    def get_coords(self):
        return tuple(self.coords)

    def set_coords(self, *args):
        if args:
            new_coords = args[:len(self.coords)]
            for i, v in enumerate(new_coords):
                self.check_number(v)  # проверка на тип данных
                self.coords[i] = v

    def __len__(self):
        return len(self.coords)

    def __abs__(self):
        return abs(sqrt(sum([crd * crd for crd in self.coords])))

    @staticmethod
    def check_number(value):
        if type(value) not in {int, float}:
            raise ValueError('Неверный тип данных.')


# # Для проверки.
# vector3D = RadiusVector(3)
# vector3D.set_coords(3, -5.6, 8)
# a, b, c = vector3D.get_coords()
# vector3D.set_coords(3, -5.6, 8, 10,11)  # ошибки быть не должно, последние две координаты игнорируются
# vector3D.set_coords(1,2)  # ошибки быть не должно, меняются только первые две координаты
# res_len = len(vector3D)  # res_len = 3
# res_abs = abs(vector3D)
#
# print(res_len)
# print(res_abs)
