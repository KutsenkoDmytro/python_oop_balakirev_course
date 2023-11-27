'''
Подвиг 6. Вам необходимо написать программу описания музеев. Для этого нужно объявить класс Museum, объекты которого формируются командой:

mus = Museum(название музея)
В объектах этого класса должны формироваться следующие локальные атрибуты:

name - название музея (строка);
exhibits - список экспонатов (изначально пустой список).

Сам класс Museum должен иметь методы:

add_exhibit(self, obj) - добавление нового экспоната в музей (в конец списка exhibits);
remove_exhibit(self, obj) - удаление экспоната из музея (из списка exhibits по ссылке obj - на экспонат)
get_info_exhibit(self, indx) - получение информации об экспонате (строка) по индексу списка (нумерация с нуля).

Экспонаты представляются объектами своих классов. Для примера объявите в программе следующие классы экспонатов:

Picture - для картин;
Mummies - для мумий;
Papyri - для папирусов.

Объекты этих классов должны создаваться следующим образом (с соответствующим набором локальных атрибутов):

p = Picture(название, художник, описание)            # локальные атрибуты: name - название; author - художник; descr - описание
m = Mummies(имя мумии, место находки, описание)      # локальные атрибуты: name - имя мумии; location - место находки; descr - описание
pr = Papyri(название папируса, датировка, описание)  # локальные атрибуты: name - название папируса; date - датировка (строка); descr - описание
Метод get_info_exhibit() класса Museum должен возвращать значение атрибута descr указанного экспоната в формате:

"Описание экспоната {name}: {descr}"

Например:

"Описание экспоната Девятый вал: Айвазовский написал супер картину."

Пример использования классов (в программе эти строчки писать не нужно - только для примера):

mus = Museum("Эрмитаж")
mus.add_exhibit(Picture("Балакирев с подписчиками пишет письмо иноземному султану", "Неизвестный автор", "Вдохновляющая, устрашающая, волнующая картина"))
mus.add_exhibit(Mummies("Балакирев", "Древняя Россия", "Просветитель XXI века, удостоенный мумификации"))
p = Papyri("Ученья для, не злата ради", "Древняя Россия", "Самое древнее найденное рукописное свидетельство о языках программирования")
mus.add_exhibit(p)
for x in mus.exhibits:
    print(x.descr)
P.S. На экран ничего выводить не нужно.

'''

# class StringValue:
#     '''Дескриптор данных (строковый тип).'''
#     def __set_name__(self, owner, name):
#         self.name = '_' + name
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         if type(value) is str:
#             setattr(instance, self.name, value)
#         else:
#             raise ValueError('Неверный тип присваиваемых данных.')


class Museum:
    '''Описывает музей.'''

    def __init__(self, name):
        self.name = name
        self.exhibits = []

    def add_exhibit(self, obj):
        self.exhibits.append(obj)

    def remove_exhibit(self, obj):
        while obj in self.exhibits:
            self.exhibits.remove(obj)

    def get_info_exhibit(self, indx):
        if -len(self.exhibits) <= indx < len(self.exhibits):
            exhib = self.exhibits[indx]
            return f'Описание экспоната {exhib.name}: {exhib.descr}'


class Picture:
    '''Описывает картины.'''
    # author = StringValue()
    # name = StringValue()
    # descr = StringValue()

    def __init__(self, name, author, descr):
        self.author = author
        self.name = name
        self.descr = descr


class Mummies:
    '''Описывает мумии.'''
    # name = StringValue()
    # location = StringValue()
    # descr = StringValue()

    def __init__(self, name, location, descr):
        self.name = name
        self.location = location
        self.descr = descr


class Papyri:
    '''Описывает папирусы.'''
    # name = StringValue()
    # date = StringValue()
    # descr = StringValue()

    def __init__(self, name, date, descr):
        self.name = name
        self.date = date
        self.descr = descr


# # Для проверки.
# mus = Museum("Эрмитаж")
# mus.add_exhibit(Picture("Балакирев с подписчиками пишет письмо иноземному султану", "Неизвестный автор", "Вдохновляющая, устрашающая, волнующая картина"))
# mus.add_exhibit(Mummies("Балакирев", "Древняя", "Просветитель XXI века, удостоенный мумификации"))
# p = Papyri("Ученья для, не злата ради", "Древняя", "Самое древнее найденное рукописное свидетельство о языках программирования")
#
# mus.add_exhibit(p)
# for x in mus.exhibits:
#     print(x.descr)
