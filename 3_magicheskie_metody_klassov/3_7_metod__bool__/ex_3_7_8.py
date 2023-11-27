'''
Большой подвиг 8. (task_5.py)

Вы начинаете разрабатывать игру "Сапер". Для этого вам нужно уметь представлять и управлять игровым полем. Будем полагать, что оно имеет размеры N x M клеток. Каждая клетка будет представлена объектом класса Cell и содержать либо число мин вокруг этой клетки, либо саму мину.

SaperPole

Для начала в программе объявите класс GamePole, который будет создавать и управлять игровым полем. Объект этого класса должен формироваться командой:

pole = GamePole(N, M, total_mines)
И, так как поле в игре одно, то нужно контролировать создание только одного объекта класса GamePole (используйте паттерн Singleton, о котором мы с вами говорили, когда рассматривали магический метод new()).

Объект pole должен иметь локальный приватный атрибут:

__pole_cells - двумерный (вложенный) кортеж, размерами N x M элементов (N строк и M столбцов), состоящий из объектов класса Cell.

Для доступа к этой коллекции объявите в классе GamePole объект-свойство (property):

pole - только для чтения (получения) ссылки на коллекцию __pole_cells.

Далее, в самом классе GamePole объявите следующие методы:

init_pole() - для инициализации начального состояния игрового поля (расставляет мины и делает все клетки закрытыми);
open_cell(i, j) - открывает ячейку с индексами (i, j); нумерация индексов начинается с нуля; метод меняет значение атрибута __is_open объекта Cell в ячейке (i, j) на True;
show_pole() - отображает игровое поле в консоли (как именно сделать - на ваше усмотрение, этот метод - домашнее задание).

Расстановку мин выполняйте случайным образом по игровому полю (для этого удобно воспользоваться функцией randint модуля random). После расстановки всех total_mines мин, вычислите их количество вокруг остальных клеток (где нет мин). Область охвата - соседние (прилегающие) клетки (8 штук).

В методе open_cell() необходимо проверять корректность индексов (i, j). Если индексы указаны некорректно, то генерируется исключение командой:

raise IndexError('некорректные индексы i, j клетки игрового поля')
Следующий класс Cell описывает состояние одной ячейки игрового поля. Объекты этого класса создаются командой:

cell = Cell()
При этом в самом объекте создаются следующие локальные приватные свойства:

__is_mine - булево значение True/False; True - в клетке находится мина, False - мина отсутствует;
__number - число мин вокруг клетки (целое число от 0 до 8);
__is_open - флаг того, открыта клетка или закрыта: True - открыта; False - закрыта.

Для работы с этими приватными атрибутами объявите в классе Cell следующие объекты-свойства с именами:

is_mine - для записи и чтения информации из атрибута __is_mine;
number - для записи и чтения информации из атрибута __number;
is_open - для записи и чтения информации из атрибута __is_open.

В этих свойствах необходимо выполнять проверку на корректность переданных значений (либо булево значение True/False, либо целое число от 0 до 8). Если передаваемое значение некорректно, то генерировать исключение командой:

raise ValueError("недопустимое значение атрибута")
С объектами класса Cell должна работать функция:

bool(cell)
которая возвращает True, если клетка закрыта и False - если открыта.

Пример использования классов (эти строчки в программе писать не нужно):

pole = GamePole(10, 20, 10)  # создается поле размерами 10x20 с общим числом мин 10
pole.init_pole()
if pole.pole[0][1]:
    pole.open_cell(0, 1)
if pole.pole[3][5]:
    pole.open_cell(3, 5)
pole.open_cell(30, 100)  # генерируется исключение IndexError
pole.show_pole()
P.S. В программе на экран выводить ничего не нужно, только объявить классы.

'''

from random import randint


class Cell:
    '''Описывает клетку игрового поля.'''

    def __init__(self):
        self.__is_mine = False
        self.__number = 0
        self.__is_open = False

    @property
    def is_mine(self):
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, value):
        if not type(value) is bool:
            self.get_error_msg()
        self.__is_mine = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        if type(value) in {int, str} and 0 <= value <= 8:
            self.__number = value
        else:
            self.get_error_msg()

    @property
    def is_open(self):
        return self.__is_open

    @is_open.setter
    def is_open(self, value):
        if not type(value) is bool:
            self.get_error_msg()
        self.__is_open = value

    @staticmethod
    def get_error_msg():
        raise ValueError("недопустимое значение атрибута")

    def __bool__(self):
        return not self.is_open


class GamePole:
    '''Описывает игровое поле.'''
    Single_object = None

    def __new__(cls, *args, **kwargs):
        if not cls.Single_object:
            cls.Single_object = super().__new__(cls)
        return cls.Single_object

    def __init__(self, N, M, total_mines):
        self.N = N
        self.M = M
        self.total_mines = total_mines
        self.__pole_cells = [[Cell() for i in range(M)] for j in range(N)]

    @property
    def pole(self):
        return self.__pole_cells

    def init_pole(self):
        '''расставляет мины и делает все клетки закрытыми.'''

        mines = self.total_mines
        pole = self.pole
        # Ложим мины в ячейки игрового поля.
        while mines > 0:
            x = randint(0,self.N-1) #Вычисляем строку поля.
            y = randint(0,self.M-1) #Вычисляем столбец поля.
            if not pole[x][y].is_mine: #Если в случайной ячейке нету мины - ложим мину.
                pole[x][y].is_mine = True
                mines -=1
        # Закрываем все ячейки игрового поля.
        for n in pole:
            for m in n:
                m.is_open = False

        # Суммируем количество мин в соседних ячейках.
        def check_neibh(x, y):
            try:
                return pole[x][y].is_mine
            except IndexError:
                return 0

        for i_n,n in enumerate(pole):
            for i_m, m in enumerate(n): # Проверяем соседей выше, слева, справа и внизу от ячейки.
                if i_n == 0:
                    val = (check_neibh(i_n,i_m - 1) if i_m !=0 else 0) + check_neibh(i_n,i_m + 1)+ \
                          (check_neibh(i_n + 1,i_m - 1) if i_m !=0 else 0) + check_neibh(i_n + 1,i_m) + check_neibh(i_n + 1,i_m + 1)
                elif i_n == len(pole)-1:
                    val = check_neibh(i_n - 1,i_m - 1) + check_neibh(i_n - 1,i_m) + check_neibh(i_n - 1,i_m + 1) + \
                          check_neibh(i_n,i_m - 1) + check_neibh(i_n,i_m + 1)
                else:
                    val = check_neibh(i_n-1,i_m-1) + check_neibh(i_n-1,i_m)+ check_neibh(i_n-1,i_m+1)+ \
                               check_neibh(i_n,i_m - 1) + check_neibh(i_n,i_m + 1)+ \
                               check_neibh(i_n + 1,i_m - 1) + check_neibh(i_n + 1,i_m) + check_neibh(i_n + 1,i_m + 1)

                m.number = val

    def open_cell(self, i, j):
        '''открывает ячейку с индексами (i, j).'''
        try:
            self.pole[i][j].is_open = True
        except:
            raise IndexError('некорректные индексы i, j клетки игрового поля')

    def show_pole(self):
        '''отображает игровое поле в консоли.'''
        for row in self.pole:
            for cell in row:
                if cell.is_open:
                    if cell.is_mine:
                        chart = '*'
                    else:
                        chart = cell.number
                else:
                    chart = '#'
                print(chart,end=' ')
            print()

    def __del__(self):
        self.__class__.Single_object = None



pole = GamePole(10,20, 10)  # создается поле размерами 10x20 с общим числом мин 10
pole.init_pole()
if pole.pole[0][1]:
    pole.open_cell(0, 1)
if pole.pole[3][5]:
    pole.open_cell(3, 5)
#pole.open_cell(30, 100)  # генерируется исключение IndexError
pole.show_pole()

print('========================')
#Для проверки:
for i in pole.pole:
    for j in i:
        j.is_open = True
pole.show_pole()

