'''
Подвиг 9 (релакс). (task_7.py)

Необходимо объявить класс Body (тело), объекты которого создаются командой:

body = Body(name, ro, volume)
где name - название тела (строка); ro - плотность тела (число: вещественное или целочисленное); volume - объем тела (число: вещественное или целочисленное).

Для объектов класса Body должны быть реализованы операторы сравнения:

body1 > body2  # True, если масса тела body1 больше массы тела body2
body1 == body2 # True, если масса тела body1 равна массе тела body2
body1 < 10     # True, если масса тела body1 меньше 10
body2 == 5     # True, если масса тела body2 равна 5
Масса тела вычисляется по формуле:

m = ro * volume
P.S. В программе только объявить класс, выводить на экран ничего не нужно.

'''


class Body:
    '''Класс описывающий тело.'''

    def __init__(self, name, ro, volume):
        self.name = name
        self.ro = ro
        self.volume = volume

    def get_weight(self):
        return self.ro * self.volume

    def __gt__(self, other):
        self.__check_val(other)
        if isinstance(other, self.__class__):
            other = other.get_weight()
        return self.get_weight() > other

    def __lt__(self, other):
        self.__check_val(other)
        if isinstance(other, self.__class__):
            other = other.get_weight()
        return self.get_weight() < other

    def __eq__(self, other):
        self.__check_val(other)
        if isinstance(other, self.__class__):
            other = other.get_weight()
        return self.get_weight() == other

    @classmethod
    def __check_val(cls, value):
        if type(value) not in {int, float, cls}:
            raise ValueError('Не верный тип данных для сравнения.')



# # Для проверки
# body1 = Body('body1', 2, 32)
# body2 = Body('body1', 2, 2.5)
# body1 > body2  # True, если масса тела body1 больше массы тела body2
# body1 == body2 # True, если масса тела body1 равна массе тела body2
# body1 < 10     # True, если масса тела body1 меньше 10
# body2 == 5     # True, если масса тела body2 равна 5