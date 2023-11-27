'''
ex. 2.
Объявите класс Money так, чтобы объекты этого класса можно было создавать следующим образом:

my_money = Money(100)
your_money = Money(1000)
Здесь при создании объектов указывается количество денег, которое должно сохраняться
в локальном свойстве (атрибуте) money каждого экземпляра класса.


'''


class Money:
    def __init__(self, money):
        self.money = money


my_money = Money(100)
your_money = Money(1000)

# Для проверки.
# print(my_money.__dict__)
# print(your_money.__dict__)
