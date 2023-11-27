'''
Подвиг 8. (task_4.py)

Вы несколько раз уже делали стек-подобную структуру, когда объекты последовательно связаны между собой:

Stack

Доведем ее функционал до конца. Для этого, по прежнему, нужно объявить классы:

Stack - для представления стека в целом;
StackObj - для представления отдельных объектов стека.

В классе Stack должны быть методы:

push_back(obj) - для добавления нового объекта obj в конец стека;
push_front(obj) - для добавления нового объекта obj в начало стека.

В каждом объекте класса Stack должен быть публичный атрибут:

top - ссылка на первый объект стека (при пустом стеке top = None).

Объекты класса StackObj создаются командой:

obj = StackObj(data)
где data - данные, хранящиеся в объекте стека (строка).

Также в каждом объекте класса StackObj должны быть публичные атрибуты:

data - ссылка на данные объекта;
next - ссылка на следующий объект стека (если его нет, то next = None).

Наконец, с объектами класса Stack должны выполняться следующие команды:

st = Stack()

st[indx] = value # замена прежних данных на новые по порядковому индексу (indx); отсчет начинается с нуля
data = st[indx]  # получение данных из объекта стека по индексу
n = len(st) # получение общего числа объектов стека

for obj in st: # перебор объектов стека (с начала и до конца)
    print(obj.data)  # отображение данных в консоль
При работе с индексами (indx), нужно проверять их корректность. Должно быть целое число от 0 до N-1, где N - число объектов в стеке. Иначе, генерировать исключение командой:

raise IndexError('неверный индекс')
P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.

'''


# ОДНОСВЯЗНЫЙ СПИСОК (ИНТЕРИРУЕМЫЙ ОБЪЕКТ)

class StackObj:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.top = None

    def push_back(self, obj):
        '''Для добавления нового объекта obj в конец стека.'''
        ptr = self.top
        if ptr == None:
            self.top = obj
        else:
            while ptr.next != None:  # Опускаемся в конец списка.
                ptr = ptr.next
            ptr.next = obj

    def push_front(self, obj):
        '''Для добавления нового объекта obj в начало стека.'''
        ptr = self.top
        if ptr == None:
            self.top = obj
        else:
            obj.next = ptr
            self.top = obj

    def get_atr(self, indx):
        '''Для получения элемента списка по индексу.'''
        ptr = self.top
        n = 0
        while n != indx:
            if ptr.next == None:
                break
            ptr = ptr.next
            n += 1
        if not 0 <= indx <= n:
            raise IndexError('неверный индекс')
        return ptr

    def get_lst(self):
        '''Для получения всех элементов списка.'''
        lst = []
        ptr = self.top
        while ptr:
            lst.append(ptr)
            ptr = ptr.next
        return lst

    def __getitem__(self, item):
        obj = self.get_atr(item)
        return obj.data

    def __setitem__(self, key, value):
        obj = self.get_atr(key)
        obj.data = value

    def __len__(self):
        return len(self.get_lst())

    def __iter__(self):
        self.i_val = 0
        return self

    def __next__(self):
        lst = self.get_lst()
        if self.i_val < len(lst):
            i_val_old = self.i_val
            self.i_val += 1
            return lst[i_val_old]
        else:
            raise StopIteration


# Для проверки.
st = Stack()
st.push_back(StackObj("1"))
st.push_front(StackObj("2"))
st[0] = "3"  # замена прежних данных на новые по порядковому индексу (indx); отсчет начинается с нуля
data = st[0]  # получение данных из объекта стека по индексу
n = len(st)  # получение общего числа объектов стека
print(data, n)

for obj in st:  # перебор объектов стека (с начала и до конца)
    print(obj.data)  # отображение данных в консоль
