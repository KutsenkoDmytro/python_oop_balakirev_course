'''
Объявите в программе класс Cart (корзина), объекты которого создаются командой:

cart = Cart()
Каждый объект класса Cart должен иметь локальное свойство goods - список объектов
для покупки (объекты классов Table, TV, Notebook и Cup). Изначально этот список должен быть пустым.

В классе Cart объявить методы:

add(self, gd) - добавление в корзину товара, представленного объектом gd;
remove(self, indx) - удаление из корзины товара по индексу indx;
get_list(self) - получение из корзины товаров в виде списка из строк:

['<наименовние_1>: <цена_1>',
'<наименовние_2>: <цена_2>',
...
'<наименовние_N>: <цена_N>']
Объявите в программе следующие классы для описания товаров:

Table - столы;
TV - телевизоры;
Notebook - ноутбуки;
Cup - кружки.

Объекты этих классов должны создаваться командой:

gd = ИмяКласса(name, price)
Каждый объект классов товаров должен содержать локальные свойства:

name - наименование;
price - цена.

Создайте в программе объект cart класса Cart. Добавьте в него два телевизора (TV),
один стол (Table), два ноутбука (Notebook) и одну кружку (Cup). Названия и цены придумайте сами.

'''


class Cart:
    '''Описание корзины.'''

    def __init__(self):
        self.goods = []

    def add(self, gd):
        '''Добавляет товар в корзину.'''
        self.goods.append(gd)

    def remove(self, indx):
        '''Удаляет из корзины товар по индексу.'''
        self.goods.pop(indx)

    def get_list(self):
        '''Получение из корзины товаров в виде списка из строк.'''
        gd_lst = [f'{gd.name}: {gd.price}' for gd in self.goods]
        return gd_lst


class Table:
    '''Описание столов.'''

    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV:
    '''Описание телевизоров.'''

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook:
    '''Описание ноутбуков.'''

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cap:
    '''Описание кружок.'''

    def __init__(self, name, price):
        self.name = name
        self.price = price


cart = Cart()
lst_goods = [TV('Samsung', 6000), TV('LG', 5500), TV('Bravis', 3000),
             Table('Sonata', 1200), Notebook('HP', 23000),
             Notebook('Asus', 25000), Cap('Smile', 100)]
for obj in lst_goods:
    cart.add(obj)

# # Для проверки.
# print(cart.__dict__)
