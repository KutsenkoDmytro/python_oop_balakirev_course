'''
Подвиг 10. (task_9.py)

Вам необходимо описывать в программе очень большие и разреженные таблицы данных (с большим числом пропусков). Для этого предлагается объявить класс SparseTable, объекты которого создаются командой:

st = SparseTable()
В каждом объекте этого класса должны создаваться локальные публичные атрибуты:

rows - общее число строк таблицы (начальное значение 0);
cols - общее число столбцов таблицы (начальное значение 0).

В самом классе SparseTable должны быть объявлены методы:

add_data(row, col, data) - добавление данных data (объект класса Cell) в таблицу по индексам row, col (целые неотрицательные числа);
remove_data(row, col) - удаление ячейки (объект класса Cell) с индексами (row, col).

При удалении/добавлении новой ячейки должны автоматически пересчитываться атрибуты rows, cols объекта класса SparseTable. Если происходит попытка удалить несуществующую ячейку, то должно генерироваться исключение:

raise IndexError('ячейка с указанными индексами не существует')
Ячейки таблицы представляют собой объекты класса Cell, которые создаются командой:

data = Cell(value)
где value - данные ячейки (любой тип).

Хранить ячейки следует в словаре, ключами которого являются индексы (кортеж) i, j, а значениями - объекты класса Cell.

Также с объектами класса SparseTable должны выполняться команды:

res = st[i, j] # получение данных из таблицы по индексам (i, j)
st[i, j] = value # запись новых данных по индексам (i, j)
Чтение данных возможно только для существующих ячеек. Если ячейки с указанными индексами нет, то генерировать исключение командой:

raise ValueError('данные по указанным индексам отсутствуют')
При записи новых значений их следует менять в существующей ячейке или добавлять новую, если ячейка с индексами (i, j) отсутствует в таблице. (Не забывайте при этом пересчитывать атрибуты rows и cols).

Пример использования классов (эти строчки в программе не писать):

st = SparseTable()
st.add_data(2, 5, Cell("cell_25"))
st.add_data(0, 0, Cell("cell_00"))
st[2, 5] = 25 # изменение значения существующей ячейки
st[11, 7] = 'cell_117' # создание новой ячейки
print(st[0, 0]) # cell_00
st.remove_data(2, 5)
print(st.rows, st.cols) # 12, 8 - общее число строк и столбцов в таблице
val = st[2, 5] # ValueError
st.remove_data(12, 3) # IndexError
P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.


'''
#БОЛЬШИЕ И РАЗРЕЖЕННЫЕ ТАБЛИЦЫ ДАННЫХ (С БОЛЬШИМ ЧИСЛОМ ПРОПУСКОВ)

class Cell:

    def __init__(self, value):
        self.value = value


class SparseTable:

    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.cells = {}

    def __recalc_params(self):
        '''Пересчитывает строки и столбцы таблицы.'''
        # При удалении или записи нужно искать максимальные значения
        # значения строки и столбца (в кортежах словаря)
        cells_params = list(
            zip(*self.cells.keys()))  # Переобразовываем существующий список в список состоящий из 2х элементов (кортежей): 0-значения строк, 1-значения столбцов.
        self.rows = max(cells_params[0]) + 1
        self.cols = max(cells_params[1]) + 1

    def add_data(self, row, col, data):
        self.cells[(row, col)] = data
        self.__recalc_params()

    def remove_data(self, row, col):
        if not self.__check_indx(row, col):
            raise IndexError('ячейка с указанными индексами не существует')
        self.cells.pop((row, col))
        self.__recalc_params()

    def __getitem__(self, item):
        row, col = item
        if not self.__check_indx(row, col):
            raise ValueError('данные по указанным индексам отсутствуют')
        return self.cells[(row, col)].value

    def __setitem__(self, key, value):
        row, col = key
        if not self.__check_indx(row,col):  # Если нет ключа, создается новый объект и делается запись в словарь.
            self.cells[(row, col)] = Cell(value)
            self.__recalc_params()
        else:
            self.cells[(row,col)].value = value  # Иначе изменяем данные в существующем объекте.

    def __check_indx(self, row, col):
        '''Проверка на наличие ключа (кортежа) в словаре.'''
        return False if self.cells.get((row, col), False) == False else True


# Для проверки.
st = SparseTable()
st.add_data(2, 5, Cell("cell_25"))
st.add_data(0, 0, Cell("cell_00"))
st[2, 5] = 25  # изменение значения существующей ячейки
st[11, 7] = 'cell_117'  # создание новой ячейки
print(st[0, 0])  # cell_00
st.remove_data(2, 5)
print(st.rows, st.cols)  # 12, 8 - общее число строк и столбцов в таблице
# val = st[2, 5] # ValueError
# st.remove_data(12, 3) # IndexError

