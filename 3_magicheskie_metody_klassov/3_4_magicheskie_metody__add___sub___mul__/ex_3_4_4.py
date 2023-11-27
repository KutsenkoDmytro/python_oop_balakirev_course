'''
Подвиг 4. (task_1.py)

Известно, что в Python мы можем соединять два списка между собой с помощью оператора +:

lst = [1, 2, 3] + [4.5, -3.6, 0.78]
Но нет реализации оператора -, который бы убирал из списка соответствующие значения вычитаемого списка, как это показано в примере:

lst = [1, 2, 3, 4, 5, 6] - [5, 6, 7, 8, 1] # [2, 3, 4] (порядок следования оставшихся элементов списка должен сохраняться)
Давайте это поправим и создадим такой функционал. Для этого нужно объявить класс с именем NewList, объекты которого создаются командами:

lst = NewList() # пустой список
lst = NewList([-1, 0, 7.56, True]) # список с начальными значениями
Реализуйте для этого класса работу с оператором вычитания, чтобы над объектами класса NewList можно было выполнять следующие действия:

lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2 # NewList: [-4, 6, 10, 11, 15, False]
lst1 -= lst2 # NewList: [-4, 6, 10, 11, 15, False]
res_2 = lst2 - [0, True] # NewList: [1, 2, 3]
res_3 = [1, 2, 3, 4.5] - res_2 # NewList: [4.5]
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]
Также в классе NewList необходимо объявить метод:

get_list() - для возвращения результирующего списка объекта класса NewList

Например:

lst = res_2.get_list() # [1, 2, 3]
P.S. В программе требуется только объявить класс. На экран ничего выводить не нужно.

'''


class NewList:

    def __init__(self, lst = None):
        if lst is None:
            lst = []
        self.lst_values = lst

    def __sub__(self, other):
        self.__check_type_l_m(other)
        new_lst = self.__get_substract_list(other)

        return self.__class__(new_lst)

    def __rsub__(self, other):
        return self.__class__(other) - self.lst_values

    def __isub__(self, other):
        self.__check_type_l_m(other)
        new_lst = self.__get_substract_list(other)
        self.lst_values = new_lst
        return self

    def __get_substract_list(self, other):

        ptr = other.lst_values if isinstance(other, self.__class__) else other
        bool_other = [i for i in ptr if type(i) is bool]
        else_t_other = [i for i in ptr if type(i) is not bool]
        new_lst = []
        for i in self.lst_values:
            if type(i) is bool and i in bool_other:
                bool_other.remove(i)
            elif type(i) is bool and i not in bool_other:
                new_lst.append(i)
            elif i in else_t_other:
                else_t_other.remove(i)
            elif i not in else_t_other:
                new_lst.append(i)

        return new_lst

    def get_list(self):
        return self.lst_values

    @classmethod
    def __check_type_l_m(cls, value):
        if not isinstance(value, (list , cls)):
            raise TypeError('Неверный тип данных.')

# # Для проверки.
# lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
# lst2 = NewList([0, 1, 2, 3, True])
# res_1 = lst1 - lst2  # NewList: [-4, 6, 10, 11, 15, False]
# lst1 -= lst2  # NewList: [-4, 6, 10, 11, 15, False]
# res_2 = lst2 - [0, True]  # NewList: [1, 2, 3]
# res_3 = [1, 2, 3, 4.5] - res_2  # NewList: [4.5]
# a = NewList([2, 3])
# res_4 = [1, 2, 2, 3] - a  # NewList: [1, 2]
# print(res_4.get_list())
