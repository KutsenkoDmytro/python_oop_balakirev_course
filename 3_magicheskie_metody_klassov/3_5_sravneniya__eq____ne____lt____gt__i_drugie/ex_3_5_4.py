'''
Подвиг 4. (task_2.py)

Объявите класс Dimensions (габариты) с атрибутами:

MIN_DIMENSION = 10
MAX_DIMENSION = 10000
Каждый объект класса Dimensions должен создаваться командой:

d3 = Dimensions(a, b, c)   # a, b, c - габаритные размеры
Значения a, b, c должны сохраняться в локальных приватных атрибутах __a, __b, __c объектах этого класса.

Для изменения и доступа к приватным атрибутам в классе Dimensions должны быть объявлены объекты-свойства (property) с именами: a, b, c. Причем, в момент присваивания нового значения должна выполняться проверка попадания числа в диапазон [MIN_DIMENSION; MAX_DIMENSION]. Если число не попадает, то оно игнорируется и существующее значение не меняется.

С объектами класса Dimensions должны выполняться следующие операторы сравнения:

dim1 >= dim2   # True, если объем dim1 больше или равен объему dim2
dim1 > dim2    # True, если объем dim1 больше объема dim2
dim1 <= dim2   # True, если объем dim1 меньше или равен объему dim2
dim1 < dim2    # True, если объем dim1 меньше объема dim2
Объявите в программе еще один класс с именем ShopItem (товар), объекты которого создаются командой:

item = ShopItem(name, price, dim)
где name - название товара (строка); price - цена товара (целое или вещественное число); dim - габариты товара (объект класса Dimensions).

В каждом объекте класса ShopItem должны создаваться локальные атрибуты:

name - название товара;
price - цена товара;
dim - габариты товара (объект класса Dimensions).

Создайте список с именем lst_shop из четырех товаров со следующими данными:

- кеды; 1024; (40, 30, 120)
- зонт; 500.24; (10, 20, 50)
- холодильник; 40000; (2000, 600, 500)
- табуретка; 2000.99; (500, 200, 200)

Сформируйте новый список lst_shop_sorted с упорядоченными по возрастанию объема (габаритов) товаров списка lst_shop, используя стандартную функцию sorted() языка Python и ее параметр key для настройки сортировки. Прежний список lst_shop должен оставаться без изменений.

P.S. На экран в программе ничего выводить не нужно.


'''


class Demensions:
    '''Описывает габариты товара.'''

    MIN_DEMENSIONS = 10
    MAX_DEMENSIONS = 10000

    def __init__(self, a, b, c):
        if False in [self.__check_num_in_range(i) for i in [a, b, c]]:
            raise ValueError('Не верный тип данных.')
        else:
            self.__a = a
            self.__b = b
            self.__c = c

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, val):
        if self.__check_val_obj(val):
            self.__a = val

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, val):
        if self.__check_val_obj(val):
            self.__b = val

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, val):
        if self.__check_val_obj(val):
            self.__c = val

    def __gt__(self, other):
        self.__check_val_obj(other)
        return self.get_volume_rect() >= other.get_volume_rect()

    def __ge__(self, other):
        self.__check_val_obj(other)
        return self.get_volume_rect() > other.get_volume_rect()

    def get_volume_rect(self):
        return self.a * self.b * self.c

    @classmethod
    def __check_val_obj(cls, value):
        if not isinstance(value, cls):
            raise ValueError('Не верный тип данных.')

    @classmethod
    def __check_num_in_range(cls, value: int):
        return type(value) in {int, float} and \
            cls.MIN_DEMENSIONS <= value <= cls.MAX_DEMENSIONS


class ShopItem:
    '''Описывает товар.'''

    def __init__(self, name, price, dim):
        self.name = name
        self.price = price
        self.dim = Demensions(*dim)


t1 = ShopItem('кеды', 1024, (40, 30, 120))
t2 = ShopItem('зонт', 500.24, (10, 20, 50))
t3 = ShopItem('холодильник', 40000, (2000, 600, 500))
t4 = ShopItem('табуретка', 2000.99, (500, 200, 200))

lst_shop = [t1, t2, t3, t4]
lst_shop_sorted = sorted(lst_shop, key = lambda x: x.dim)


# # Для проверки.
# print(f'id: {id(lst_shop)}')
# for i in lst_shop:
#     print(i.dim.get_volume_rect())
# print('====================')
# print(f'id: {id(lst_shop_sorted)}')
# for i in lst_shop_sorted:
#     print(i.dim.get_volume_rect())


