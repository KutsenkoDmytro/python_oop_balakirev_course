'''
Подвиг 9. (task_5.py)

В программе необходимо реализовать таблицу TableValues по следующей схеме:

Table

Каждая ячейка таблицы должна быть представлена классом Cell. Объекты этого класса создаются командой:

cell = Cell(data)
где data - данные в ячейке. В каждом объекте класса Cell должен формироваться локальный приватный атрибут __data с соответствующим значением. Для работы с ним в классе Cell должно быть объект-свойство (property):

data - для записи и считывания информации из атрибута __data.

Сам класс TableValues представляет таблицу в целом, объекты которого создаются командой:

table = TableValues(rows, cols, type_data)
где rows, cols - число строк и столбцов таблицы; type_data - тип данных ячейки (int - по умолчанию, float, list, str и т.п.). Начальные значения в ячейках таблицы равны 0 (целое число).

С объектами класса TableValues должны выполняться следующие команды:

table[row, col] = value# запись нового значения в ячейку с индексами row, col (индексы отсчитываются с нуля)
value = table[row, col] # считывание значения из ячейки с индексами row, col

for row in table:  # перебор по строкам
    for value in row: # перебор по столбцам
        print(value, end=' ')  # вывод значений ячеек в консоль
    print()
При попытке записать по индексам table[row, col] данные другого типа (не совпадающего с атрибутом type_data объекта класса TableValues), должно генерироваться исключение командой:

raise TypeError('неверный тип присваиваемых данных')
При работе с индексами row, col, необходимо проверять их корректность. Если индексы не целое число или они выходят за диапазон размера таблицы, то генерировать исключение командой:

raise IndexError('неверный индекс')
P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.

'''


class Cell:

    def __init__(self, data):
        self.__data = data


    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value


class TableValues:

    def __init__(self, rows, cols, type_data=int):
        self.rows = rows
        self.cols = cols
        self.type_data = type_data
        self.cells = [[Cell(0) for j in range(cols)] for i in range(rows)]

    def __getitem__(self, item):
        r, c = item
        self.__check_indx(r,c)
        return self.cells[r][c].data

    def __setitem__(self, key, value):
        r, c = key
        self.__check_indx(r, c)
        self.__check_val(value)
        self.cells[r][c].data = value

    def __check_indx(self, row, col):
        if not (isinstance(row, int) and isinstance(col, int) and
                -self.rows <= row < self.rows and -self.cols <= col < self.cols):
            raise IndexError('неверный индекс')

    def __check_val(self,value):
        if not self.type_data is type(value):
            raise TypeError('неверный тип присваиваемых данных')

    def __iter__(self):
        self.r = 0
        return self

    def __next__(self):
        if self.r < len(self.cells):
            r_old = [i.data for i in self.cells[self.r]]
            self.r += 1
            return iter(r_old)
        else:
            raise StopIteration


# Для проверки.
table = TableValues(4, 4, str)
table[0, 0] = 'data_00' # запись нового значения в ячейку с индексами row, col (индексы отсчитываются с нуля)
value = table[0, 0]
for row in table:  # перебор по строкам
    for value in row: # перебор по столбцам
        print(value, end=' ')  # вывод значений ячеек в консоль
    print()

