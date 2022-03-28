# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
# __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде
# прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# 31 22
# 37 43
# 51 86
# 3 5 32
# 2 4 6
# -1 64 -8
# 3 5 8 3
# 8 3 7 1
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в
# привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
# объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
# строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

import random


class Matrix():

    def __init__(self, lst):
        self.lst = lst
        self.row_count = len(self.lst)
        self.col_count = len(self.lst[0])

    def __str__(self):
        ret_val = ''
        for i in range(self.row_count):
            for j in range(self.col_count):
                ret_val += str(self.lst[i][j]) + '\t'
            ret_val += '\n'
        return ret_val

    def get_item(self, row, col):
        try:
            ret_val = self.lst[row][col]
        except:
            ret_val = 0
        return ret_val

    def __add__(self, other):
        new_lst = []
        max_rows = max(self.row_count, other.row_count)
        max_cols = max(self.col_count, other.col_count)
        for i in range(max_rows):
            new_lst.append([])
            for j in range(max_cols):
                new_lst[i].append(self.get_item(i, j) + other.get_item(i, j))
        return Matrix(new_lst)


max_col = 4
max_row = 3


def create_lst():
    rows = max_row
    cols = max_col
    tmp_list = []
    for i in range(rows):
        tmp_list.append([])
        for j in range(cols):
            tmp_list[i].append(random.randint(0, 9))
    return tmp_list


m1 = Matrix(create_lst())
print(m1)

m2 = Matrix(create_lst())
print(m2)

m3 = m1 + m2
print(m3)
