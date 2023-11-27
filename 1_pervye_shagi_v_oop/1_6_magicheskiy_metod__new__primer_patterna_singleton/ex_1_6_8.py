'''
ex. 8
В программе объявлена переменная TYPE_OS и два следующих класса:

TYPE_OS = 1 # 1 - Windows; 2 - Linux

class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"
Необходимо объявить третий класс с именем Dialog, который бы создавал объекты командой:

dlg = Dialog(<название>)
Здесь <название> - это строка, которая сохраняется в локальном свойстве name объекта dlg.

Класс Dialog должен создавать объекты класса DialogWindows, если переменная TYPE_OS = 1
и объекты класса DialogLinux, если переменная TYPE_OS не равна 1. При этом, переменная TYPE_OS
может меняться в последующих строчках программы. Имейте это в виду, при объявлении класса Dialog.

'''

TYPE_OS = 1


class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


class Dialog:
    '''Создает объект диалога в зависимости от переменной.'''
    __type_os = None

    def __new__(cls, *args, **kwargs):
        __type_os = TYPE_OS
        return super().__new__(cls)

    def __init__(self, name):
        self.name = name
        if self.__type_os == 1:
            DialogWindows()
        else:
            DialogLinux()

# # Проверка.
# d1 = Dialog('dialog1')
# TYPE_OS = 2
# d2 = Dialog('dialog2')
