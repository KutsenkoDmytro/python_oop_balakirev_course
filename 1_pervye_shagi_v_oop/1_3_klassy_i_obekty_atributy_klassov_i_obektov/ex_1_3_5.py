''''
Подвиг 5. Объявите пустой класс с именем Car. С помощью функции setattr() добавьте в этот класс атрибуты:

model: "Тойота"
color: "Розовый"
number: "П111УУ77"
Выведите на экран значение атрибута color, используя словарь __dict__ класса Car.
'''


class Car:
    pass


d = {'model': 'Тойота', 'color': 'Розовый', 'number': 'П111УУ77'}
for key, val in d.items():
    setattr(Car, key, val)

print(Car.__dict__.get('color', None))
