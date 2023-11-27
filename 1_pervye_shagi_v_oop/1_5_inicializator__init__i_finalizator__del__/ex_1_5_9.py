'''
Вам необходимо реализовать односвязный список (не список языка Python, объекты в
списке не хранить, а формировать связанную структуру, показанную на рисунке) из объектов класса ListObject:

Для этого объявите в программе класс ListObject, объекты которого создаются командой:

obj = ListObject(data)
Каждый объект класса ListObject должен содержать локальные свойства:

next_obj - ссылка на следующий присоединенный объект (если следующего объекта нет, то next_obj = None);
data - данные объекта в виде строки.

В самом классе ListObject должен быть объявлен метод:

link(self, obj) - для присоединения объекта obj такого же класса к текущему объекту
self (то есть, атрибут next_obj объекта self должен ссылаться на obj).

Прочитайте список строк из входного потока командой:

lst_in = list(map(str.strip, sys.stdin.readlines()))
Затем сформируйте односвязный список, в объектах которых (в атрибуте data) хранятся
строки из списка lst_in (первая строка в первом объекте, вторая - во втором и т.д.).
На первый добавленный объект класса ListObject должна ссылаться переменная head_obj.

'''

class ListObject:

    def __init__(self, data):
        self.data = data
        self.next_obj = None

    def link(self, obj):
        self.next_obj = obj


sub_list = ['tree',
            '[A-Z]',
            'filter: FX - 2000',
            'E:equal, D:dodge',
            '555',
            'del',
            'Singleton']


head_obj = ListObject(sub_list.pop(0))
head = head_obj

for i in range(len(sub_list)):
    cur_obj = ListObject(sub_list.pop(0))
    head.link(cur_obj)
    head = cur_obj


next = head_obj.next_obj
print(head_obj,head_obj.__dict__)
while next:
    print(next,next.__dict__)
    next = next.next_obj

'''
# Рекурсией

class ListObject:
    next_obj = None

    def __init__(self, data):
        self.data = data[0]
        if len(data[1:])!=0:
            self.link(ListObject(data[1:]))

    def link(self, obj):
        self.next_obj = obj


sub_list = ['tree',
            '[A-Z]',
            'filter: FX - 2000',
            'E:equal, D:dodge',
            '555',
            'del',
            'Singleton']

linked_list = ListObject(sub_list)


'''

