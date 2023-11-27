'''
Вы создаете телефонную записную книжку.
Она определяется классом PhoneBook. Объекты этого класса создаются командой:

p = PhoneBook()
А сам класс должен иметь следующий набор методов:

add_phone(phone) - добавление нового номера телефона (в список);
remove_phone(indx) - удаление номера телефона по индексу списка;
get_phone_list() - получение списка из объектов всех телефонных номеров.

Каждый номер телефона должен быть представлен классом PhoneNumber. Объекты этого класса должны создаваться командой:

note = PhoneNumber(number, fio)
где

number - номер телефона (число) в формате XXXXXXXXXXX (одиннадцати цифр, X - цифра);
fio - Ф.И.О. владельца номера (строка).
В каждом объекте класса PhoneNumber должны формироваться локальные атрибуты:

number - номер телефона (число);
fio - ФИО владельца номера телефона.

Необходимо объявить два класса PhoneBook и PhoneNumber в соответствии с заданием.

Пример использования классов (эти строчки в программе писать не нужно):

p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
phones = p.get_phone_list()

'''
# Реализация задания через двусвязный список.

from string import digits


class PhoneNumber:

    def __init__(self, number, fio):
        if self.__check_number(number) and self.__check_fio(fio):
            self.__number = number
            self.__fio = fio
            self.next = None
            self.prev = None
        else:
            raise ValueError('введены не корректные данные при инициализации.')

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        if self.__check_number(number):
            self.__number = number

    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, fio):
        if self.__check_fio(fio):
            self.__fio = fio

    @classmethod
    def __check_number(cls, number):
        return type(number) is int and \
            len(str(number)) == 11 and \
            set(str(number)) <= set(digits)

    @classmethod
    def __check_fio(cls, fio):
        return type(fio) is str


class PhoneBook:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_phone(self, phone):
        '''Добавление нового номера телефона (в список).'''
        if self.head == None:
            self.head = phone
        if self.tail != None:
            self.tail.next = phone
            phone.prev = self.tail
        self.tail = phone

    def get_at(self, index):
        '''Для доступа к произвольному элементу списка по индексу.'''
        ptr = self.head
        i = 0
        while i != index:
            if ptr == None:
                return ptr
            ptr = ptr.next
            i += 1
        return ptr

    def remove_phone(self, indx):
        '''Удаление номера телефона по индексу списка.'''
        ptr = self.get_at(indx)  # Получаем объект по индексу.
        if ptr:
            if ptr == self.head == self.tail:  # Если элемент единственный.
                self.head = self.tail = None
            elif ptr == self.head:  # Если элемент первый.
                self.head = ptr.next
            elif ptr == self.tail:  # Если элемент последний.
                self.tail = ptr.prev
                self.tail.next = None
            else:  # Иначе связываем левый и правый элементы.
                ptr.prev.next = ptr.next
                ptr.next.prev = ptr.prev
            del ptr

    def get_phone_list(self):
        '''Получение списка из объектов всех телефонных номеров.'''
        lst_res = []
        ptr = self.head
        while ptr:
            lst_res.append(ptr.number)
            ptr = ptr.next
        return lst_res


p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
phones = p.get_phone_list()

# # Для проверки.
# print(phones)

