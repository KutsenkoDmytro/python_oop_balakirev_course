'''
Подвиг 7. (task_3.py)

Объявите класс с именем DataBase (база данных - БД), объекты которого создаются командой:

db = DataBase(path)
где path - путь к файлу с данными БД (строка).

Также в классе DataBase нужно объявить следующие методы:

write(self, record) - для добавления новой записи в БД, представленной объектом record;
read(self, pk) - чтение записи из БД (возвращает объект Record) по ее уникальному идентификатору pk (уникальное целое положительное число); запись ищется в значениях словаря (см. ниже)

Каждая запись БД должна описываться классом Record, а объекты этого класса создаваться командой:

record = Record(fio, descr, old)
где fio - ФИО некоторого человека (строка); descr - характеристика человека (строка); old - возраст человека (целое число).

В каждом объекте класса Record должны формироваться следующие локальные атрибуты:

pk - уникальный идентификатор записи (число: целое, положительное); формируется автоматически при создании каждого нового объекта;
fio - ФИО человека (строка);
descr - характеристика человека (строка);
old - возраст человека (целое число).

Реализовать для объектов класса Record вычисление хэша по атрибутам: fio и old (без учета регистра). Если они одинаковы для разных записей, то и хэши должны получаться равными. Также для объектов класса Record с одинаковыми хэшами оператор == должен выдавать значение True, а с разными хэшами - False.

Хранить записи в БД следует в виде словаря dict_db (атрибут объекта db класса DataBase), ключами которого являются объекты класса Record, а значениями список из объектов с равными хэшами:

dict_db[rec1] = [rec1, rec2, ..., recN]
где rec1, rec2, ..., recN - объекты класса Record с одинаковыми хэшами.

Для наполнения БД прочитайте строки из входного потока с помощью команды:

lst_in = list(map(str.strip, sys.stdin.readlines()))
где каждая строка представлена в формате:

"ФИО; характеристика; возраст"
Например:

Балакирев С.М.; программист; 33
Кузнецов А.В.; разведчик-нелегал; 35
Суворов А.В.; полководец; 42
Иванов И.И.; фигурант всех подобных списков; 26
Балакирев С.М.; преподаватель; 37
Каждая строка должна быть представлена объектом класса Record и записана в БД db (в словарь db.dict_db).

P.S. На экран ничего выводить не нужно.

Sample Input:

Балакирев С.М.; программист; 33
Кузнецов Н.И.; разведчик-нелегал; 35
Суворов А.В.; полководец; 42
Иванов И.И.; фигурант всех подобных списков; 26
Балакирев С.М.; преподаватель; 33
Sample Output:

'''