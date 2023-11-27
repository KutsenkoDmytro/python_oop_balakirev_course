'''
Объявите класс с именем Money и определите в нем следующие переменные и методы:

приватная локальная переменная money (целочисленная) для хранения количества денег (своя для каждого объекта класса Money);
публичный метод set_money(money) для передачи нового значения приватной локальной переменной money (изменение выполняется только если метод check_money(money) возвращает значение True);
публичный метод get_money() для получения текущего объема средств (денег);
публичный метод add_money(mn) для прибавления средств из объекта mn класса Money к средствам текущего объекта;
приватный метод класса check_money(money) для проверки корректности объема средств в параметре money (возвращает True, если значение корректно и False - в противном случае).
Проверка корректности выполняется по критерию: параметр money должен быть целым числом, больше или равным нулю.

'''


class Money:

    def __init__(self, money):
        self.__money = 0
        if self.__check_money(money):
            self.__money = money

    def set_money(self, money):
        if self.__check_money(money):
            self.__money = money
        else:
            raise ValueError('не верный формат данных')

    def get_money(self):
        return self.__money

    def add_money(self, mn):
        self.__money += mn.get_money()


    @classmethod
    def __check_money(cls, money):
        return type(money) is int and money >= 0

# # Для проверки.
# mn_1 = Money(500)
# mn_2 = Money(300)
# mn_1.add_money(mn_2)
# print(mn_1.get_money())