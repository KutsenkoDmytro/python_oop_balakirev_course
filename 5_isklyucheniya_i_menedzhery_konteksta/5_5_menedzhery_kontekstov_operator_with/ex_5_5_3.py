'''
Подвиг 3. Объявите класс PrimaryKey, который должен работать совместно с менеджером контекста следующим образом:

with PrimaryKey() as pk:
    raise ValueError

где pk - ссылка на объект класса PrimaryKey. Класс PrimaryKey должен в момент входа в менеджер контекста выводить на экран сообщение "вход", а при завершении работы менеджера контекста выводить тип возникшего исключения. 

Класс PrimaryKey следует реализовать так, чтобы менеджер контекста сам обрабатывал возникшее исключение.Memory limit: 256 MBTime limit: 15 seconds

'''


# Примечание (изменение объекта без изменения его id)
# a = [1,2,3]
# b = [4,5,6]
# print(id(a))
# print(a)
#
# a[:] = b
# print(id(a))
# print(a)


# здесь объявляйте класс PrimaryKey
class PrimaryKey:

    def __enter__(self):
        print('вход')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type)
        return True


with PrimaryKey() as pk:
    raise ValueError
