'''
Подвиг 6. (task_5.py) - мое исполнение (task_5_1.py) - еще вариант исполнения

Ранее вы уже создавали стек-подобную структуру, когда один объект ссылается на следующий и так по цепочке до последнего:

Stack

Для этого в программе объявлялись два класса:

StackObj - для описания объектов стека;
Stack - для управления стек-подобной структурой.

И, далее, объекты класса StackObj следовало создавать командой:

obj = StackObj(data)
где data - это строка с некоторым содержимым объекта (данными). При этом каждый объект класса StackObj должен иметь следующие локальные атрибуты:

data - ссылка на строку с данными, указанными при создании объекта;
next - ссылка на следующий объект класса StackObj (при создании объекта принимает значение None).

Класс Stack предполагается использовать следующим образом:

st = Stack() # создание объекта стек-подобной структуры
В каждом объекте класса Stack должен быть локальный публичный атрибут:

top - ссылка на первый объект стека (если стек пуст, то top = None).

А в самом классе Stack следующие методы:

push(self, obj) - добавление объекта класса StackObj в конец стека;
pop(self) - извлечение последнего объекта с его удалением из стека;

Дополнительно в классе Stack нужно объявить магические методы для обращения к объекту стека по его индексу, например:

obj_top = st[0] # получение первого объекта
obj = st[4] # получение 5-го объекта стека
st[2] = StackObj("obj3") # замена прежнего (3-го) объекта стека на новый
Если индекс не целое число или число меньше нуля или больше числа объектов в стеке, то должно генерироваться исключение командой:

raise IndexError('неверный индекс')
Пример использования классов Stack и StackObj (эти строчки в программе не писать):

st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st[1] = StackObj("new obj2")
print(st[2].data) # obj3
print(st[1].data) # new obj2
res = st[3] # исключение IndexError
P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.

'''


class StackObj:
    '''Для описания объектов стека.'''

    def __init__(self, data):
        self.next = None
        self.data = data


class Stack:
    '''Для управления стек-подобной структурой.'''

    def __init__(self):
        self.top = None

    def push(self, obj):
        '''Добавление объекта класса StackObj в конец стека.'''
        ptr = self.top
        if ptr == None:
            self.top = obj
        else:
            while ptr.next != None:
                ptr = ptr.next
            ptr.next = obj

    def pop(self):  # pop_back
        '''Извлечение последнего объекта с его удалением из стека.'''
        ptr = self.top
        if ptr == None:
            del_obj = None
        elif ptr.next == None:
            del_obj = ptr
            self.top = None
        else:
            while ptr.next.next != None:
                ptr = ptr.next
            del_obj = ptr.next
            ptr.next = None
        return del_obj

    def get_at(self, index):
        '''Получение объекта из стека по индексу.'''
        ptr = self.top
        counter = 0
        while counter != index:
            if ptr.next == None:
                break
            counter += 1
            ptr = ptr.next
        if not 0 <= index <= counter:
            raise IndexError('неверный индекс')
        return ptr

    def __getitem__(self, item):
        return self.get_at(item)

    def __setitem__(self, key, value):
        ptr = self.top
        target = self.get_at(
            key)  # Получаем текущий объект находящийся под указанным индексом.
        if ptr == target:  # Если объект замены находится в голове списка.
            value.next = ptr.next
            self.top = value
        else:
            while ptr.next != target:  # Если объет замены находится дальше в списке.
                ptr = ptr.next
            value.next = ptr.next.next  # Для атрибута next нового объекта устанавливаем значение соответствующего атрибута старого.
            ptr.next = value  # Атрибуту next предыдущего объекта присваиваем значение нового объекта.

    def get_obj_list(self):
        '''Возвращает все элементы односвязного списка.'''
        lst = []
        ptr = self.top
        while ptr:
            lst.append(ptr)
            ptr = ptr.next
        return lst


# Для проверки
st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
# print(st.get_obj_list())
st[1] = StackObj("new obj2")
print(st[2].data)  # obj3
print(st[1].data)  # new obj2
# res = st[3] # исключение IndexError
