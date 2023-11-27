'''

Подвиг 8. Вы начинаете создавать интернет-магазин. Для этого в программе объявляется класс SuperShop, объекты которого создаются командой:

myshop = SuperShop(название магазина)
В каждом объекте класса SuperShop должны формироваться следующие локальные атрибуты:

name - название магазина (строка);
goods - список из товаров.

Также в классе SuperShop должны быть методы:

add_product(product) - добавление товара в магазин (в конец списка goods);
remove_product(product) - удаление товара из магазина (из списка goods).

Здесь product - это объект класса Product, описывающий конкретный товар. В этом классе следует объявить следующие дескрипторы:

name = StringValue(min_length, max_length)    # min_length - минимально допустимая длина строки; max_length - максимально допустимая длина строки
price = PriceValue(max_value)    # max_value - максимально допустимое значение

Объекты класса Product будут создаваться командой:

pr = Product(наименование, цена)
Классы StringValue и PriceValue - это дескрипторы данных.
Класс StringValue должен проверять, что присваивается строковый тип с длиной строки в диапазоне [2; 50], т.е. min_length = 2, max_length = 50.
Класс PriceValue должен проверять, что присваивается вещественное или целочисленное значение в диапазоне [0; 10000], т.е. max_value = 10000.
Если проверки не проходят, то соответствующие (прежние) значения меняться не должны.

Пример использования класса SuperShop (эти строчки в программе писать не нужно):

shop = SuperShop("У Балакирева")
shop.add_product(Product("Курс по Python", 0))
shop.add_product(Product("Курс по Python ООП", 2000))
for p in shop.goods:
    print(f"{p.name}: {p.price}")
P.S. В программе требуется объявить классы с описанным функционалом. На экран в программе выводить ничего не нужно.

'''


class StringValue:
    '''Дескриптор данных (строка).'''

    def __validation_string(self, value):
        return type(value) is str and \
            self.min_length <= len(value) <= self.max_length

    def __init__(self, min_length=2, max_length=50):
        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.__validation_string(value):
            setattr(instance, self.name, value)


class PriceValue:
    '''Дескриптор данных (число).'''

    def __validation_number(self, value):
        return type(value) in {int, float} and \
            self.min_value <= value <= self.max_value

    def __init__(self, max_value=10000):
        self.max_value = max_value
        self.min_value = 0

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.__validation_number(value):
            setattr(instance, self.name, value)


class SuperShop:
    '''Описывает магазин.'''

    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        '''Добавляес товар в магазин (в конец списка goods).'''
        self.goods.append(product)

    def remove_product(self, product):
        '''Удаляет товар из магазина (из списка goods)'''
        self.goods.remove(product)


class Product:
    '''Описывает товар.'''
    name = StringValue()
    price = PriceValue()

    def __init__(self, name, price):
        self.name = name
        self.price = price


# # Для проверки.
# shop = SuperShop('MyShop')
# pr_1 = Product('ноутбук', 10000)
# pr_2 = Product('телефон', 6000)
#
#
# shop.add_product(pr_1)
# shop.add_product(pr_2)
# for prod in shop.goods:
#     print(prod.name, prod.price)
