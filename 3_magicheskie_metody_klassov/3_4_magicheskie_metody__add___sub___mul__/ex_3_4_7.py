'''
Подвиг 7. (task_4.py)

Вам поручается создать программу по учету книг (библиотеку). Для этого необходимо в программе объявить два класса:

Lib - для представления библиотеки в целом;
Book - для описания отдельной книги.

Объекты класса Book должны создаваться командой:

book = Book(title, author, year)
где title - заголовок книги (строка); author - автор книги (строка); year - год издания (целое число).

Объекты класса Lib создаются командой:

lib = Lib()
Каждый объект должен содержать локальный публичный атрибут:

book_list - ссылка на список из книг (объектов класса Book). Изначально список пустой.

Также объекты класса Lib должны работать со следующими операторами:

lib = lib + book # добавление новой книги в библиотеку
lib += book

lib = lib - book # удаление книги book из библиотеки (удаление происходит по ранее созданному объекту book класса Book)
lib -= book

lib = lib - indx # удаление книги по ее порядковому номеру (индексу: отсчет начинается с нуля)
lib -= indx
При реализации бинарных операторов + и - создавать копии библиотек (объекты класса Lib) не нужно.

Также с объектами класса Lib должна работать функция:

n = len(lib) # n - число книг
которая возвращает число книг в библиотеке.

P.S. В программе достаточно только объявить классы. На экран ничего выводить не нужно.

'''


class Lib:

    def __init__(self):
        self.book_list = []

    def __add__(self, other):
        if self.__check_val_obj(other):
            self.book_list.append(other)
            return self
        else:
            raise ValueError('Не верный тип данных.')

    def __iadd__(self, other):
        return self + other

    def __sub__(self, other):
        if self.__check_val_obj(other):
            self.book_list.remove(other)
            return self
        elif self.__check_val_int(other):
            self.book_list.pop(other)
            return self
        else:
            raise ValueError('Не верный тип данных.')

    def __isub__(self, other):
        return self - other

    def __len__(self):
        return len(self.book_list)

    @staticmethod
    def __check_val_obj(value):
        return isinstance(value, Book)

    @staticmethod
    def __check_val_int(value):
        return type(value) is int



class Book:

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __setattr__(self, key, value):
        if key in {'title', 'author'}:
            self.__check_val_str(value)
        elif key == 'year':
            self.__check_val_int(value)
        object.__setattr__(self, key, value)

    @staticmethod
    def __check_val_str(value):
        if not isinstance(value, str):
            raise ValueError('Не верный тип данных.')

    @staticmethod
    def __check_val_int(value):
        if type(value) is not int:
            raise ValueError('Не верный тип данных.')




# # Для проверки.
# lib = Lib()
# book1 = Book('title1', 'author', 2022)
# book2 = Book('title2', 'author', 2022)
# book3 = Book('title3', 'author', 2022)
# book4 = Book('title4', 'author', 2022)
# book5 = Book('title5', 'author', 2022)
# book6 = Book('title6', 'author', 2022)
#
# lib = lib + book1
# lib += book2
# lib += book3
# lib += book4
# lib += book5
# lib += book6
#
# lib = lib - book4
# lib -= book3
#
# lib = lib - 1
# lib -= 0
# n = len(lib)
#
# print(n)
# print(lib.book_list)
