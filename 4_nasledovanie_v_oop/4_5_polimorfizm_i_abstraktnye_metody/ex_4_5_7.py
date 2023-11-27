'''
Подвиг 7. (task_5.py)

Используя информацию о модуле abc из предыдущего подвига 6, объявите базовый класс с именем StackInterface со следующими абстрактными методами:

def push_back(self, obj) - добавление объекта в конец стека;
def pop_back(self) - удаление последнего объекта из стека.

Stack

На основе этого класса объявите дочерний класс с именем Stack. Объекты этого класса должны создаваться командой:

st = Stack()
и в каждом объекте этого класса должен формироваться локальный атрибут:

_top - ссылка на первый объект стека (для пустого стека _top = None).

В самом классе Stack переопределить абстрактные методы базового класса:

def push_back(self, obj) - добавление объекта в конец стека;
def pop_back(self) - удаление последнего объекта из стека.

Сами объекты стека должны определяться классом StackObj и создаваться командой:

obj = StackObj(data)
где data - информация, хранящаяся в объекте (строка). В каждом объекте класса StackObj должны автоматически формироваться атрибуты:

_data - информация, хранящаяся в объекте (строка);
_next - ссылка на следующий объект стека (если следующий отсутствует, то _next = None).

Пример использования классов (эти строчки в программе писать не нужно):

st = Stack()
st.push_back(StackObj("obj 1"))
obj = StackObj("obj 2")
st.push_back(obj)
del_obj = st.pop_back() # del_obj - ссылка на удаленный объект (если объектов не было, то del_obj = None)
P.S. В программе требуется объявить только классы. На экран выводить ничего не нужно.

'''

from abc import ABC, abstractmethod


class StackInterface(ABC):

    @abstractmethod
    def push_back(self, obj):
        '''Добавление объекта в конец стека.'''
        pass

    @abstractmethod
    def pop_back(self, obj):
        '''Удаление последнего объекта из стека.'''
        pass


class StackObj:

    def __init__(self, data):
        self._data = data
        self._next = None


class Stack(StackInterface):

    def __init__(self):
        self._top = None

    def push_back(self, obj):
        '''Добавляет объект в конец списка.'''
        ptr = self._top
        if ptr == None:
            self._top = obj
        else:
            while ptr._next != None:
                ptr = ptr._next
            ptr._next = obj

    def pop_back(self):
        '''Удаляет объект из конца списка.'''
        ptr = self._top
        if ptr == None:  # Если нет объекта.
            del_obj = None
        elif ptr._next == None:  # Если он единственный.
            self._top = None
            del_obj = ptr
        else:
            while ptr._next._next != None:
                ptr = ptr._next
            # Получеем предпоследний объект списка (ptr) и делаем его последним в списке.
            del_obj = ptr._next
            ptr._next = None
        return del_obj


st = Stack()
st.push_back(StackObj("obj 1"))
obj = StackObj("obj 2")
st.push_back(obj)
del_obj = st.pop_back()  # del_obj - ссылка на удаленный объект (если объектов не было, то del_obj = None)
