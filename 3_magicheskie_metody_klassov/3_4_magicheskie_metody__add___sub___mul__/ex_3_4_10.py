'''
Подвиг 10 (на повторение). (task_7.py)

В нейронных сетях использую операцию под названием Max Pooling. Суть ее состоит в сканировании прямоугольной таблицы чисел (матрицы) окном определенного размера (обычно, 2x2 элемента) и выбора наибольшего значения в пределах этого окна:

MaxPooling

Или, если окна выходят за пределы матрицы, то они пропускаются (игнорируются):

MaxPooling3

Мы повторим эту процедуру. Для этого в программе нужно объявить класс с именем MaxPooling, объекты которого создаются командой:

mp = MaxPooling(step=(2, 2), size=(2,2))
где step - шаг смещения окна по горизонтали и вертикали;
size - размер окна по горизонтали и вертикали.

Параметры step и size по умолчанию должны принимать кортеж со значениями (2, 2).

Для выполнения операции Max Pooling используется команда:

res = mp(matrix)
где matrix - прямоугольная таблица чисел;
res - ссылка на результат обработки таблицы matrix (должна создаваться новая таблица чисел.

Прямоугольную таблицу чисел следует описывать вложенными списками. Если при сканировании таблицы часть окна выходит за ее пределы, то эти данные отбрасывать (не учитывать все окно).

Если matrix не является прямоугольной таблицей или содержит хотя бы одно не числовое значение, то должно генерироваться исключение командой:

raise ValueError("Неверный формат для первого параметра matrix.")
Пример использования класса (эти строчки в программе писать не нужно):

mp = MaxPooling(step=(2, 2), size=(2,2))
res = mp([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 8, 7, 6],
    [5, 4, 3, 2]
    ])    # [[6, 8], [9, 7]]
Результатом будет таблица чисел:

6 8
9 7
P.S. В программе достаточно объявить только класс. Выводить на экран ничего не нужно.


'''

#ОБРАБОТКА МАТРИЦЫ


class MaxPooling:

    def __init__(self, step=(2, 2), size=(2, 2)):
        self.step = step
        self.size = size

    def __call__(self, matrix, *args, **kwargs):
        self.__check_matrix(matrix)
        sz_new_mx = self.__get_correct_size_mx(matrix)
        lst_res = []
        for i in range(0, sz_new_mx[1],
                       self.step[1]):  # шагаем по строкам с интервалом step.
            if i + self.size[1] > sz_new_mx[1]:  # предотвращаем выход за диапазон (по строкам).
                break
            else:
                lst_i = []
                for j in range(0, sz_new_mx[0], self.step[
                    0]):  # шагаем по столбцам с интервалом step.
                    if j + self.size[0] > sz_new_mx[0]:  # предотвращаем выход за диапазон (по столбцам).
                        break
                    else:
                        lst_j = []
                        for k in range(self.size[0]):
                            lst_j += matrix[i + k][j:j + self.size[0]]
                        lst_i.append(max(lst_j))
                lst_res.append(lst_i)
        return lst_res

    def __get_correct_size_mx(self, matrix):
        width_mx = len(matrix[0])
        size_wnd_right = self.size[0]
        if size_wnd_right > width_mx:
            crct_width_mx = 0
        else:
            crct_width_mx =  ((width_mx-size_wnd_right) // self.step[0]*self.step[0]) + size_wnd_right

            # crct_width_mx = size_wnd_right
            # while crct_width_mx <= width_mx:
            #     a = crct_width_mx + self.step[0]
            #     if a > width_mx:
            #         break
            #     crct_width_mx = a

        height_mx = len(matrix)
        size_wnd_down = self.size[1]
        if size_wnd_down > height_mx:
            crct_height_mx = 0
        else:
            crct_height_mx =  ((height_mx-size_wnd_down) // self.step[1])*self.step[1] + size_wnd_down

            # crct_height_mx = size_wnd_down
            # while crct_height_mx <= height_mx:
            #     a = crct_height_mx + self.step[1]
            #     if a > height_mx:
            #         break
            #     crct_height_mx = a
        return (crct_width_mx, crct_height_mx)

    @staticmethod
    def __check_matrix(value):
        check = True
        if not isinstance(value, list):
            check = False
        elif len(set(list(map(len, value)))) != 1:
            check = False
        else:
            for lst in value:
                for val in lst:
                    if type(val) not in {int, float}:
                        check = False
        if not check:
            raise ValueError("Неверный формат для первого параметра matrix.")

# Для проверки.
# mp = MaxPooling(step=(2, 2), size=(2, 2))
# m = mp([
#     [1, 2, 3, 4, 5, 6, 7, 8],
#     [9, 10, 11, 12, 13, 14, 15, 16],
#     [17, 18, 19, 20, 21, 22, 23, 24],
#     [25, 26, 27, 28, 29, 30, 31, 32],
#     [33, 34, 35, 36, 37, 38, 39, 40],
#     [41, 42, 43, 44, 45, 46, 47, 48],
#     [49, 50, 51, 52, 53, 54, 55, 56],
#     [57, 58, 59, 60, 61, 62, 63, 64]
# ])
# print(m)
