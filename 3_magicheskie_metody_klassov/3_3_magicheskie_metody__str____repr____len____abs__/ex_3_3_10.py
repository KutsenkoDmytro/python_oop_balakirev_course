'''
Подвиг 10 (на повторение). Объявите класс PolyLine (полилиния) для представления линии из последовательности прямолинейных сегментов. Объекты этого класса должны создаваться командой:

poly = PolyLine(start_coord, coord_2, coord_3, ..., coord_N)
Здесь start_coord - координата начала полилинии (кортеж из двух чисел x, y); coord_2, coord_3, ... - последующие координаты точек на плоскости (представленные кортежами), соединенных прямыми линиями.

Например:

poly = PolyLine((1, 2), (3, 5), (0, 10), (-1, 8))


В классе PolyLine должны быть объявлены следующие методы:

add_coord(x, y) - добавление новой координаты (в конец);
remove_coord(indx) - удаление координаты по индексу (порядковому номеру, начинается с нуля);
get_coords() - получение списка координат (в виде списка из кортежей).

'''

class PolyLine:

    def __init__(self, *args):
        self.__coords = list(args)

    def add_cord(self, x, y):
        self.__coords.append((x,y))

    def remove_coord(self, indx):
        self.__coords.pop(indx)

    def get_coords(self):
        return self.__coords

# # Для проверки.
# poly = PolyLine((1, 2), (3, 5), (0, 10), (-1, 8))
# print(poly.get_coords())