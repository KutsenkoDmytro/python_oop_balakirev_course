'''
Подвиг 3. Объявите класс с именем Model, объекты которого создаются командой:

model = Model()
Объявите в этом классе метод query() для формирования записи базы данных. Использоваться этот метод должен следующим образом:

model.query(field_1=value_1, field_2=value_2, ..., field_N=value_N)

Например:

model.query(id=1, fio='Sergey', old=33)
Все эти переданные данные должны сохраняться внутри объекта model класса Model. Затем, при выполнении команды:

print(model)
В консоль должна выводиться информация об объекте в формате:

"Model: field_1 = value_1, field_2 = value_2, ..., field_N = value_N"

Например:

"Model: id = 1, fio = Sergey, old = 33"

Если метод query() не вызывался, то в консоль выводится строка:

"Model"

P.S. В программе нужно только объявить класс, выводить в консоль ничего не нужно.

'''

class Model:

    def __init__(self):
        self.data = {}

    def query(self, *args, **kwargs):
        self.data |= kwargs

    def __str__(self):
        name = self.__class__.__name__
        if self.data:
            str_res = f'{name}: '+', '.join([f'{k} = {v}' for k, v in self.data.items()])
            return str_res
        else:
            return  name

model = Model()
model.query(id=1, fio='Sergey', old=33)

print(model)