'''
Посвящение в ООП

Вы прошли серию испытаний и совершили множество подвигов, чтобы лицом к лицу столкнуться с настоящим вызовом, достойным лишь избранных! Для подтверждения своих знаний и навыков вам предлагается пройти этап посвящения в объектно-ориентированное программирование. И вот задание, которое выпало на вашу долю.

Руководство компании целыми днями не знает куда себя деть. Поэтому они решили дать задание своим программистам написать программу игры "Морской бой". Но эта игра будет немного отличаться от классической. Для тех, кто не знаком с этой древней, как мир, игрой, напомню ее краткое описание.

Каждый игрок у себя на бумаге рисует игровое поле 10 х 10 клеток и расставляет на нем десять кораблей: однопалубных - 4; двухпалубных - 3; трехпалубных - 2; четырехпалубный - 1.



Корабли расставляются случайным образом, но так, чтобы не выходили за пределы игрового поля и не соприкасались друг с другом (в том числе и по диагонали).

Затем, игроки по очереди называют клетки, куда производят выстрелы. И отмечают эти выстрелы на другом таком же поле в 10 х 10 клеток, которое представляет поле соперника. Соперник при этом должен честно отвечать: "промах", если ни один корабль не был задет и "попал", если произошло попадание. Выигрывает тот игрок, который первым поразит все корабли соперника.

Но это была игра из глубокого прошлого. Теперь же, в компьютерную эру, корабли на игровом поле могут перемещаться в направлении своей ориентации на одну клетку после каждого хода соперника, если в них не было ни одного попадания.

Итак, лично вам поручается сделать важный фрагмент этой игры - расстановку и управление кораблями в этой игре. А само задание звучит так.

Техническое задание

В программе необходимо объявить два класса:

Ship - для представления кораблей;
GamePole - для описания игрового поля.

Класс Ship

Класс Ship должен описывать корабли набором следующих параметров:

x, y - координаты начала расположения корабля (целые числа);
length - длина корабля (число палуб: целое значение: 1, 2, 3 или 4);
tp - ориентация корабля (1 - горизонтальная; 2 - вертикальная).



Объекты класса Ship должны создаваться командами:

ship = Ship(length)
ship = Ship(length, tp)
ship = Ship(length, tp, x, y)

По умолчанию (если не указывается) параметр tp = 1, а координаты x, y равны None.

В каждом объекте класса Ship должны формироваться следующие локальные атрибуты:

_x, _y - координаты корабля (целые значения в диапазоне [0; size), где size - размер игрового поля);
_length - длина корабля (число палуб);
_tp - ориентация корабля;
_is_move - возможно ли перемещение корабля (изначально равно True);
_cells - изначально список длиной length, состоящий из единиц (например, при length=3, _cells = [1, 1, 1]).

Список _cells будет сигнализировать о попадании соперником в какую-либо палубу корабля. Если стоит 1, то попадания не было, а если стоит значение 2, то произошло попадание в соответствующую палубу.

При попадании в корабль (хотя бы одну его палубу), флаг _is_move устанавливается в False и перемещение корабля по игровому полю прекращается.

В самом классе Ship должны быть реализованы следующие методы (конечно, возможны и другие, дополнительные):

set_start_coords(x, y) - установка начальных координат (запись значений в локальные атрибуты _x, _y);
get_start_coords() - получение начальных координат корабля в виде кортежа x, y;
move(go) - перемещение корабля в направлении его ориентации на go клеток (go = 1 - движение в одну сторону на клетку; go = -1 - движение в другую сторону на одну клетку); движение возможно только если флаг _is_move = True;
is_collide(ship) - проверка на столкновение с другим кораблем ship (столкновением считается, если другой корабль или пересекается с текущим или просто соприкасается, в том числе и по диагонали); метод возвращает True, если столкновение есть и False - в противном случае;
is_out_pole(size) - проверка на выход корабля за пределы игрового поля (size - размер игрового поля, обычно, size = 10); возвращается булево значение True, если корабль вышел из игрового поля и False - в противном случае;

С помощью магических методов __getitem__() и __setitem__() обеспечить доступ к коллекции _cells следующим образом:

value = ship[indx] # считывание значения из _cells по индексу indx (индекс отсчитывается от 0)
ship[indx] = value # запись нового значения в коллекцию _cells

Класс GamePole

Следующий класс GamePole должен обеспечивать работу с игровым полем. Объекты этого класса создаются командой:

pole = GamePole(size)

где size - размеры игрового поля (обычно, size = 10).

В каждом объекте этого класса должны формироваться локальные атрибуты:

_size - размер игрового поля (целое положительное число);
_ships - список из кораблей (объектов класса Ship); изначально пустой список.

В самом классе GamePole должны быть реализованы следующие методы (возможны и другие, дополнительные методы):

init() - начальная инициализация игрового поля; здесь создается список из кораблей (объектов класса Ship): однопалубных - 4; двухпалубных - 3; трехпалубных - 2; четырехпалубный - 1 (ориентация этих кораблей должна быть случайной).

Корабли формируются в коллекции _ships следующим образом: однопалубных - 4; двухпалубных - 3; трехпалубных - 2; четырехпалубный - 1. Ориентация этих кораблей должна быть случайной. Для этого можно воспользоваться функцией randint следующим образом:

[Ship(4, tp=randint(1, 2)), Ship(3, tp=randint(1, 2)), Ship(3, tp=randint(1, 2)), ...]

Начальные координаты x, y не расставленных кораблей равны None.

После этого, выполняется их расстановка на игровом поле со случайными координатами так, чтобы корабли не пересекались между собой.

get_ships() - возвращает коллекцию _ships;
move_ships() - перемещает каждый корабль из коллекции _ships на одну клетку (случайным образом вперед или назад) в направлении ориентации корабля; если перемещение в выбранную сторону невозможно (другой корабль или пределы игрового поля), то попытаться переместиться в противоположную сторону, иначе (если перемещения невозможны), оставаться на месте;
show() - отображение игрового поля в консоли (корабли должны отображаться значениями из коллекции _cells каждого корабля, вода - значением 0);

get_pole() - получение текущего игрового поля в виде двумерного (вложенного) кортежа размерами size x size элементов.

Пример отображения игрового поля:

0 0 1 0 1 1 1 0 0 0
1 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 0 0 1
0 0 0 0 1 0 1 0 0 1
0 0 0 0 0 0 1 0 0 0
1 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 0 0 0
0 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 1 1 0

Пример использования классов (эти строчки в программе не писать):

SIZE_GAME_POLE = 10

pole = GamePole(SIZE_GAME_POLE)
pole.init()
pole.show()

pole.move_ships()
print()
pole.show()


В программе требуется только объявить классы Ship и GamePole с соответствующим функционалом. На экран выводить ничего не нужно.

P.S. Для самых преданных поклонников программирования и ООП. Завершите эту программу, добавив еще один класс SeaBattle для управления игровым процессом в целом. Игра должна осуществляться между человеком и компьютером. Выстрелы со стороны компьютера можно реализовать случайным образом в свободные клетки. Сыграйте в эту игру и выиграйте у компьютера.
 Memory limit: 256 MBTime limit: 15 seconds

'''

from random import randint, choice


class GamePoleError(Exception):
    '''Базовый класс исключений для игрового поля.'''
    pass

class CountShipsError(GamePoleError):
    '''Исключения при передачи неверного количества кораблей.'''
    pass

class TypeShipsError(GamePoleError):
    '''Исключения при передачи кораблей неверного типа.'''
    pass

class ShipsCoordsError(GamePoleError):
    '''Исключения при передачи кораблей c неверными координатами.'''
    pass


class Ship:
    '''Класс представления кораблей.'''

    def __init__(self, *args):

        params = len(args)  # Количество переданных параметров.

        self._length = args[0]
        self._tp = args[1] if params >= 2 else 1  # Ориентация корабля (1 - горизонтальная; 2 - вертикальная).
        self._x = args[2] if params >= 3 else None  # Координата 'x' (строка).
        self._y = args[3] if params >= 4 else None  # Координата 'y' (столбец).
        self._is_move = True # Перемещение корабля.
        self._cells = [1] * self._length  # Изначально список длиной length, состоящий из единиц (например, при length=3, _cells = [1, 1, 1]).

    def get_width(self):
        '''Возвращает ширину корабля.'''
        return self._length if self._tp == 1 else 1

    def get_height(self):
        '''Возвращает длину корабля.'''
        return self._length if self._tp == 2 else 1

    def get_coords_cells_ship(self):
        '''Возвращает список координат ячеек которые занимает корабль.'''
        lst = []

        if self._x != None and self._y != None:
            if self._tp == 1:
                for step in range(self._length):
                    lst.append((self._x, self._y + step))
            elif self._tp == 2:
                for step in range(self._length):
                    lst.append((self._x + step, self._y))
        return lst

    def get_area(self):
        '''Возвращает список координат (площадь которую занимает корабль с внешней границей в 1 ячейку.)'''
        lst = []

        if self._x != None and self._y != None:
            if self._tp == 1:
                for step_x in range(self._x - 1, self._x + 2):
                    for step_y in range(self._y - 1,
                                        self._y + self._length + 1):
                        lst.append((step_x, step_y))

            elif self._tp == 2:
                for step_y in range(self._y - 1, self._y + 2):
                    for step_x in range(self._x - 1,
                                        self._x + self._length + 1):
                        lst.append((step_x, step_y))
        return lst

    def set_start_coords(self, x, y):
        '''Установка начальных координат (запись значений в локальные атрибуты _x, _y).'''
        self._x = x
        self._y = y

    def get_start_coords(self):
        '''Получение начальных координат корабля в виде кортежа x, y.'''
        return self._x, self._y

    def move(self, go):
        '''
        Перемещение корабля в направлении его ориентации на go клеток
        (go = 1 - движение в одну сторону на клетку; go = -1 - движение в другую сторону на одну клетку);
        движение возможно только если флаг _is_move = True
        '''

        # Если корабль не ранен (может двигаться).
        if self._is_move:
            # Если ориентация корабля горизонтальная, - сунем на одну ячейку по 'y'.
            if self._tp == 1:
                if go == 1:
                    self._y += 1
                elif go == -1:
                    self._y -= 1
            # Если ориентация корабля вертикальная, - сунем на одну ячейку по 'x'.
            else:
                if go == 1:
                    self._x += 1
                elif go == -1:
                    self._x -= 1


    def is_collide(self, ship):
        '''
        Проверка на столкновение с другим кораблем ship
        (столкновением считается, если другой корабль или пересекается с текущим
        или просто соприкасается, в том числе и по диагонали);
        метод возвращает True, если столкновение есть и False - в противном случае;
        '''

        # Проверяем на пересечение координаты корабля с площадью занимаемой другим кораблем.
        return True if set(self.get_coords_cells_ship()) & set(ship.get_area()) else False


    def is_out_pole(self, size=10):
        '''
        Проверка на выход корабля за пределы игрового поля
        (size - размер игрового поля, обычно, size = 10);
        возвращается булево значение True, если корабль вышел из игрового поля и False - в противном случае;
        '''

        #Берем значение максимальной координаты и сравниваем с крайней границой игрового поля. Если максимальная координата
        # больше или равна размеру поля или минимальная меньше нуля, метод возвращает True.

        coords = [coord for cell_coords in self.get_coords_cells_ship()
                            for coord in cell_coords]

        return (max(coords) >= size) or (min(coords) < 0)


    def __getitem__(self, item):
        '''Cчитывание значения из _cells по индексу indx (индекс отсчитывается от 0).'''
        return self._cells[item]

    def __setitem__(self, key, value):
        '''Запись нового значения в коллекцию.'''
        self._cells[key] = value


class GamePole:
    '''Класс представления игровых полей.'''

    def __init__(self, size=10):
        self._size = size
        self._ships = []

    def init(self, ships=None):
        '''
        Здесь создается список из кораблей (объектов класса Ship):
        однопалубных - 4; двухпалубных - 3; трехпалубных - 2; четырехпалубный - 1
        (ориентация этих кораблей должна быть случайной).
        '''

        # Создается список кораблей со случайной ориентацией.
        if ships != None:
            self._ships = ships
        else:
            self._ships = [Ship(4, randint(1, 2)),
                           Ship(3, randint(1, 2)), Ship(3, randint(1, 2)),
                           Ship(2, randint(1, 2)), Ship(2, randint(1, 2)),
                           Ship(2, randint(1, 2)),
                           Ship(1, randint(1, 2)), Ship(1, randint(1, 2)),
                           Ship(1, randint(1, 2)),
                           Ship(1, randint(1, 2))
                           ]

        # Фильтруем корабли, которым не переданы координаты 'x', 'y'.
        ship_without_coords = filter(lambda s: s._x == None and s._y == None,
                                     self._ships)
        border = self._size

        for sp in ship_without_coords:
            # Выбираем случайные координаты для размещения нового корабля.
            while True:
                x = randint(0, border - 1)
                y = randint(0, border - 1)
                # Если ориентация корабля горизонтальная, то для проверки к 'y' добавляем длину корабля,
                # иначе к 'x' (проверка на выход за пределы поля).
                if sp._tp == 1 and (y + sp._length) > (border - 1):
                    y_ = y + sp._length
                    if y_ > (border - 1):
                        continue
                else:
                    x_ = x + sp._length
                    if x_ > (border - 1):
                        continue

                # Фильтруем список кораблей, отбирая корабли не равны текущему и которые имеют координаты 'x' и 'y' != None.
                placed_ships = list(
                    filter(lambda s: s != sp and s._x != None and s._y != None,
                           self._ships))

                # Делаем проверку на непересечение с координатами другого корабля.
                is_collis = self.__is_collision(x, y, sp, placed_ships)

                if x < border and y < border and is_collis == False:
                    sp.set_start_coords(x, y)
                    break

        # Генерируем исключения в случае ошибок.
        type_ships = [s._length for s in self._ships]  # Список типов кораблей.
        ships_with_corect_coords = []  # Количество кораблей с корректными координатами.
        for sp in self._ships:
            sp_coords = sp.get_coords_cells_ship()
            if not (set(sp_coords) & set(
                    [coords for ship in filter(lambda s: s != sp, self._ships)
                     for coords in ship.get_area()]) \
                    or max([coord for cell_coords in sp_coords
                            for coord in cell_coords]) >= border):
                ships_with_corect_coords.append(sp)

        if len(self._ships) != 10:
            raise CountShipsError(
                'Передано неверное количество кораблей при инициализации.')
        elif not (type_ships.count(4) == 1 and type_ships.count(3) == 2 \
                  and type_ships.count(2) == 3 and type_ships.count(1) == 4):
            raise TypeShipsError(
                'Перереданы корабли неверных типов при инициализации.')
        elif len(ships_with_corect_coords) != 10:
            raise ShipsCoordsError(
                'Переданы корабли с неверными координатами при инициализации.')

    @staticmethod
    def __is_collision(x, y, ship, placed_ships):
        '''Осуществляет проверку на пересечение координат с координатами прощади другого корабля.'''

        lst = []
        if ship._tp == 1:
            for step in range(ship._length):
                lst.append((x, y + step))
        elif ship._tp == 2:
            for step in range(ship._length):
                lst.append((x + step, y))

        if set(lst) & set([coords for ship in placed_ships
                           for coords in ship.get_area()]):
            return True
        return False

    def get_ships(self):
        '''Возвращает список _ships.'''
        return self._ships

    def move_ships(self):
        '''
        Перемещает каждый корабль из коллекции _ships на одну клетку
        (случайным образом вперед или назад) в направлении ориентации корабля;
        если перемещение в выбранную сторону невозможно (другой корабль или пределы игрового поля),
        то попытаться переместиться в противоположную сторону, иначе (если перемещения невозможны), оставаться на месте;
        '''

        ships = self.get_ships()
        for sp in ships:
            if 2 in sp._cells: # Если корабль ранен, то не пытаемся его перемещать.
                continue

            cur_x, cur_y = sp._x, sp._y # Фиксируем текущие координаты корабля.
            go = randint(-1,1) # Выбираем случайное направление для шага.
            sp.move(go) # Делаем шаг в соответствующем направлении.
            is_collide = any([sp.is_collide(s) for s in filter(lambda s: s != sp, ships)]) # Проверяем есть ли пересечение новых координат хоть с одним с кораблей флотилии.
            is_out_pole = sp.is_out_pole(self._size) # Проверяем не выходят ли новые координаты за пределы поля.

            if is_collide or is_out_pole: # Если хоть одно из условий выше возвратило True пробуем переместить корабль в другую сторону.
                sp._x, sp._y = cur_x, cur_y # Поставим корабль на прежнюю позицию.
                go = 1 if go == -1 else -1 # Меняем курс на противоположный.
                sp.move(go)  # Делаем шаг в соответствующем направлении.
                is_collide = any([sp.is_collide(s) for s in filter(lambda s: s != sp,ships)])
                is_out_pole = sp.is_out_pole(self._size)

                if is_collide or is_out_pole: # Если хоть одно условие опять возвратило True, - ставим корабль на место.
                    sp._x, sp._y = cur_x, cur_y


    def show(self, hide_ships = False):
        '''
        Отображение игрового поля в консоли
        (корабли должны отображаться значениями из коллекции _cells каждого корабля, вода - значением 0);
        '''

        # Формируем словарь в формате: ('x', 'y') : состояние палубы корабля (значение по индексу из списка _cells).
        dict_coords = {}

        for coords, ship in self.get_ships_coords().items():
            indx = ship.get_coords_cells_ship().index(coords)
            dict_coords[coords] = ship[indx]

        # Получаем множество координат вокруг затонувших кораблей.
        shipwreck_coords = {coord for sp in self.get_ships() if all(cell == 2 for cell in sp._cells)
                            for coord in set(sp.get_area()) - set(sp.get_coords_cells_ship())}

        # В зависимости от переданного в hide_ships аргумента скрываем все ячейки поля до поражения корабля противника, или отображаем их.
        for k, v in enumerate(self.get_pole()):
            for key, val in enumerate(v):
                if not hide_ships:
                    print(dict_coords.get((k,key),0),end='')
                else:
                    val = dict_coords.get((k,key),0)
                    print(val if val not in (0,1) or (k,key) in shipwreck_coords else '#', end='')
            print()


    def get_pole(self):
        '''Получение текущего игрового поля в виде двумерного (вложенного) кортежа размерами size x size элементов.'''

        return tuple(tuple([0] * self._size) for i in range(self._size))

    def get_ships_coords(self):
        '''Возвращает словарь в формате: ('х','y') : объект корабль.'''
        return {coords:sp for sp in self.get_ships() for coords in sp.get_coords_cells_ship()}



class SeaBattle:
    '''Класс для управления игровым процессом.'''

    def __init__(self, size=10):

        # При инициализации создаем 2 игровых поля (для игрока и для компютера соответственно).
        self._size = size
        self._all_cells = [(x,y) for x in range(size) for y in range(size)]
        self._pole_human = GamePole(size)
        self._pole_computer = GamePole(size)
        # В словари будут записываться координаты кораблей (если он ранен) и площади вокруг них (если он затонул).
        self._opened_cells_human_pole = {}
        self._opened_cells_computer_pole = {}
        self._is_human_win = False
        self._is_computer_win = False

    def init(self,size=10):
        '''Запускает игру заново.'''
        self.__init__(size)

    def __bool__(self):
        '''Возвращает True если игра закончена и False в противном случае.'''
        return not any([self._is_human_win, self._is_computer_win])


    def __check_indx(self,indx_x, indx_y):
        '''Проверка на корректность индексов (должны быть [0,_size)).'''
        if not (isinstance(indx_x, int) and isinstance(indx_y,
                                                       int) and 0 <= indx_x < self._size \
                and 0 <= indx_y < self._size):
            raise IndexError('некорректно указанные индексы')

    def __get_empty_cells(self, open_cells: list):
        '''
        Метод должен вычитать из множества всех ячеек, открытые ячейки
        и возвращать список кортежей (координат ячеек) доступных для хода игрока или компютера.
        '''
        return list(set(self._all_cells) - set(open_cells))



    def human_go(self):
        '''Ход игрока.'''

        empty_cells = self.__get_empty_cells(list(self._opened_cells_computer_pole.keys()))
        print(f'Ваш ход. Введите координаты ячейки в формате "x y", где x, y - целые числа от 0 до {self._size-1}:\n')
        while True:
            h_step = tuple(int(i) if i.isdigit() else i for i in input().split())
            self.__check_indx(h_step[0], h_step[1])
            if h_step in empty_cells:
                # Реализуется логика выстрела.
                sp_coords_dict = self._pole_computer.get_ships_coords()# Получаем словарь кординат где находятся корабли.
                stricken_ship = sp_coords_dict.get(h_step)
                if not stricken_ship:
                    self._pole_computer.move_ships() # Если игрок не попал у корабль, передвигаем все подвижные корабли компютера.
                    break # Прерываем цикл.
                else:
                    # Если игрок попал у корабль, запретим перемещение по полю. Возьмем список координат етого корабля,
                    # индекс ячейки у которую попал игрок и изменим значение ячейки списка _cells с таким же индексом на значение 2 (поражен).
                    if stricken_ship._is_move:
                        stricken_ship._is_move = False

                    coords_stricken_ship = stricken_ship.get_coords_cells_ship()
                    h_step_indx = coords_stricken_ship.index(h_step)
                    stricken_ship[h_step_indx] = 2
                    # Внесем новое значение в словарь _opened_cells_computer_pole.
                    self._opened_cells_computer_pole[h_step] = 2
                    # Далее пройдемся по всех палубах етого корабля, и если все поражены, то корабль затонул, и координаты вокруг него тоже
                    # следует внести в словарь _opened_cells_computer_pole.
                    if all(map(lambda s: s == 2, stricken_ship._cells)):
                        sp_border_coords = set(stricken_ship.get_area())-set(coords_stricken_ship)
                        for coord in sp_border_coords:
                            self._opened_cells_computer_pole[coord] = 0
                    self._pole_computer.move_ships()  # Передвигаем все подвижные корабли компютера.
                    self._pole_computer.show(hide_ships=True) # Покажем игроку результат выстрела (отобразим поле в консоли).
                    # Делаем проверку игры на ее завершение (все палубы всех кораблей компютера поражены). Если True, - то победил человек и игра завершена.
                    if self.__check_endgame(self._pole_computer.get_ships()):
                        self._is_human_win = True
                        break
            else:
                print('Нет смысла целить в открытую ячейку! Введите координаты повторно.')



    def computer_go(self):
        '''Ход компютера.'''
        empty_cells = self.__get_empty_cells(list(self._opened_cells_human_pole.keys()))
        while True:
            c_step = choice(empty_cells)
            sp_coords_dict = self._pole_human.get_ships_coords()
            stricken_ship = sp_coords_dict.get(c_step)

            if not stricken_ship:
                self._pole_human.move_ships()  # Передвигаем все подвижные корабли игрока.
                break
            else:
                if stricken_ship._is_move:
                    stricken_ship._is_move = False

                coords_stricken_ship = stricken_ship.get_coords_cells_ship()
                c_step_indx = coords_stricken_ship.index(c_step)
                stricken_ship[c_step_indx] = 2
                # Внесем новое значение в словарь _opened_cells_human_pole.
                self._opened_cells_human_pole[c_step] = 2
                # Далее пройдемся по всех палубах етого корабля, и если все поражены, то корабль затонул, и координаты вокруг него тоже
                # следует внести в словарь _opened_cells_human_pole.
                if all(map(lambda s: s == 2, stricken_ship._cells)):
                    sp_border_coords = set(stricken_ship.get_area()) - set(
                        coords_stricken_ship)
                    for coord in sp_border_coords:
                        self._opened_cells_human_pole[coord] = 0
                self._pole_human.move_ships()  # Передвигаем все подвижные корабли игрока.
                # Делаем проверку игры на ее завершение (все палубы всех кораблей игрока поражены). Если да, - то победил компьютер и игра завершена.
                if self.__check_endgame(self._pole_human.get_ships()):
                    self._is_computer_win = True
                    break

    @staticmethod
    def __check_endgame(lst_ships):
        '''Делает проверку поражения всех палуб кораблей противника.'''

        return all(map(lambda s: s == 2, [cell for sp in lst_ships
                                          for cell in sp._cells]))

# Для запуска игрового процесса.
game = SeaBattle()
game.init()
game._pole_human.init()
game._pole_computer.init()

step_game = 0
while game:

    if step_game % 2 == 0:
        print('---Поле компьютера---')
        game._pole_computer.show(hide_ships=True)
        game.human_go()
    else:
        print('-----Поле игрока-----')
        game._pole_human.show(hide_ships=False)
        game.computer_go()

    step_game += 1


if game._is_human_win:
    print("Поздравляем! Вы победили!")
elif game._is_computer_win:
    print("Все получится, со временем")


# SIZE_GAME_POLE = 10
#
# pole = GamePole(SIZE_GAME_POLE)
# pole.init()
# pole.show()
#
# pole.move_ships()
# print()
# pole.show()




#TESTS
# ship = Ship(2)
# ship = Ship(2, 1)
# ship = Ship(3, 2, 0, 0)
#
# assert ship._length == 3 and ship._tp == 2 and ship._x == 0 and ship._y == 0, "неверные значения атрибутов объекта класса Ship"
# assert ship._cells == [1, 1, 1], "неверный список _cells"
# assert ship._is_move, "неверное значение атрибута _is_move"
#
# ship.set_start_coords(1, 2)
# assert ship._x == 1 and ship._y == 2, "неверно отработал метод set_start_coords()"
# assert ship.get_start_coords() == (1, 2), "неверно отработал метод get_start_coords()"
#
# ship.move(1)
# s1 = Ship(4, 1, 0, 0)
# s2 = Ship(3, 2, 0, 0)
# s3 = Ship(3, 2, 0, 2)
#
# assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 0)"
# assert s1.is_collide(
#     s3), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 2)"
#
# s2 = Ship(3, 2, 1, 1)
# assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 1, 1)"
#
# s2 = Ship(3, 1, 8, 1)
# assert s2.is_out_pole(10) == False, "неверно работает метод is_out_pole() для корабля Ship(3, 1, 8, 1)"
#
# s2 = Ship(3, 2, 1, 5)
# assert s2.is_out_pole(10) == False, "неверно работает метод is_out_pole(10) для корабля Ship(3, 2, 1, 5)"
#
# s2[0] = 2
# assert s2[0] == 2, "неверно работает обращение ship[indx]"
#
# p = GamePole(10)
# p.init()
# for nn in range(5):
#     for s in p._ships:
#         assert s.is_out_pole(10) == False, "корабли выходят за пределы игрового поля"
#
#         for ship in p.get_ships():
#             if s != ship:
#                 assert s.is_collide(ship) == False, "корабли на игровом поле соприкасаются"
#     p.move_ships()
#
# gp = p.get_pole()
# assert type(gp) == tuple and type(gp[0]) == tuple, "метод get_pole должен возвращать двумерный кортеж"
# assert len(gp) == 10 and len(gp[0]) == 10, "неверные размеры игрового поля, которое вернул метод get_pole"
#
# pole_size_8 = GamePole(8)
# pole_size_8.init()
# print()