'''
Испытание магией
Видео-разбор (решение смотреть только после своей попытки): https://youtu.be/1dSxnEFfDu8

Вы прошли магические методы. Начальство оценило вашу стойкость, рвение и решило дать вам испытание для подтверждения уровня полученных навыков. Вам выпала великая честь создать полноценную программу игры в "Крестики-нолики". И вот перед вами текст с заданием самого испытания.

Техническое задание
Необходимо объявить класс с именем TicTacToe (крестики-нолики) для управления игровым процессом. Объекты этого класса будут создаваться командой:

game = TicTacToe()
В каждом объекте этого класса должен быть публичный атрибут:

pole - двумерный кортеж, размером 3x3.

Каждый элемент кортежа pole является объектом класса Cell:

cell = Cell()
В объектах этого класса должно автоматически формироваться локальное свойство:

value - текущее значение в ячейке: 0 - клетка свободна; 1 - стоит крестик; 2 - стоит нолик.

Также с объектами класса Cell должна выполняться функция:

bool(cell) - возвращает True, если клетка свободна (value = 0) и False - в противном случае.

К каждой клетке игрового поля должен быть доступ через операторы:

res = game[i, j] # получение значения из клетки с индексами i, j
game[i, j] = value # запись нового значения в клетку с индексами i, j
Если индексы указаны неверно (не целые числа или числа, выходящие за диапазон [0; 2]), то следует генерировать исключение командой:

raise IndexError('некорректно указанные индексы')
Чтобы в программе не оперировать величинами: 0 - свободная клетка; 1 - крестики и 2 - нолики, в классе TicTacToe должны быть три публичных атрибута (атрибуты класса):

FREE_CELL = 0      # свободная клетка
HUMAN_X = 1        # крестик (игрок - человек)
COMPUTER_O = 2     # нолик (игрок - компьютер)
В самом классе TicTacToe должны быть объявлены следующие методы (как минимум):

init() - инициализация игры (очистка игрового поля, возможно, еще какие-либо действия);
show() - отображение текущего состояния игрового поля (как именно - на свое усмотрение);
human_go() - реализация хода игрока (запрашивает координаты свободной клетки и ставит туда крестик);
computer_go() - реализация хода компьютера (ставит случайным образом нолик в свободную клетку).

Также в классе TicTacToe должны быть следующие объекты-свойства (property):

is_human_win - возвращает True, если победил человек, иначе - False;
is_computer_win - возвращает True, если победил компьютер, иначе - False;
is_draw - возвращает True, если ничья, иначе - False.

Наконец, с объектами класса TicTacToe должна выполняться функция:

bool(game) - возвращает True, если игра не окончена (никто не победил и есть свободные клетки) и False - в противном случае.

Все эти функции и свойства предполагается использовать следующим образом (эти строчки в программе не писать):

game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1


game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")
Вам в программе необходимо объявить только два класса: TicTacToe и Cell так, чтобы с их помощью можно было бы сыграть в "Крестики-нолики" между человеком и компьютером.

P.S. Запускать игру и выводить что-либо на экран не нужно. Только объявить классы.

P.S.S. Домашнее задание: завершите создание этой игры и выиграйте у компьютера хотя бы один раз.

'''

#РАЗРАБОТКА ИГРЫ В КРЕСТИКИ-НОЛИКИ


from random import choice


class Cell:

    def __init__(self):
        self.value = 0

    def __bool__(self):
        return self.value == 0


class TicTacToe:
    FREE_CELL = 0
    HUMAN_X = 1
    COMPUTER_O = 2

    def __init__(self):
        self.pole = tuple(tuple(Cell() for c in range(3)) for r in range(3))
        self.__is_human_win = False
        self.__is_computer_win = False
        self.__is_draw = False

    @property
    def is_human_win(self):
        return self.__is_human_win

    @is_human_win.setter
    def is_human_win(self, val):
        self.__is_human_win = val

    @property
    def is_computer_win(self):
        return self.__is_computer_win

    @is_computer_win.setter
    def is_computer_win(self, val):
        self.__is_computer_win = val

    @property
    def is_draw(self):
        return self.__is_draw

    @is_draw.setter
    def is_draw(self, val):
        self.__is_draw = val

    @staticmethod
    def __check_indx(indx_r, indx_c):
        if not (isinstance(indx_r, int) and isinstance(indx_c, int) and 0 <= indx_r <= 2 \
                and 0 <= indx_c <= 2):
            raise IndexError('некорректно указанные индексы')

    def __getitem__(self, item):
        i_r, i_c = item
        self.__check_indx(i_r, i_c)
        return self.pole[i_r][i_c].value

    def __setitem__(self, key, value):
        i_r, i_c = key
        self.__check_indx(i_r, i_c)
        self.pole[i_r][i_c].value = value
        self.__check_endgame(value)

    def __bool__(self):
        '''Возвращает True если игра закончена и False в противном случае.'''
        return not any([self.is_human_win, self.is_computer_win, self.is_draw])

    def init(self):
        '''Запускает игру заново.'''
        self.__init__()

    def show(self):
        '''Отображает игровое поле.'''
        for r in self.pole:
            for c in r:
                print(c.value, end=' ')
            print()

    def get_empty_cells(self):
        '''Возвращает список состоящий из координат свободных ячеек.'''
        empty_cells = [(ir, ic) for ir, r in enumerate(self.pole)
                       for ic, c in enumerate(r) if bool(c)]
        return empty_cells

    def human_go(self):
        '''Ход игрока.'''
        empty_cells = self.get_empty_cells()
        print('Ваш ход. Введите координаты ячейки в формате "row cel", где row, cell - целые числа:\n')

        while True:
            u_step = tuple(
                int(i) if i.isdigit() else i for i in input().split())
            self.__check_indx(u_step[0], u_step[1])
            if u_step in empty_cells:
                self[u_step[0], u_step[1]] = self.HUMAN_X
                break
            else:
                print('Ячейка занята! Введите координаты повторно.')
        self.__check_endgame(self.HUMAN_X)

    def computer_go(self):
        '''Ход компютера.'''
        empty_cells = self.get_empty_cells()
        c_step = choice(empty_cells)
        self[c_step[0], c_step[1]] = self.COMPUTER_O
        self.__check_endgame(self.COMPUTER_O)

    def __check_endgame(self, char_last_pl):
        '''Осуществляет поиск выиграшных комбинаций по строках, столбцах и диагоналях.'''
        pole = self.pole
        res = -1
        activate = True
        while activate:
            for r in pole:  # поиск выиграшной комбинации по строкам.
                r_lst = []
                for i in r:
                    r_lst.append(i.value == char_last_pl)
                if all(r_lst):
                    res = char_last_pl
                    activate = False
            for c in zip(*pole):  # поиск выиграшной комбинации по столбцам.
                c_lst = []
                for i in c:
                    c_lst.append(i.value == char_last_pl)
                if all(c_lst):
                    res = char_last_pl
                    activate = False
            if {pole[i][i].value for i in range(3)} == {char_last_pl} or \
                    {pole[0][2].value, pole[1][1].value, pole[2][0].value} == {char_last_pl}:  # поиск выиграшной комбинации по диагонали.
                res = char_last_pl
                activate = False
            if len(self.get_empty_cells()) == 0:
                res = 0
            activate = False

        # обявляем победителя (если он есть) и заканчиваем игру.
        if res == 0:
            self.is_draw = True
        elif res == 1:
            self.is_human_win = True
        elif res == 2:
            self.is_computer_win = True



# TESTS:
cell = Cell()
assert cell.value == 0, "начальное значение атрибута value объекта класса Cell должно быть равно 0"
assert bool(
    cell), "функция bool для объекта класса Cell вернула неверное значение"
cell.value = 1
assert not bool(
    cell), "функция bool для объекта класса Cell вернула неверное значение"

assert hasattr(TicTacToe, 'show') and hasattr(TicTacToe, 'human_go') and hasattr(
    TicTacToe, 'computer_go'), "класс TicTacToe должен иметь методы show, human_go, computer_go"

game = TicTacToe()
assert bool(game), "функция bool вернула неверное значения для объекта класса TicTacToe"
assert game[0, 0] == 0 and game[2,
                                2] == 0, "неверные значения ячеек, взятые по индексам"

game[1, 1] = TicTacToe.HUMAN_X
assert game[1, 1] == TicTacToe.HUMAN_X, "неверно работает оператор присваивания нового значения в ячейку игрового поля"

game[0, 0] = TicTacToe.COMPUTER_O
assert game[0, 0] == TicTacToe.COMPUTER_O, "неверно работает оператор присваивания нового значения в ячейку игрового поля"

game.init()
assert game[0, 0] == TicTacToe.FREE_CELL and game[1,
                                                  1] == TicTacToe.FREE_CELL, "при инициализации игрового поля все клетки должны принимать значение из атрибута FREE_CELL"

try:
    game[3, 0] = 4
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

game.init()
assert game.is_human_win == False and game.is_computer_win == False and game.is_draw == False, "при инициализации игры атрибуты is_human_win, is_computer_win, is_draw должны быть равны False, возможно не пересчитывается статус игры при вызове метода init()"

game[0, 0] = TicTacToe.HUMAN_X
game[1, 1] = TicTacToe.HUMAN_X
game[2, 2] = TicTacToe.HUMAN_X
assert game.is_human_win == True and game.is_computer_win == False and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"

game.init()
game[0, 0] = TicTacToe.COMPUTER_O
game[1, 0] = TicTacToe.COMPUTER_O
game[2, 0] = TicTacToe.COMPUTER_O
assert game.is_human_win == False and game.is_computer_win and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"




# Для проверки.
game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1


game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")
