'''
Подвиг 3. (task_1.py)

Создается проект, в котором предполагается использовать списки из целых чисел. Для этого вам ставится задача создать класс с именем ListInteger с базовым классом list и переопределить три метода:

__init__()
__setitem__()
append()

так, чтобы список ListInteger содержал только целые числа. При попытке присвоить любой другой тип данных, генерировать исключение командой:

raise TypeError('можно передавать только целочисленные значения')
Пример использования класса ListInteger (эти строчки в программе не писать):

s = ListInteger((1, 2, 3))
s[1] = 10
s.append(11)
print(s)
s[0] = 10.5 # TypeError
P.S. В программе нужно объявить только класс. На экран выводить ничего не нужно.

'''
#ПЕРЕОПРЕДЕЛЕНИЕ МЕТОДОВ СПИСКА


class ListInteger(list):

    def __init__(self,lst, *args):
        for i in lst:
            self.__check_int(i)
        super().__init__(lst)

    def __setitem__(self, key, value):
        self.__check_int(value)
        super().__setitem__(key,value)

    def append(self, value):
        self.__check_int(value)
        super().append(value)

    @staticmethod
    def __check_int(value):
        if not type(value) is int:
            raise TypeError('можно передавать только целочисленные значения')


s = ListInteger((1, 2, 3))
s[1] = 10
s.append(11)
print(s)
#s[0] = 10.5 # TypeError