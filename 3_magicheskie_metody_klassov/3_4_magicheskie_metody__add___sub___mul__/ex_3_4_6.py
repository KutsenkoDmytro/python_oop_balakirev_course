'''
Подвиг 6. (task_3.py)

Ранее, в одном из подвигов мы с вами создавали односвязный список с объектами класса StackObj (когда один объект ссылается на следующий и так далее):

Stack

Давайте снова создадим такую структуру данных. Для этого объявим два класса:

Stack - для управления односвязным списком в целом;
StackObj - для представления отдельных объектов в односвязным списком.

Объекты класса StackObj должны создаваться командой:

obj = StackObj(data)
где data - строка с некоторыми данными.

Каждый объект класса StackObj должен иметь локальные приватные атрибуты:

__data - ссылка на строку с переданными данными;
__next - ссылка на следующий объект односвязного списка (если следующего нет, то __next = None).

Объекты класса Stack создаются командой:

st = Stack()
и каждый из них должен содержать локальный атрибут:

top - ссылка на первый объект односвязного списка (если объектов нет, то top = None).

Также в классе Stack следует объявить следующие методы:

push_back(self, obj) - добавление объекта класса StackObj в конец односвязного списка;
pop_back(self) - удаление последнего объекта из односвязного списка.

Дополнительно нужно реализовать следующий функционал (в этих операциях копии односвязного списка создавать не нужно):

# добавление нового объекта класса StackObj в конец односвязного списка st
st = st + obj
st += obj

# добавление нескольких объектов в конец односвязного списка
st = st * ['data_1', 'data_2', ..., 'data_N']
st *= ['data_1', 'data_2', ..., 'data_N']
В последних двух строчках должны автоматически создаваться N объектов класса StackObj с данными, взятыми из списка (каждый элемент списка для очередного добавляемого объекта).

P.S. В программе достаточно только объявить классы. На экран ничего выводить не нужно.

'''


class StackObj:

    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        self.__next = next


class Stack:

    def __init__(self):
        self.top = None

    def push_back(self, obj):
        if self.top == None:
            self.top = obj
        else:
            ptr = self.top
            while ptr.next != None:
                ptr = ptr.next
            ptr.next = obj

    def pop_back(self):
        ptr = self.top
        if ptr.next == None:  # Если существует один элемент списка.
            self.top = None
        else:
            while ptr.next.next != None:
                ptr = ptr.next
            ptr.next = None

    def get_lst_data(self):
        '''Пользовательский метод для вывода данных всех элементов списка.'''
        lst = []
        ptr = self.top
        while ptr != None:
            lst.append(ptr.data)
            ptr = ptr.next
        return lst

    @staticmethod
    def check_val_obj(value):
        if not isinstance(value, StackObj):
            raise ValueError('Не верный тип данных.')

    @staticmethod
    def check_val_lst(value):
        if not isinstance(value, list):
            raise ValueError('Не верный тип данных.')

    def __add__(self, other):
        self.check_val_obj(other)
        self.push_back(other)
        return self

    def __iadd__(self, other):
        self.check_val_obj(other)
        return self + other

    def __mul__(self, other):
        self.check_val_lst(other)
        lst = [StackObj(dt) for dt in other]
        for obj in lst:
            self.push_back(obj)
        return self

    def __imul__(self, other):
        self.check_val_lst(other)
        return self * other

# #Для проверки.
# st = Stack()
# st.push_back(StackObj('data_1'))
# st.push_back(StackObj('data_2'))
# st.push_back(StackObj('data_3'))
# st.push_back(StackObj('data_4'))
# st.pop_back()
# st = st + StackObj('data_q')
# st = st * ['data_a', 'data_b', 'data_c']
# st *= ['data_d', 'data_e', 'data_f']
# print(st.get_lst_data())
