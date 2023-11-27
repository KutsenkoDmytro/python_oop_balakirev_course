'''
Подвиг 9 (релакс). (task_5.py)

Объявите класс с именем Dimensions, объекты которого создаются командой:

d = Dimensions(a, b, c)
где a, b, c - положительные числа (целые или вещественные), описывающие габариты некоторого тела: высота, ширина и глубина.

Каждый объект класса Dimensions должен иметь аналогичные публичные атрибуты a, b, c (с соответствующими числовыми значениями). Также для каждого объекта должен вычисляться хэш на основе всех трех габаритов: a, b, c.

С помощью функции input() прочитайте из входного потока строку, записанную в формате:

"a1 b1 c1; a2 b2 c2; ... ;aN bN cN"

Например:

"1 2 3; 4 5 6.78; 1 2 3; 0 1 2.5"

Если какой-либо габарит оказывается отрицательным значением или равен нулю, то при создании объектов должна генерироваться ошибка командой:

raise ValueError("габаритные размеры должны быть положительными числами")
Сформируйте на основе прочитанной строки список lst_dims из объектов класса Dimensions. После этого отсортируйте этот список по возрастанию (неубыванию) хэшей этих объектов так, чтобы объекты с равными хэшами стояли друг за другом.

P.S. На экран ничего выводить не нужно.

Sample Input:

1 2 3; 4 5 6.78; 1 2 3; 3 1 2.5
Sample Output:

'''


class Dimensions:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def __check_pos_num(value):
        if not (isinstance(value, (int, float)) and value > 0):
            raise ValueError(
                "габаритные размеры должны быть положительными числами")

    def __setattr__(self, key, value):
        if key in {'a', 'b', 'c'}:
            self.__check_pos_num(value)
        object.__setattr__(self, key, value)

    def __hash__(self):
        return hash((self.a, self.b, self.c))

    def __eq__(self, other):
        return hash(self) == hash(other)


st = '1 2 3; 4 5 6.78; 1 2 3; 3 1 2.5'
get_num = lambda x: int(x) if x.isdigit() else float(x)
lst = [s.split() for s in st.split('; ')]

lst_attrs = []
for i in lst:
    lst = []
    for j in i:
        lst.append(get_num(j))
    lst_attrs.append(lst)

lst_dims = [Dimensions(a[0], a[1], a[2]) for a in lst_attrs]
lst_dims = sorted(lst_dims, key=lambda x: hash(x))


# Для проверки.
print(lst_dims)
print('============')
print([hash(obj) for obj in lst_dims])

