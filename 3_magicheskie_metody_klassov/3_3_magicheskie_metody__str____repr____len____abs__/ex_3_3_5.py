'''
Подвиг 5. Объявите класс LinkedList (связный список) для работы со следующей структурой данных:



Здесь создается список из связанных между собой объектов класса ObjList. Объекты этого класса создаются командой:

obj = ObjList(data)
где data - строка с некоторой информацией. Также в каждом объекте obj класса ObjList должны создаваться следующие локальные атрибуты:

__data - ссылка на строку с данными;
__prev - ссылка на предыдущий объект связного списка (если объекта нет, то __prev = None);
__next - ссылка на следующий объект связного списка (если объекта нет, то __next = None).

В свою очередь, объекты класса LinkedList должны создаваться командой:

linked_lst = LinkedList()
и содержать локальные атрибуты:

head - ссылка на первый объект связного списка (если список пуст, то head = None);
tail - ссылка на последний объект связного списка (если список пуст, то tail = None).

А сам класс содержать следующие методы:

add_obj(obj) - добавление нового объекта obj класса ObjList в конец связного списка;
remove_obj(indx) - удаление объекта класса ObjList из связного списка по его порядковому номеру (индексу); индекс отсчитывается с нуля.

Также с объектами класса LinkedList должны поддерживаться следующие операции:

len(linked_lst) - возвращает число объектов в связном списке;
linked_lst(indx) - возвращает строку __data, хранящуюся в объекте класса ObjList, расположенного под индексом indx (в связном списке).

Пример использования классов (эти строчки в программе писать не нужно):

linked_lst = LinkedList()
linked_lst.add_obj(ObjList("Sergey"))
linked_lst.add_obj(ObjList("Balakirev"))
linked_lst.add_obj(ObjList("Python"))
linked_lst.remove_obj(2)
linked_lst.add_obj(ObjList("Python ООП"))
n = len(linked_lst)  # n = 3
s = linked_lst(1) # s = Balakirev
P.S. На экран в программе ничего выводить не нужно.


'''
# ДВУХСВЯЗНЫЙ СПИСОК


class ValidateObjList:
    '''Дескриптор атрибутов класса ObjList.'''

    def __set_name__(self, owner, name):
        self.name = f'_{owner.__name__}__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class ObjList:
    data = ValidateObjList()
    prev = ValidateObjList()
    next = ValidateObjList()

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        if self.head == None:
            self.head = obj
        if self.tail != None:
            self.tail.next = obj
            obj.prev = self.tail
        self.tail = obj

    def get_obj(self, indx):
        ptr = self.head
        n = 0
        while n < indx:
            if ptr == None:
                return None
            ptr = ptr.next
            n += 1
        return ptr

    def remove_obj(self, indx):
        ptr = self.get_obj(indx)
        if ptr != None:
            if ptr == self.head == self.tail:  # Если удаляем единственный элемент.
                self.head = self.tail = None
            elif ptr == self.head:  # Если удаляем первый элемент.
                ptr.next.prev = None
                self.head = ptr.next
            elif ptr == self.tail:  # Если удаляем последний элемент.
                ptr.prev.next = None
                self.tail = ptr.prev
            else:
                ptr.prev.next = ptr.next  # Если удаляем промежуточный элемент.
                ptr.next.prev = ptr.prev
            del ptr

    def get_objs_list(self):
        lst = []
        ptr = self.head
        while ptr:
            lst.append(ptr.data)
            ptr = ptr.next
        return lst

    def __len__(self):
        return len(self.get_objs_list())

    def __call__(self, indx, *args, **kwargs):
        ptr = self.get_obj(indx)
        if ptr != None:
            return ptr.data

# # Для проверки.
# linked_lst = LinkedList()
# linked_lst.add_obj(ObjList("Sergey"))
# linked_lst.add_obj(ObjList("Balakirev"))
# linked_lst.add_obj(ObjList("Python"))
# linked_lst.remove_obj(2)
# linked_lst.add_obj(ObjList("Python ООП"))
# n = len(linked_lst)  # n = 3
# s = linked_lst(1) # s = Balakirev
# print(n)
# print(s)