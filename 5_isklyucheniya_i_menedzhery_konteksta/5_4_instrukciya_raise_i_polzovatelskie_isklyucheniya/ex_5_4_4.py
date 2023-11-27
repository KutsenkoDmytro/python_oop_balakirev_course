'''
Подвиг 4. Объявите класс-исключение с именем StringException, унаследованным от базового класса Exception. После этого объявите еще два класса-исключения:

NegativeLengthString - ошибка, если длина отрицательная;
ExceedLengthString - ошибка, если длина превышает заданное значение;

унаследованные от базового класса StringException.

Затем, в блоке try (см. программу) пропишите команду генерации исключения для перехода в блок обработки исключения ExceedLengthString.Memory limit: 256 MBTime limit: 15 seconds
'''
# Нет примера решения данной задачи.


class StringException(Exception):
    '''Базовый класс исключений для строк.'''

class NegativeLengthString(StringException):
    '''Ошибка, если длина отрицательная.'''

class ExceedLengthString(StringException):
    '''Ошибка, если длина превышает заданное значение.'''
# здесь объявляйте классы


try:
    # здесь команда для генерации исключения
    st, len_st = input(), int(input())
    if len_st < 0:
        raise NegativeLengthString
    elif len(st) > len_st:
        raise ExceedLengthString
    else:
        raise StringException

except NegativeLengthString:
    print("NegativeLengthString")
except ExceedLengthString:
    print("ExceedLengthString")
except StringException:
    print("StringException")