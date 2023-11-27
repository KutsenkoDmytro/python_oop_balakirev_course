'''
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/eKxzgkKD1fI

Подвиг 9. Объявите в программе класс Triangle, объекты которого создаются командой:

tr = Triangle(a, b, c)

где a, b, c - длины сторон треугольника (любые положительные числа). В каждом объекте класса Triangle должны формироваться локальные атрибуты _a, _b, _c с соответствующими значениями.

Если в качестве хотя бы одной величины a, b, c передается не числовое значение, или меньше либо равно нулю, то должно генерироваться исключение командой:

raise TypeError('стороны треугольника должны быть положительными числами')

Если из переданных значений a, b, c нельзя составить треугольник (условие: каждая сторона должна быть меньше суммы двух других), то генерировать исключение командой:

raise ValueError('из указанных длин сторон нельзя составить треугольник')

Затем, на основе следующего набора данных:

input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]

необходимо сформировать объекты класса Triangle, но только в том случае, если не возникло никаких исключений. Все созданные объекты представить в виде списка с именем lst_tr.

P.S. В программе нужно только сформировать список lst_tr. На экран ничего выводить не нужно.Memory limit: 256 MBTime limit: 15 seconds


'''

# class Triangle_desc:
#     '''Дескриптор класса Triangle'''
#
#     def __set_name__(self, owner, name):
#         self.name = '_'+name
#
#     def __get__(self, instance, owner):
#         return getattr(instance,self.name)
#
#     def __set__(self, instance, value):
#         if not (type(value) in (int,float) and value > 0):
#             raise TypeError('стороны треугольника должны быть положительными числами')
#         setattr(instance,self.name, value)


class Triangle:

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    def __setattr__(self, key, value):
        if key in {'_a', '_b', '_c'}:
            self.__check_value(value)

            st_attrs = set(self.__dict__.keys())
            if (key == '_a' and {'_b','_c'} <= st_attrs):
                a, b, c = value, self._b, self._c
            elif (key == '_b' and {'_a','_c'} <= st_attrs):
                a, b, c = self._a, value, self._c
            elif (key == '_c' and {'_a', '_b'} <= st_attrs):
                a, b, c = self._a, self._b, value
            else:
                return super().__setattr__(key, value)
            if a > b + c or b > a + c or c > b + a:
                raise ValueError('из указанных длин сторон нельзя составить треугольник')

        return super().__setattr__(key, value)

    @staticmethod
    def __check_value(value):
        if not (type(value) in (int, float) and value > 0):
            raise TypeError('стороны треугольника должны быть положительными числами')




input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]
lst_tr = []
for obj in input_data:
    try:
        tr = Triangle(*obj)
        lst_tr.append(tr)
    except:
        pass
        #print(f"Ошибка при создании треугольника: {obj}")

print(lst_tr)
