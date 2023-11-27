'''
Реализуйте односвязный список (не список Python, не использовать список Python для хранения объектов), когда один объект ссылается на следующий и так по цепочке до последнего:
Для этого объявите в программе два класса:

StackObj - для описания объектов односвязного списка;
Stack - для управления односвязным списком.

Объекты класса StackObj предполагается создавать командой:

obj = StackObj(данные)
Здесь данные - это строка с некоторым содержимым. Каждый объект класса StackObj должен иметь следующие локальные приватные атрибуты:

__data - ссылка на строку с данными, указанными при создании объекта;
__next - ссылка на следующий объект класса StackObj (при создании объекта принимает значение None).

Также в классе StackObj должны быть объявлены объекты-свойства:

next - для записи и считывания информации из локального приватного свойства __next;
data - для записи и считывания информации из локального приватного свойства __data.

При записи необходимо реализовать проверку, что __next будет ссылаться на объект класса StackObj или значение None. Если проверка не проходит, то __next остается без изменений.

Класс Stack предполагается использовать следующим образом:

st = Stack() # создание объекта односвязного списка
В объектах класса Stack должен быть локальный публичный атрибут:

top - ссылка на первый добавленный объект односвязного списка (если список пуст, то top = None).

А в самом классе Stack следующие методы:

push(self, obj) - добавление объекта класса StackObj в конец односвязного списка;
pop(self) - извлечение последнего объекта с его удалением из односвязного списка;

get_data(self) - получение списка из объектов односвязного списка
(список из строк локального атрибута __data каждого объекта в порядке их добавления, или пустой список, если объектов нет).

Пример использования классов Stack и StackObj (эти строчки в программе писать не нужно):

st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.pop()
res = st.get_data()    # ['obj1', 'obj2']
'''


# Пример реализации без создания дополнительных локальных атрибутов в StackObj и Stack

class StackObj:

    def __init__(self, data):
        self.__next = None
        self.__data = data

    # объект-свойство next
    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if self.__check_next(obj):
            self.__next = obj

    # объект-свойство data
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @classmethod
    def __check_next(cls, obj):
        return type(obj) == cls or obj == None


class Stack:

    def __init__(self):
        self.top = None

    def push(self, obj):
        if self.top == None:
            self.top = obj
        else:
            top = self.top
            end = top
            while end.next != None:
                end = end.next
            end.next = obj

    def pop(self):
        if self.top == None:
            return
        elif self.top.next == None:
            res = self.top
            self.top = None
        else:
            ptr = self.top
            while ptr.next.next != None:
                ptr = ptr.next
            res = ptr.next
            ptr.next = None
        return res

    def get_data(self):
        lst_res = []
        ptr = self.top
        while ptr != None:
            lst_res.append(ptr.data)
            ptr = ptr.next
        return lst_res


'''
class Stack:

    def __init__(self):
        self.top = None
        self.end = None

    def push(self, obj):
        if self.top == self.end == None:
            self.top = obj
        else:
            self.end.next = obj
        self.end = obj

    def pop(self):
        if self.end == None:
            return
        elif self.end == self.top:
            res = self.top
            self.end = self.top = None
        else:
            ptr = self.top
            while ptr.next.next != None:
                ptr = ptr.next
            res = ptr.next
            ptr.next = None
            self.end = ptr
        return res

    def get_data(self):
        lst_res = []
        ptr = self.top
        while ptr != None:
            lst_res.append(ptr.data)
            ptr = ptr.next
        return lst_res
'''

st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.pop()


res = st.get_data()

# # Для проверки.
# print(res)
