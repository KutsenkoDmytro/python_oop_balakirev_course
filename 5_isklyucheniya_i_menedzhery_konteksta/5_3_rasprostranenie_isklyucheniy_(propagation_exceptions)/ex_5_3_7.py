'''
Подвиг 7. В программе выполняется считывание числовых данных из входного потока, командой:

digits = list(map(float, input().split()))

Эти данные следует представить в виде объекта класса TupleLimit. Сам класс должен наследоваться от класса tuple, а его объекты создаваться командой:

tl = TupleLimit(lst, max_length)

где lst - коллекция (список или кортеж) из данных; max_length - максимально допустимая длина коллекции TupleLimit. Если длина lst превышает значение max_length, то должно генерироваться исключение командой:

raise ValueError('число элементов коллекции превышает заданный предел')

В самом классе TupleLimit переопределить магические методы __str__() и __repr__() для отображения объекта класса TupleLimit в виде строки из набора данных lst, записанных через пробел. Например:

"1.0 2.5 -5.0 11.2"

Создайте в программе объект класса TupleLimit для прочитанных данных digits и параметром max_length = 5. Выведите на экран объект в случае его успешного создания. Иначе, выведите сообщение обработанного исключения.
Sample Input:1 2 3 4 5
Sample Output:1.0 2.0 3.0 4.0 5.0
Memory limit: 256 MBTime limit: 15 seconds

'''

#ПЕРЕОПРЕДЕЛЕНИЕ МЕТОДОВ КОРТЕЖА (НАСЛЕДОВАНИЕ)

class TupleLimit(tuple):

    def __new__(cls,lst, max_length, *args, **kwargs):
        if len(lst) > max_length:
            raise ValueError('число элементов коллекции превышает заданный предел')
        return super().__new__(cls,lst)

    def __str__(self):
        return ' '.join([str(v) for v in self])

    def __repr__(self):
        return self.__str__()


st = '1 2 3 4 5'
digits =list(map(float, st.split())) #list(map(float, input().split()))

try:
    tl = TupleLimit(digits,5)
    print(tl)
except Exception as e:
    print(e)