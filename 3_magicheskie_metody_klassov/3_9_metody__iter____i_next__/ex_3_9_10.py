'''
Подвиг 10 (на повторение). (task_6.py)

Объявите класс Matrix (матрица) для операций с матрицами. Объекты этого класса должны создаваться командой:

m1 = Matrix(rows, cols, fill_value)
где rows, cols - число строк и столбцов матрицы; fill_value - заполняемое начальное значение элементов матрицы (должно быть число: целое или вещественное). Если в качестве аргументов передаются не числа, то генерировать исключение:

raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
Также объекты можно создавать командой:

m2 = Matrix(list2D)
где list2D - двумерный список (прямоугольный), состоящий из чисел (целых или вещественных). Если список list2D не прямоугольный, или хотя бы один из его элементов не число, то генерировать исключение командой:

raise TypeError('список должен быть прямоугольным, состоящим из чисел')
Для объектов класса Matrix должны выполняться следующие команды:

matrix = Matrix(4, 5, 0)
res = matrix[0, 0] # возвращается первый элемент матрицы
matrix[indx1, indx2] = value # элементу матрицы с индексами (indx1, indx2) присваивается новое значение
Если в результате присвоения тип данных не соответствует числу, то генерировать исключение командой:

raise TypeError('значения матрицы должны быть числами')
Если указываются недопустимые индексы матрицы (должны быть целыми числами от 0 и до размеров матрицы), то генерировать исключение:

raise IndexError('недопустимые значения индексов')
Также с объектами класса Matrix должны выполняться операторы:

matrix = m1 + m2 # сложение соответствующих значений элементов матриц m1 и m2
matrix = m1 + 10 # прибавление числа ко всем элементам матрицы m1
matrix = m1 - m2 # вычитание соответствующих значений элементов матриц m1 и m2
matrix = m1 - 10 # вычитание числа из всех элементов матрицы m1
Во всех этих операция должна формироваться новая матрица с соответствующими значениями. Если размеры матриц не совпадают (разные хотя бы по одной оси), то генерировать исключение командой:

raise ValueError('операции возможны только с матрицами равных размеров')
Пример для понимания использования индексов (эти строчки в программе писать не нужно):

mt = Matrix([[1, 2], [3, 4]])
res = mt[0, 0] # 1
res = mt[0, 1] # 2
res = mt[1, 0] # 3
res = mt[1, 1] # 4
P.S. В программе нужно объявить только класс. Выводить на экран ничего не нужно.

'''

#МАТРИЦЫ


class Matrix:

    def __init__(self, *args):
        if len(args) == 1 and type(args[0]) is list:
            self.__check_list2D(args[0])
            list2D = args[0]
        else:
            if not self.__check_params_list2D(args[0], args[1], args[2]):
                raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
            list2D = [[args[2] for c in range(args[1])] for r in range(args[0])]
        self.list2D = list2D

    def get_params_list2D(self):
        '''Возвращает кортежем количество строк и столбцов матрицы (rows,cols)'''
        return (len(self.list2D), len(self.list2D[0]))

    def __check_list2D(self, value: list):
        '''Проверяет переданный двумерный список на корректность формы и значений.'''
        if not all(map(lambda c: type(c) in {int, float},
                       [c for r in value for c in r])) or not \
                len({len(i) for i in value}) <= 1:
            raise TypeError(
                'список должен быть прямоугольным, состоящим из чисел')

    def __check_params_list2D(self, x, y, val):
        '''Проверяет тип переданых значений (строки, столбца, значения).'''
        return {type(x), type(y)} == {int} and type(val) in {int, float}

    def __check_indx(self, row, col):
        '''Проверяет корректность индексов.'''
        lst_rows, lst_cols = self.get_params_list2D()
        if not type(row) is int or not type(col) is int or \
                not 0 <= row < lst_rows or \
                not 0 <= col < lst_cols:
            raise IndexError('недопустимые значения индексов')

    def __check_val(self, val):
        '''Проверяет передаваемое значение елемента матрицы.'''
        if not type(val) in {int, float}:
            raise TypeError('значения матрицы должны быть числами')

    def __check_dimensions(self, obj):
        '''Проверить на разность размеров матриц.'''
        if self.get_params_list2D() != obj.get_params_list2D():
            raise ValueError(
                'операции возможны только с матрицами равных размеров')

    def __getitem__(self, item):
        r, c = item
        self.__check_indx(r, c)
        return self.list2D[r][c]

    def __setitem__(self, key, value):
        r, c = key
        self.__check_indx(r, c)
        self.__check_val(value)
        self.list2D[r][c] = value

    def __add__(self, other):
        if type(other) is int:
            list2D_new = [[c + other for c in r] for r in self.list2D]
            return self.__class__(list2D_new)
        elif isinstance(other, self.__class__):
            self.__check_dimensions(other)

            lst_rows, lst_cols = self.get_params_list2D()
            lst_obj1 = self.list2D
            lst_obj2 = other.list2D
            list2D_new = [[lst_obj1[r][c] + lst_obj2[r][c] \
                           for c in range(lst_cols)] for r in range(lst_rows)]
            return self.__class__(list2D_new)

    def __sub__(self, other):
        if type(other) is int:
            list2D_new = [[c - other for c in r] for r in self.list2D]
            return self.__class__(list2D_new)
        elif isinstance(other, self.__class__):
            self.__check_dimensions(other)

            lst_rows, lst_cols = self.get_params_list2D()
            lst_obj1 = self.list2D
            lst_obj2 = other.list2D
            list2D_new = [[lst_obj1[r][c] - lst_obj2[r][c] \
                           for c in range(lst_cols)] for r in range(lst_rows)]
            return self.__class__(list2D_new)

    def draw_list2D(self):
        '''Выводит матрицу в консоль.'''
        for r in self.list2D:
            for c in r:
                print(c, end=' ')
            print()



# Для проверки.
m1 = Matrix(3, 3, 5)
m1.draw_list2D()
m2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('=============')
m2.draw_list2D()
print('=============')
res = m1[0, 0]
print(res)
print('=============')
m1[0, 0] = 1
m1.draw_list2D()
print('=============')
matrix1 = m1 + m2
matrix1.draw_list2D()
print('=============')
matrix2 = m1 + 10
matrix2.draw_list2D()
print('=============')
matrix3 = m1 - m2
matrix3.draw_list2D()
print('=============')
matrix4 = m1 - 10
matrix4.draw_list2D()




