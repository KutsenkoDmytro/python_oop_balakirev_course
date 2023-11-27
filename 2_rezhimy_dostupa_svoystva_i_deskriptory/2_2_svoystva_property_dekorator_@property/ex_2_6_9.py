'''
Вам требуется сформировать класс PathLines для описания маршрутов, состоящих из линейных сегментов.
При этом каждый линейный сегмент предполагается задавать отдельным классом LineTo. Объекты этого класса будут формироваться командой:

line = LineTo(x, y)
где x, y - следующая координата линейного участка (начало маршрута из точки 0, 0).

В каждом объекте класса LineTo должны формироваться локальные атрибуты:

x, y - для хранения координат конца линии (начало определяется по координатам предыдущего объекта).

Объекты класса PathLines должны создаваться командами:

p = PathLines()                   # начало маршрута из точки 0, 0
p = PathLines(line1, line2, ...)  # начало маршрута из точки 0, 0
где line1, line2, ... - объекты класса LineTo.

Сам же класс PathLines должен иметь следующие методы:

get_path() - возвращает список из объектов класса LineTo (если объектов нет, то пустой список);
get_length() - возвращает суммарную длину пути (сумма длин всех линейных сегментов);
add_line(self, line) - добавление нового линейного сегмента (объекта класса LineTo) в конец маршрута.

Пояснение: суммарный маршрут - это сумма длин всех линейных сегментов, а длина каждого линейного сегмента определяется как евклидовое расстояние по формуле:

L = sqrt((x1-x0)^2 + (y1-y0)^2)
где x0, y0 - предыдущая точка маршрута; x1, y1 - текущая точка маршрута.

Пример использования классов (эти строчки в программе писать не нужно):

p = PathLines(LineTo(10, 20), LineTo(10, 30))
p.add_line(LineTo(20, -10))
dist = p.get_length()

'''
# Двусвязный список.

from math import sqrt


class LineTo:
    '''Описывает линейный сегмент.'''
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.next = None
        self.prev = None


class PathLines:
    '''Описывает маршруты, состоящие из линейных сегментов.'''

    def __init__(self, *args):
        self.head = None
        self.tail = None
        if args:
            for obj in args:
                self.add_line(obj)

    def add_line(self, line):
        '''Добавляет новый линейный сегмент (объекта класса LineTo) в конец маршрута.'''
        if self.head == None:
            self.head = line
        if self.tail != None:
            self.tail.next = line
            line.prev = self.tail
        self.tail = line

    def get_path(self):
        '''Возвращает список из объектов класса LineTo (если объектов нет, то пустой список).'''
        lst_res = []
        ptr = self.head
        while ptr:
            lst_res.append(ptr)
            ptr = ptr.next
        return lst_res

    def get_length(self):
        '''Возвращает суммарную длину пути (сумма длин всех линейных сегментов).'''
        dist = 0
        for indx, obj in enumerate(self.get_path()):
            l = 0
            if indx == 0:
                l = sqrt((obj.x - 0) ** 2 + (obj.y - 0) ** 2)
            else:
                l = sqrt((obj.x - obj.prev.x) ** 2 + (obj.y - obj.prev.y) ** 2)
            dist += l
        return dist


p = PathLines(LineTo(10, 20), LineTo(10, 30))
p.add_line(LineTo(20, -10))
dist = p.get_length()

# # Для проверки:
# print(p.get_path())
# print(dist)
