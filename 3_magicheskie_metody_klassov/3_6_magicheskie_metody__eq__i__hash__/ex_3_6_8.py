'''
Подвиг 8. (task_4.py)

Из входного потока необходимо прочитать список строк командой:

lst_in = list(map(str.strip, sys.stdin.readlines()))
Каждая строка содержит информацию об учебном пособии в формате:

"Название; автор; год издания"

Например:

Python; Балакирев С.М.; 2020
Python ООП; Балакирев С.М.; 2021
Python ООП; Балакирев С.М.; 2022
Python; Балакирев С.М.; 2021
Необходимо каждую из этих строк представить объектом класса BookStudy, которые создаются командой:

bs = BookStudy(name, author, year)
где name - название пособия (строка); author - автор пособия (строка); year - год издания (целое число). Такие же публичные локальные атрибуты должны быть в объектах класса BookStudy.

Для каждого объекта реализовать вычисление хэша по двум атрибутам: name и author (без учета регистра).

Сформировать список lst_bs из объектов класса BookStudy на основе прочитанных строк (списка lst_in). После этого определить число книг с уникальными хэшами. Это число сохранить через переменную unique_books (целое число).

P.S. На экран ничего выводить не нужно.

Sample Input:

Python; Балакирев С.М.; 2020
Python ООП; Балакирев С.М.; 2021
Python ООП; Балакирев С.М.; 2022
Python; Балакирев С.М.; 2021
Sample Output:

'''

#import sys

#lst_in = list(map(str.strip, sys.stdin.readlines()))

lst_in = ['Python; Балакирев С.М.; 2020',
          'Python ООП; Балакирев С.М.; 2021',
          'Python ООП; Балакирев С.М.; 2022',
          'Python; Балакирев С.М.; 2021']

class BookStudy:

    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def __hash__(self):
        return hash((self.name.lower(), self.author.lower()))

    def __eq__(self, other):
        return hash(self) == hash(other)

lst_in = [i.split('; ') for i in lst_in]

lst_bs = [BookStudy(j[0], j[1], j[2]) for j in lst_in]
unique_books = len(set({hash(b) for b in lst_bs}))

# Для проверки.
print(lst_bs)
print(unique_books)


