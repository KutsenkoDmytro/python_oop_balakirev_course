'''
Подвиг 10 (на повторение). (task_6.py)

Объявите класс с именем Triangle, объекты которого создаются командой:

tr = Triangle(a, b, c)
где a, b, c - длины сторон треугольника (числа: целые или вещественные). В классе Triangle объявите следующие дескрипторы данных:

a, b, c - для записи и считывания длин сторон треугольника.

При записи нового значения нужно проверять, что присваивается положительное число (целое или вещественное). Иначе, генерируется исключение командой:

raise ValueError("длины сторон треугольника должны быть положительными числами")
Также нужно проверять, что все три стороны a, b, c могут образовывать стороны треугольника. То есть, должны выполняться условия:

a < b+c; b < a+c; c < a+b

Иначе генерируется исключение командой:

raise ValueError("с указанными длинами нельзя образовать треугольник")
Наконец, с объектами класса Triangle должны выполняться функции:

len(tr) - возвращает периметр треугольника, приведенный к целому значению с помощью функции int();
tr() - возвращает площадь треугольника (можно вычислить по формуле Герона: s = sqrt(p * (p-a) * (p-b) * (p-c)), где p - полупериметр треугольника).

P.S. На экран ничего выводить не нужно, только объявить класс Triangle.

'''

from math import sqrt


class Triangle_Descr:

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class Triangle:
    a = Triangle_Descr()
    b = Triangle_Descr()
    c = Triangle_Descr()

    def __init__(self, a, b, c):
        for i in [a, b, c]:
            self.check_pos_num(i)
        self.check_is_triangle(a, b, c)
        self.a = a
        self.b = b
        self.c = c

    def __setattr__(self, key, value):
        if {'_a', '_b', '_c'} <= set(self.__dict__.keys()):
            if key == 'a':
                self.check_pos_num(value)
                self.check_is_triangle(value, self.b, self.c)
            elif key == 'b':
                self.check_pos_num(value)
                self.check_is_triangle(self.a, value, self.c)
            elif key == 'c':
                self.check_pos_num(value)
                self.check_is_triangle(self.a, self.b, value)
        object.__setattr__(self, key, value)

    def __len__(self):
        '''Возвращает периметр треугольника.'''
        return int(self.a + self.b + self.c)

    def __call__(self, *args, **kwargs):
        '''Возвращает площадь треугольника.'''
        p = (self.a + self.b + self.c) / 2  # Либо len(self) / 2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    @staticmethod
    def check_pos_num(value):
        if not (isinstance(value, (int, float)) and value > 0):
            raise ValueError(
                "длины сторон треугольника должны быть положительными числами")

    @staticmethod
    def check_is_triangle(a, b, c):
        if a > b + c or b > a + c or c > a + b:
            raise ValueError(
                "с указанными длинами нельзя образовать треугольник")


# Для проверки.
tr = Triangle(3, 5, 4)
tr.a = 5
pp = len(tr)
print(tr())

print(tr.__dict__)
print(pp)
