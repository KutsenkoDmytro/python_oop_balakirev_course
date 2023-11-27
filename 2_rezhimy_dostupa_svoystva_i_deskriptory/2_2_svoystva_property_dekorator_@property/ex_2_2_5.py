'''
Объявите в программе класс WindowDlg, объекты которого предполагается создавать командой:
wnd = WindowDlg(заголовок окна, ширина, высота)
В каждом объекте класса WindowDlg должны создаваться приватные локальные атрибуты:

__title - заголовок окна (строка);
__width, __height - ширина и высота окна (числа).

В классе WindowDlg необходимо реализовать метод:

show() - для отображения окна на экране (выводит в консоль строку в формате:
"<Заголовок>: <ширина>, <высота>", например "Диалог 1: 100, 50").

Также в классе WindowDlg необходимо реализовать два объекта-свойства:

width - для изменения и считывания ширины окна;
height - для изменения и считывания высоты окна.

При изменении размеров окна необходимо выполнять проверку:

переданное значение является целым числом в диапазоне [0; 10000].
Если хотя бы один размер изменился (высота или ширина), то следует выполнить
автоматическую перерисовку окна (вызвать метод show()). При начальной инициализации размеров width, height вызывать метод show() не нужно.

'''


class WindowDlg:
    '''Описывает диалоговое окно.'''

    def __init__(self, title, width, height):

        if self.__check_size_param(width) and \
                self.__check_size_param(height) and \
                type(title) is str:
            self.__title = title
            self.__width = width
            self.__height = height
        else:
            raise ValueError('не верный тип данных')

    def show(self):
        print(f'{self.__title}: {self.__width}, {self.__height}')

    # объект-свойство width
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if self.__check_size_param(width) and \
                self.__width != width:
            self.__width = width
            self.show()

    # объект-свойство height
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if self.__check_size_param(height) and \
                self.__height != height:
            self.__height = height
            self.show()

    @classmethod
    def __check_size_param(cls, value):
        '''Проверяет размер параметра.'''
        return (type(value) is int) and (0 <= value <= 10000)

# # Для проверки.
# wd_1 = WindowDlg('Диалог 1',50, 100)
# wd_1.height = 120
