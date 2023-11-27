'''
Объявите два класса:

Cell - для представления клетки игрового поля;
GamePole - для управления игровым полем, размером N x N клеток.

С помощью класса Cell предполагается создавать отдельные клетки командой:

c1 = Cell(around_mines, mine)
Здесь around_mines - число мин вокруг данной клетки поля; mine - булева величина (True//False),
означающая наличие мины в текущей клетке. При этом, в каждом объекте класса Cell должны создаваться локальные свойства:

around_mines - число мин вокруг клетки (начальное значение 0);
mine - наличие/отсутствие мины в текущей клетке (True//False);
fl_open - открыта/закрыта клетка - булево значение (True//False). Изначально все клетки закрыты (False).

С помощью класса GamePole должна быть возможность создавать квадратное игровое поле с числом клеток N x N:

pole_game = GamePole(N, M)
Здесь N - размер поля; M - общее число мин на поле. При этом, каждая клетка
представляется объектом класса Cell и все объекты хранятся в двумерном списке N x N элементов - локальном свойстве pole объекта класса GamePole.

В классе GamePole должны быть также реализованы следующие методы:

init() - инициализация поля с новой расстановкой M мин (случайным образом по игровому полю,
разумеется каждая мина должна находиться в отдельной клетке).
show() - отображение поля в консоли в виде таблицы чисел открытых клеток (если клетка не открыта,
то отображается символ #; мина отображается символом *; между клетками при отображении ставить пробел).

При создании экземпляра класса GamePole в его инициализаторе следует вызывать метод init() для первоначальной инициализации игрового поля.
В классе GamePole могут быть и другие вспомогательные методы.

Создайте экземпляр pole_game класса GamePole с размером поля N = 10 и числом мин M = 12.

'''
import random

class Cell:
    '''Представления клетки игрового поля.'''

    def __init__(self, around_mines, mine):
        self.around_mines = 0 if not around_mines else around_mines
        self.mine = mine
        self.fl_open = False

class GamePole:
    '''Cоздает квадратное игровое поле с числом клеток N x N'''

    def __init__(self, N, M):
        self.N = N
        self.M = M
        mines_in_cell = [True if m < M else False for m in range(N*N)]
        random.shuffle(mines_in_cell)
        gen_m = (m for m in mines_in_cell)

        self.pole = [[Cell(0,
                           next(gen_m)) for j in range(N)] for i in range(N)]
        self.get_around_mines()

    def get_around_mines(self):
        '''Устанавливает значение атрибута around_mines для каждой ячейки поля.'''
        pole = self.pole
        for i, vi in enumerate(pole):
            if i == 0:
                # если первый элемент двумерного списка.
                for j, vj in enumerate(vi):
                    if j == 0:
                        lst_around_obj = [pole[i][j+1],*pole[i+1][j:j+2]]
                        vj.around_mines =  sum([1 for obj in lst_around_obj if obj.mine == True])
                    elif j == len(vi)-1:
                        lst_around_obj = [pole[i][j-1], *pole[i + 1][j-1:]]
                        vj.around_mines = sum(
                            [1 for obj in lst_around_obj if obj.mine == True])
                    else:
                         lst_around_obj = [pole[i][j-1], pole[i][j+1], *pole[i+1][j-1:j+2]]
                         vj.around_mines = sum(
                             [1 for obj in lst_around_obj if obj.mine == True])
            elif i == len(pole)-1:
                # если последний элемент двухмерного списка.
                for j, vj in enumerate(vi):
                    if j == 0:
                        lst_around_obj = [pole[i][j+1],*pole[i-1][j:j+2]]
                        vj.around_mines =  sum([1 for obj in lst_around_obj if obj.mine == True])
                    elif j == len(vi)-1:
                        lst_around_obj = [pole[i][j-1], *pole[i - 1][j-1:]]
                        vj.around_mines = sum(
                            [1 for obj in lst_around_obj if obj.mine == True])
                    else:
                         lst_around_obj = [pole[i][j-1], pole[i][j+1], *pole[i-1][j-1:j+2]]
                         vj.around_mines = sum(
                             [1 for obj in lst_around_obj if obj.mine == True])
            else:
                # если средний элемент двумерного списка.
                for j, vj in enumerate(vi):
                    if j == 0:
                        lst_around_obj = [pole[i][j+1],*pole[i+1][j:j+2],*pole[i-1][j:j+2]]
                        vj.around_mines =  sum([1 for obj in lst_around_obj if obj.mine == True])
                    elif j == len(vi)-1:
                        lst_around_obj = [pole[i][j-1],*pole[i + 1][j-1:], *pole[i - 1][j-1:]]
                        vj.around_mines = sum(
                            [1 for obj in lst_around_obj if obj.mine == True])
                    else:
                         lst_around_obj = [pole[i][j-1], pole[i][j+1],*pole[i+1][j-1:j+2], *pole[i-1][j-1:j+2]]
                         vj.around_mines = sum(
                             [1 for obj in lst_around_obj if obj.mine == True])

    def open_or_close_cells(self, open = False):
        '''Открывает или закрывает все ячейки.'''
        for lst in self.pole:
            for cell in lst:
                cell.fl_open = open

    def show(self):
        '''Отображает поле в зависимости от значений атрибутов
        ячеек fl_open, mine, around_mines'''
        for lst in self.pole:
            lst_print = list()
            for cell in lst:
                if cell.fl_open == False:
                    lst_print.append('#')
                elif cell.mine == True:
                    lst_print.append('*')
                else:
                    lst_print.append(cell.around_mines)
            print(*lst_print,'\n')


pole_game = GamePole(10, 12)
pole_game.show()
print("==============================")
pole_game.open_or_close_cells(True)
pole_game.show()

