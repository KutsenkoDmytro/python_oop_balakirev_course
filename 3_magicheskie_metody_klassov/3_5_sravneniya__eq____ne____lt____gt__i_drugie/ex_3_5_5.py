'''
Подвиг 5. (task_3.py)

Имеется стихотворение, представленное следующим списком строк:

stich = ["Я к вам пишу – чего же боле?",
        "Что я могу еще сказать?",
        "Теперь, я знаю, в вашей воле",
        "Меня презреньем наказать.",
        "Но вы, к моей несчастной доле",
        "Хоть каплю жалости храня,",
        "Вы не оставите меня."]
Необходимо в каждой строчке этого стиха убрать символы "–?!,.;" в начале и в конце каждого слова и разбить строку по словам (слова разделяются одним или несколькими пробелами). На основе полученного списка слов, создать объект класса StringText командой:

st = StringText(lst_words)
где lst_words - список из слов одной строчки стихотворения.

С объектами класса StringText должны быть реализованы операторы сравнения:

st1 > st2   # True, если число слов в st1 больше, чем в st2
st1 >= st2  # True, если число слов в st1 больше или равно st2
st1 < st2   # True, если число слов в st1 меньше, чем в st2
st1 <= st2  # True, если число слов в st1 меньше или равно st2
Все объекты класса StringText (для каждой строчки стихотворения) сохранить в списке lst_text. Затем, сформировать новый список lst_text_sorted из отсортированных объектов класса StringText по убыванию числа слов. Для сортировки использовать стандартную функцию sorted() языка Python. После этого преобразовать данный список (lst_text_sorted) в список из строк (объекты заменяются на соответствующие строки, между словами ставится пробел).

P.S. На экран в программе ничего выводить не нужно.

'''


class ListParcer:  # Можно заменить регулярным выражением [re.sub(r"[–?!,.;]", '', a).split() for a in stich]
    '''Функтор для парсинга строк (элементов списка).'''

    def __init__(self, chars='–?!,.;'):
        self.chars = chars

    def __call__(self, lst, *args, **kwargs):
        # Замена символов в строках (элементах списка).
        for i, v in enumerate(lst):
            for symb in self.chars:
                v = v.replace(symb, '')
            lst[i] = v
        # Разбиваем строки по словам и возвращаем список.
        lst_res = [i.split() for i in lst]
        return lst_res


class StringText:

    def __init__(self, lst_words: list):
        self.lst_words = lst_words

    def __gt__(self, other):
        self.__check_val_obj(other)
        return len(self) > len(other)

    def __ge__(self, other):
        self.__check_val_obj(other)
        return len(self) > len(other)

    def __len__(self):
        return len(self.lst_words)

    @classmethod
    def __check_val_obj(cls, value):
        if not isinstance(value, cls):
            raise ValueError('Не верный тип данных.')


stich = ["Я к вам пишу – чего же боле?",
         "Что я могу еще сказать?",
         "Теперь, я знаю, в вашей воле",
         "Меня презреньем наказать.",
         "Но вы, к моей несчастной доле",
         "Хоть каплю жалости храня,",
         "Вы не оставите меня."]

pars1 = ListParcer()
lst_res = pars1(stich)

lst_text = [StringText(val) for val in lst_res]
lst_text_sorted = sorted(lst_text, key=lambda x: x,
                         reverse=True)  # Здесь key=lambda x: x, можно не использовать так как сравнение между класами происходит по кол-ву слов.
lst_text_sorted = [' '.join(obj.lst_words) for obj in lst_text_sorted]

# # Для проверки.
# for i in lst_text:
#     print(len(i))
# print('==================')
# for i in lst_text_sorted:
#     print(i)
