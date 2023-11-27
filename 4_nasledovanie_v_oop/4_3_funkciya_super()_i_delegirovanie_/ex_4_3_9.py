'''
Подвиг 9 (на повторение). (task_7.py)

Объявите класс StringDigit, который наследуется от стандартного класса str. Объекты класса StringDigit должны создаваться командой:

sd = StringDigit(string)
где string - строка из цифр (например, "12455752345950"). Если в строке string окажется хотя бы один не цифровой символ, то генерировать исключение командой:

raise ValueError("в строке должны быть только цифры")
Также в классе StringDigit нужно переопределить оператор + (конкатенации строк) так, чтобы операции:

sd = sd + "123"
sd = "123" + sd
создавали новые объекты класса StringDigit (а не класса str). Если же при соединении строк появляется не цифровой символ, то генерировать исключение:

raise ValueError("в строке должны быть только цифры")
Пример использования класса (эти строчки в программе не писать):

sd = StringDigit("123")
print(sd)       # 123
sd = sd + "456" # StringDigit: 123456
sd = "789" + sd # StringDigit: 789123456
sd = sd + "12f" # ValueError
P.S. В программе нужно объявить только класс. На экран выводить ничего не нужно.

'''
#ПЕРЕОПРЕДЕЛЕНИЕ МЕТОДОВ СТРОКИ
#если тип данных неизменяемый (число, строка, кортеж и т.д.) логику проверки значений желательно прописовать в методе __new__, а не в инициализаторе.
#если логику прописывать в __init__, то не нужно передавать доп агрументы делегируя инициализацию базовому классу: super().__init__()


class StringDigit(str):
    
    def __new__(cls,val, *args, **kwargs):
        cls.__check_isdigit(val)
        return super().__new__(cls, val)

    def __add__(self, other):
        new_str = str(self) + other
        self.__check_isdigit(new_str)
        return self.__class__(new_str)

    def __radd__(self, other):
        new_str = other + str(self)
        self.__check_isdigit(new_str)
        return self.__class__(new_str)

    @staticmethod
    def __check_isdigit(value:str):
        if not value.isdigit():
            raise ValueError("в строке должны быть только цифры")


# Для проверки.
sd = StringDigit("123")
print(sd)       # 123
sd = sd + "456" # StringDigit: 123456
sd = "789" + sd # StringDigit: 789123456
#sd = sd + "12f" # ValueError

