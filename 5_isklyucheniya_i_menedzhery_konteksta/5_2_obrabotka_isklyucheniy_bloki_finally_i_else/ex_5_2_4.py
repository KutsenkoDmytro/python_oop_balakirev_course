'''
Подвиг 4. В программе вводятся два значения в одну строчку через пробел.
Значениями могут быть числа, слова, булевы величины (True/False).
Необходимо прочитать эти значения из входного потока.
Если оба значения являются числами, то вычислить их сумму, иначе соединить их в одну строку с помощью оператора + (конкатенации строк).
Результат вывести на экран (в блоке finally).

P.S. Реализовать программу с использованием блоков try/except/finally.
Sample Input:8 11
Sample Output:19
Memory limit: 256 MBTime limit: 15 seconds
'''


def check_value(value):
    '''Преобразовывает строку в число (если это возможно).'''
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return value


lst_st = input().split()

res = ''
try:
    res = sum(map(check_value,lst_st))
except Exception:
    if lst_st:
        res = ''.join(lst_st)
finally:
    print(res)