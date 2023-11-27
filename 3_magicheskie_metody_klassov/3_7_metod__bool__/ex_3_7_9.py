'''
Подвиг 9 (на повторение). (task_6.py)

Объявите в программе класс Vector, объекты которого создаются командой:

v = Vector(x1, x2, x3,..., xN)
где x1, x2, x3,..., xN - координаты вектора (числа: целые или вещественные).

С каждым объектом класса Vector должны выполняться операторы:

v1 + v2 # суммирование соответствующих координат векторов
v1 - v2 # вычитание соответствующих координат векторов
v1 * v2 # умножение соответствующих координат векторов

v1 += 10 # прибавление ко всем координатам вектора числа 10
v1 -= 10 # вычитание из всех координат вектора числа 10
v1 += v2
v2 -= v1

v1 == v2 # True, если соответствующие координаты векторов равны
v1 != v2 # True, если хотя бы одна пара координат векторов не совпадает
При реализации бинарных операторов +, -, * следует создавать новые объекты класса Vector с новыми (вычисленными) координатами. При реализации операторов +=, -= координаты меняются в текущем объекте, не создавая новый.

Если число координат (размерность) векторов v1 и v2 не совпадает, то при операторах +, -, * должно генерироваться исключение командой:

raise ArithmeticError('размерности векторов не совпадают')
P.S. В программе на экран выводить ничего не нужно, только объявить класс.

'''


class Vector:

    def __init__(self, *args):
        self.coords = list(args) if args else []

    def __add__(self, other):
        self.__check_obj(other)
        self.__check_dimension(other)
        new_coords = [v[0] + v[1] for v in zip(self.coords, other.coords)]
        return self.__class__(*new_coords)

    def __iadd__(self, other):
        if type(other) in {int, float, self.__class__}:
            if type(other) is self.__class__:
                self.__check_dimension(other)
                new_coords = [v[0] + v[1] for v in
                              zip(self.coords, other.coords)]
            else:
                new_coords = [v + other for v in self.coords]
            self.coords = new_coords
            return self
        else:
            raise ValueError('не верный тип данных')

    def __sub__(self, other):
        self.__check_obj(other)
        self.__check_dimension(other)
        new_coords = [v[0] - v[1] for v in zip(self.coords, other.coords)]
        return self.__class__(*new_coords)

    def __isub__(self, other):
        if type(other) in {int, float, self.__class__}:
            if type(other) is self.__class__:
                self.__check_dimension(other)
                new_coords = [v[0] - v[1] for v in
                              zip(self.coords, other.coords)]
            else:
                new_coords = [v - other for v in self.coords]
            self.coords = new_coords
            return self
        else:
            raise ValueError('не верный тип данных')

    def __mul__(self, other):
        self.__check_obj(other)
        self.__check_dimension(other)
        new_coords = [v[0] * v[1] for v in zip(self.coords, other.coords)]
        return self.__class__(*new_coords)

    def __len__(self):
        return len(self.coords)

    def __eq__(self, other):
        self.__check_obj(other)
        return self.coords == other.coords

    def __check_dimension(self, other):
        if len(self) != len(other):
            raise ArithmeticError('размерности векторов не совпадают')

    @classmethod
    def __check_obj(cls, other):
        if not isinstance(other, cls):
            raise ValueError('не верный тип данных')


# Test
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print((v1 + v2).coords)
print((v1 - v2).coords)
print((v1 * v2).coords)

v1 += 10
print(v1.coords)
v1 -= 10
print(v1.coords)
v1 += v2
print(v1.coords)
v2 -= v1
print(v2.coords)


print(v1 == v2)
print(v1 != v2)
