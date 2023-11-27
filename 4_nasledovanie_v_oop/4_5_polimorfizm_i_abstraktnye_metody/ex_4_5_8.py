'''
Подвиг 8. (task_6.py)

С помощью модуля abc можно определять не только абстрактные методы, но и абстрактные объекты-свойства (property). Делается это следующим образом:

from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def go(self):
        """Метод для перемещения транспортного средства"""

    @property
    @abstractmethod
    def speed(self):
        """Абстрактный объект-свойство"""
Используя эту информацию и информацию о модуле abc из подвига 6, объявите базовый класс с именем CountryInterface со следующими абстрактными методами и свойствами:

name - абстрактное свойство (property), название страны (строка);
population - абстрактное свойство (property), численность населения (целое положительное число);
square - абстрактное свойство (property), площадь страны (положительное число);

get_info() - абстрактный метод для получения сводной информации о стране.

На основе класса CountryInterface объявите дочерний класс Country, объекты которого создаются командой:

country = Country(name, population, square)
В самом классе Country должны быть переопределены следующие свойства и методы базового класса:

name - свойство (property) для считывания названия страны (строка);
population - свойство (property) для записи и считывания численности населения (целое положительное число);
square - свойство (property) для записи и считывания площади страны (положительное число);

get_info() - метод для получения сводной информации о стране в виде строки:

"<название>: <площадь>, <численность населения>"
Пример использования классов (эти строчки в программе писать не нужно):

country = Country("Россия", 140000000, 324005489.55)
name = country.name
pop = country.population
country.population = 150000000
country.square = 354005483.0
print(country.get_info()) # Россия: 354005483.0, 150000000
P.S. В программе требуется объявить только классы. На экран выводить ничего не нужно.

'''

#ПРИМЕР ИСПОЛЬЗОВАНИЯ АБСТРАКТНЫХ МЕТОДОВ СО СВОЙСТВОМ PROPERTY + ПРОВЕРКА ПРИ ИНИЦИАЛИЗАЦИИ ЧЕРЕЗ СВОЙСТВО.


from abc import ABC, abstractmethod

class CountryInterface(ABC):

    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        pass

    @property
    @abstractmethod
    def population(self):
        pass

    @population.setter
    @abstractmethod
    def population(self, value):
        pass

    @property
    @abstractmethod
    def square(self):
        pass

    @square.setter
    @abstractmethod
    def square(self, value):
        pass

    @abstractmethod
    def get_info(self):
        pass


class Country(CountryInterface):

    def __init__(self, name, population, square):
        self.name = name
        self.population = population
        self.square = square

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value,str):
            self._name = value
        else:
            raise ValueError()

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, value):
        if isinstance(value,int) and value > 0:
            self._population = value
        else:
            raise ValueError()

    @property
    def square(self):
        return self._square

    @square.setter
    def square(self, value):
        if isinstance(value,(int,float)) and value > 0:
            self._square = value
        else:
            raise ValueError()

    def get_info(self):
        st = f'{self.name}: {self.square}, {self.population}'
        return st

country = Country('Страна', 140000000, 324005489.55)
name = country.name
pop = country.population
country.population = 150000000
country.square = 354005483.0
print(country.get_info()) # Страна: 354005483.0, 150000000



