'''
Подвиг 4. (task_2.py)

Вам необходимо объявить базовый класс ShopInterface с абстрактным методом:

def get_id(self): ...
В самом методе должно генерироваться исключение командой:

raise NotImplementedError('в классе не переопределен метод get_id')
Инициализатор в классе ShopInterface прописывать не нужно.

Далее объявите дочерний класс ShopItem (от базового класса ShopInterface), объекты которого создаются командой:

item = ShopItem(name, weight, price)
где name - название товара (строка); weight - вес товара (любое положительное число); price - цена товара (любое положительное число).

В каждом объекте класса ShopItem должны формироваться локальные атрибуты с именами _name, _weight, _price и соответствующими значениями. Также в объектах класса ShopItem должен автоматически формироваться локальный приватный атрибут __id с уникальным (для каждого товара) целым значением.

В классе ShopItem необходимо переопределить метод get_id() базового класса так, чтобы он (метод) возвращал значение атрибута __id.

P.S. В программе требуется объявить только классы. На экран выводить ничего не нужно.

'''

#from abc import ABC, abstractmethod

class ShopInterface:

    def get_id(self):
        raise NotImplementedError('в классе не переопределен метод get_id')

class ShopItem:
    __counter = 0

    def __new__(cls, *args, **kwargs):
        cls.__counter +=1
        return super().__new__(cls)

    def __init__(self, name, weight, price):
        self.__id = self.__counter
        self._name = name
        self._weight = weight
        self._price = price

    def get_id(self):
        return self.__id


