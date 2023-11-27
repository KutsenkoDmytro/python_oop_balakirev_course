'''
Необходимо реализовать связный список (не список языка Python и не хранить объекты в списке Python),
когда объекты класса ObjList связаны с соседними через приватные свойства __next и __prev:
Для этого объявите класс LinkedList, который будет представлять связный список в целом и иметь набор следующих методов:

add_obj(self, obj) - добавление нового объекта obj класса ObjList в конец связного списка;
remove_obj(self) - удаление последнего объекта из связного списка;
get_data(self) - получение списка из строк локального свойства __data всех объектов связного списка.

И в каждом объекте этого класса должны создаваться локальные публичные атрибуты:

head - ссылка на первый объект связного списка (если список пустой, то head = None);
tail - ссылка на последний объект связного списка (если список пустой, то tail = None).

Объекты класса ObjList должны иметь следующий набор приватных локальных свойств:

__next - ссылка на следующий объект связного списка (если следующего объекта нет, то __next = None);
__prev - ссылка на предыдущий объект связного списка (если предыдущего объекта нет, то __prev = None);
__data - строка с данными.

Также в классе ObjList должны быть реализованы следующие сеттеры и геттеры:

set_next(self, obj) - изменение приватного свойства __next на значение obj;
set_prev(self, obj) - изменение приватного свойства __prev на значение obj;
get_next(self) - получение значения приватного свойства __next;
get_prev(self) - получение значения приватного свойства __prev;
**set_data(self, data)__ - изменение приватного свойства __data на значение data;
get_data(self) - получение значения приватного свойства __data.

Создавать объекты класса ObjList предполагается командой:

ob = ObjList("данные 1")
А использовать класс LinkedList следующим образом (пример, эти строчки писать в программе не нужно):

lst = LinkedList()
lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))
res = lst.get_data()    # ['данные 1', 'данные 2', 'данные 3']
Объявите в программе классы LinkedList и ObjList в соответствии с заданием.

'''


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):  # push_back()

        if self.head == None:
            self.head = obj  # если голова списка = None, помещаем созданный елемент в голову списка

        if self.tail != None:  # если хвост списка != None
            obj.set_prev(self.tail)  # атрибуту __prev созданного объекта присваиваем ссылку на объект в хвосте
            self.tail.set_next(obj)  # атрибуту __next объекта в хвосте присваиваем ссылку на созданный объект
        self.tail = obj  # помещаем созданный элемент в хвост списка

    def remove_obj(self):
        if self.head != self.tail:
            self.tail = self.tail.get_prew()
            self.tail.set_next(None)
        else:
            self.head = None
            self.tail = None

    def get_data(self):
        ptr = self.head
        lst = []

        while ptr:
            lst.append(ptr.get_data())
            ptr = ptr.get_next()
        return lst


class ObjList:

    def __init__(self, data):
        self.__next = None  # следующий объект
        self.__prev = None  # предыдущий объект
        self.__data = data

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prew(self):
        return self.__prev

    def set_data(self, data):  # не нужный метод
        pass

    def get_data(self):
        return self.__data


lst = LinkedList()
lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))
lst.add_obj(ObjList("данные 4"))
lst.remove_obj()
lst.remove_obj()

# # Для проверки.
print(lst.get_data())
