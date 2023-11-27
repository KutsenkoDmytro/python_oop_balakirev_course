'''
Подвиг 9. Объявите класс-декоратор InputDigits для декорирования стандартной функции input так, чтобы при вводе строки из целых чисел, записанных через пробел, например:

"12 -5 10 83"

на выходе возвращался список из целых чисел:

[12, -5, 10, 83]

Назовите декорированную функцию input_dg и вызовите ее командой:

res = input_dg()
P.S. На экран ничего выводить не нужно.

'''


class InputDigits:
    '''Класс-декоратор, возвращающий список чисел из строки.'''
    def __init__(self, func):
        self.__func = func

    def __call__(self, *args, **kwargs):
        str = self.__func()
        return list(map(int, str.split()))



input_dg = InputDigits(input)

# @InputDigits
# def input_dg():
#     return input()

res = input_dg()

# # Для проверки:
# print(res)



