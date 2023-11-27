'''
Подвиг 6 (релакс). (task_3.py)

Объявите класс Line, объекты которого создаются командой:

line = Line(x1, y1, x2, y2)
где x1, y1, x2, y2 - координаты начала линии (x1, y1) и координаты конца линии (x2, y2). Могут быть произвольными числами. В объектах класса Line должны создаваться соответствующие локальные атрибуты с именами x1, y1, x2, y2.

В классе Line определить магический метод __len__() так, чтобы функция:

bool(line)
возвращала False, если длина линии меньше 1.

P.S. На экран ничего выводить не нужно. Только объявить класс.

'''

class Line:

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def __len__(self):
        return self.get_line_length() > 1

    # def __bool__(self):
    #     return  self.__len__() > 1

    def get_line_length(self):
        return ((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** 0.5


# # Для проверки.
# line = Line(2,2,3,3)
# print(line.get_line_length())
# print(bool(line))

