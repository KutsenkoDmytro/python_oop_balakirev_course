t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e',
     'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
     'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c',
     'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


def remove_duplicate_dashes(func):
    def wrapper(*args, **kwards):
        s = func(*args, **kwards)
        while '__' in s:
            s = s.replace('__', '_')
        return s

    return wrapper


@remove_duplicate_dashes
def get_translate(s):
    symb = ": ;.,-"
    s_res = ''
    for i in s.lower():
        if i in symb:
            s_res += '_'
        else:
            try:
                s_res += t[i]
            except:
                s_res += i
    return s_res


s = input()
print(get_translate(s))

