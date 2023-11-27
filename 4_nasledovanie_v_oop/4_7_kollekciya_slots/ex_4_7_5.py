'''
Подвиг 5. (task_2.py)

Объявите класс Planet (планета), объекты которого создаются командой:

p = Planet(name, diametr, period_solar, period)
где name - наименование планеты; diametr - диаметр планеты (любое положительное число); period_solar - период (время) обращения планеты вокруг Солнца (любое положительное число); period - период обращения планеты вокруг своей оси (любое положительное число).

В каждом объекте класса Planet должны формироваться локальные атрибуты с именами: _name, _diametr, _period_solar, _period и соответствующими значениями.

SolarSystem

Затем, объявите класс с именем SolarSystem (солнечная система). В объектах этого класса должны быть допустимы, следующие локальные атрибуты (ограничение задается через коллекцию __slots__):

_mercury - ссылка на планету Меркурий (объект класса Planet);
_venus - ссылка на планету Венера (объект класса Planet);
_earth - ссылка на планету Земля (объект класса Planet);
_mars - ссылка на планету Марс (объект класса Planet);
_jupiter - ссылка на планету Юпитер (объект класса Planet);
_saturn - ссылка на планету Сатурн (объект класса Planet);
_uranus - ссылка на планету Уран (объект класса Planet);
_neptune - ссылка на планету Нептун (объект класса Planet).
Объект класса SolarSystem должен создаваться командой:

s_system = SolarSystem()
и быть только один (одновременно в программе два и более объектов класса SolarSystem недопустимо). Используйте для этого паттерн Singleton.

В момент создания объекта SolarSystem должны автоматически создаваться перечисленные локальные атрибуты и ссылаться на соответствующие объекты класса Planet со следующими данными по планетам:

PlanetTable

Создайте в программе объект s_system класса SolarSystem.

P.S. В программе следует объявить только классы и создать объект s_system. На экран выводить ничего не нужно.


'''


class Planet:

    def __init__(self, name, diametr, period_solar, period):
        self._name = name
        self._diametr = diametr
        self._period_solar = period_solar
        self._period = period


class SolarSystem:
    single_obj = None

    def __new__(cls, *args, **kwargs):
        if cls.single_obj == None:
            cls.single_obj = super().__new__(cls)
        return cls.single_obj

    __slots__ = (
        '_mercury', '_venus', '_earth', '_mars', '_jupiter', '_saturn',
        '_uranus','_neptun')

    def __init__(self):
        planets_dict = {'_mercury': ('Меркурий', 4878, 87.97, 1407.5),
                        '_venus': ('Венера', 12104, 224.7, 5832.45),
                        '_earth': ('Земля', 12756, 365.3, 23.93),
                        '_mars': ('Марс', 6794, 687, 24.62),
                        '_jupiter': ('Юпитер', 142800, 4330, 9.9),
                        '_saturn': ('Сатурн', 120660, 10753, 10.63),
                        '_uranus': ('Уран', 51118, 30665, 17.2),
                        '_neptun': ('Нептун', 49528, 60150, 16.1)}

        for k, v in planets_dict.items():
            setattr(self, k, Planet(*v))


s_system = SolarSystem()
s_system2 = SolarSystem()

# # Для проверки.
# for p in s_system.__slots__:
#     print(getattr(s_system,p)._name)