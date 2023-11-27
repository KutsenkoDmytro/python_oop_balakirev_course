'''
Подвиг 5. (task_1.py)

Объявите в программе класс Person, объекты которого создаются командой:

p = Person(fio, job, old, salary, year_job)
где fio - ФИО сотрудника (строка);
job - наименование должности (строка);
old - возраст (целое число);
salary - зарплата (число: целое или вещественное);
year_job - непрерывный стаж на указанном месте работы (целое число).

В каждом объекте класса Person автоматически должны создаваться локальные атрибуты с такими же именами: fio, job, old, salary, year_job и соответствующими значениями.

Также с объектами класса Person должны поддерживаться следующие команды:

data = p[indx] # получение данных по порядковому номеру (indx) атрибута (порядок: fio, job, old, salary, year_job и начинается с нуля)
p[indx] = value # запись в поле с указанным индексом (indx) нового значения value
for v in p: # перебор всех атрибутов объекта в порядке: fio, job, old, salary, year_job
    print(v)
При работе с индексами, проверить корректность значения indx. Оно должно быть целым числом в диапазоне [0; 4]. Иначе, генерировать исключение командой:

raise IndexError('неверный индекс')
Пример использования класса (эти строчки в программе не писать):

pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
pers[0] = 'Балакирев С.М.'
for v in pers:
    print(v)
pers[5] = 123 # IndexError
P.S. В программе нужно объявить только класс. Выводить на экран ничего не нужно.

'''


class Person:

    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self._order_val = ('fio', 'job', 'old', 'salary', 'year_job')

    def __getitem__(self, item):
        self._check_indx(item)
        return getattr(self, self._order_val[item])

    def __setitem__(self, key, value):
        self._check_indx(key)
        setattr(self, self._order_val[key], value)

    #В данной реализации можно явно не об'являть методы __iter__ и __next__.
    def __iter__(self):
        self.indx_i = -1
        return self

    def __next__(self):
        if self.indx_i + 1 < len(self._order_val):
            self.indx_i += 1
            return getattr(self, self._order_val[self.indx_i])
        else:
            raise StopIteration

    @staticmethod
    def _check_indx(indx):
        if not (isinstance(indx, int) and 0 <= indx <= 4):
            raise IndexError('неверный индекс')



#Для проверки.
pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
pers[0] = 'Балакирев С.М.'
pers.new_attr = 'Новый атрибут'
for v in pers:
    print(v)
#pers[5] = 123 # IndexError
