'''
Подвиг 3. (task_1.py)

Объявите класс Track (маршрут), объекты которого создаются командой:

track = Track(start_x, start_y)
где start_x, start_y - координаты начала маршрута (целые или вещественные числа).

Каждый линейный сегмент маршрута определяется классом TrackLine, объекты которого создаются командой:

line = TrackLine(to_x, to_y, max_speed)
где to_x, to_y - координаты следующей точки маршрута (целые или вещественные числа); max_speed - максимальная скорость на данном участке (целое число).

Для формирования и работы с маршрутом в классе Track должны быть объявлены следующие методы:

add_track(self, tr) - добавление линейного сегмента маршрута (следующей точки);
get_tracks(self) - получение кортежа из объектов класса TrackLine.

Также для объектов класса Track должны быть реализованные следующие операции сравнения:

track1 == track2  # маршруты равны, если равны их длины
track1 != track2  # маршруты не равны, если не равны их длины
track1 > track2  # True, если длина пути для track1 больше, чем для track2
track1 < track2  # True, если длина пути для track1 меньше, чем для track2

'''


class Track:

    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.line_segments = []

    def add_track(self, tr):
        if isinstance(tr, TrackLine):
            self.line_segments.append(tr)
        else:
            raise TypeError('Не верный тип данных.')

    def get_tracks(self):
        return tuple(self.line_segments)

    def __eq__(self, other):
        self.__check_val_obj(other)
        return len(self) == len(other)

    def __gt__(self, other):
        self.__check_val_obj(other)
        return len(self) > len(other)

    @classmethod
    def __check_val_obj(cls, value):
        if not isinstance(value, cls):
            raise ValueError('Не верный тип данных.')

    @staticmethod
    def __get_line_length(x1, y1, x2, y2):
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    def __len__(self):
        sgts = self.line_segments
        lng_track = 0
        lng_track += self.__get_line_length(self.start_x, self.start_y,
                                            sgts[0].to_x, sgts[0].to_y)
        for i in range(len(sgts) - 1):
            lng_track += self.__get_line_length(sgts[i].to_x, sgts[i].to_y,
                                                sgts[i + 1].to_x,
                                                sgts[i + 1].to_y)
        return int(lng_track)


class TrackLine:

    def __init__(self, to_x, to_y, max_speed):
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed


track1 = Track(0, 0)
track2 = Track(0, 1)

track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))

track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))

res_eq = track1 == track2