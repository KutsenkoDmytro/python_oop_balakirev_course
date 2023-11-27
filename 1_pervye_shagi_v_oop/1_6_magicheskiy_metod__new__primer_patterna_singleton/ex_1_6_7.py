'''
ex. 7
Объявите класс SingletonFive, с помощью которого можно было бы создавать объекты командой:

a = SingletonFive(<наименование>)
Здесь <наименование> - это данные, которые сохраняются в локальном свойстве name созданного объекта.

Этот класс должен формировать только первые пять объектов. Остальные (шестой, седьмой и т.д.) должны быть ссылкой на последний (пятый) созданный объект.

Создайте первые десять объектов класса SingletonFive с помощью следующего фрагмента программы:

objs = [SingletonFive(str(n)) for n in range(10)]
'''


class SingletonFive:
    '''
    Позволяет создавать до 5ти екземпляров (включительно).
    '''
    __list_inst = []

    def __new__(cls, *args, **kwargs):
        if len(cls.__list_inst) < 5:
            cls.__list_inst.append(super().__new__(cls))

        return cls.__list_inst[-1]

    def __init__(self, name):
        self.name = name


objs = [SingletonFive(str(n)) for n in range(10)]
print(objs)
