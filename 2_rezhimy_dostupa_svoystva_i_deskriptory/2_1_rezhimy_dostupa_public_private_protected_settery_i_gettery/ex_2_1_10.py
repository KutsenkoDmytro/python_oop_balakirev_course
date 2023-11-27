'''
Объявите класс EmailValidator для проверки корректности email-адреса.
Необходимо запретить создание объектов этого класса: при создании экземпляров должно возвращаться значение None, например:

em = EmailValidator() # None
В самом классе реализовать следующие методы класса (@classmethod):

get_random_email(cls) - для генерации случайного email-адреса по формату: xxxxxxx...xxx@gmail.com, где x - любой допустимый символ в email (латинский буквы, цифры, символ подчеркивания и точка);

check_email(cls, email) - возвращает True, если email записан верно и False - в противном случае.

Корректность строки email определяется по следующим критериям:

допустимые символы: латинский алфавит, цифры, символы подчеркивания, точки и собачка @ (одна);
длина email до символа @ не должна превышать 100 (сто включительно);
длина email после символа @ не должна быть больше 50 (включительно);
после символа @ обязательно должна идти хотя бы одна точка;
не должно быть двух точек подряд.
Также в классе нужно реализовать приватный статический метод класса:

is_email_str(email) - для проверки типа переменной email, если строка, то возвращается значение True, иначе - False.

Метод is_email_str() следует использовать в методе check_email() перед проверкой корректности email. Если параметр email не является строкой, то check_email() возвращает False.

Пример использования класса EmailValidator (эти строчки в программе писать не нужно):

res = EmailValidator.check_email("sc_lib@list.ru") # True
res = EmailValidator.check_email("sc_lib@list_ru") # False

'''

from string import ascii_letters, digits
from random import randint, choice


class EmailValidator:
    __CHARS_RANDOM = ascii_letters + digits + '_' + '.'
    __CHARS_CORRECT = __CHARS_RANDOM + '@'

    def __new__(cls, *args, **kwargs):
        '''Запрещает создание єкземпляров класса.'''
        return None

    @classmethod
    def get_random_email(cls):
        '''Генерирует случайный адрес.'''
        str = ''
        while not cls.check_email(str):
            for i in range(randint(1, 100)):
                str += choice(cls.__CHARS_RANDOM)
            str += '@gmail.com'
        return str

    @classmethod
    def check_email(cls, email):
        '''Возвращает True, если email записан верно
        и False - в противном случае.
        '''
        res = cls.__is_email_str(email) \
              and set(email) <= set(cls.__CHARS_CORRECT) \
              and email.count('@') == 1 \
              and len(email[:email.index('@')]) <= 100 \
              and len(email[email.index('@'):]) <= 50 \
              and '.' in email[email.index('@'):] \
              and '..' not in email

        return res

    @staticmethod
    def __is_email_str(email):
        '''Для проверки типа переменной email.'''
        return type(email) == str


res = EmailValidator.check_email("sc_lib@list.ru")
res = EmailValidator.check_email("sc_lib@list_ru")
