# 7.	Реализовать генератор с помощью функции с ключевым словом yield,
# создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция вызывается следующим образом: for el in fact(n).
#     Она отвечает за получение факториала числа.
#     В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
from functools import reduce


x = 5
# 1ый вариант
def fact(n):
    el_fact = 1
    for el in range(1, n + 1):
        el_fact = el_fact * el
    yield el_fact


for el in fact(x):
    print(f'Факториал числа {x} = {el}')


# 2-ой вариант
def fact_v2(n):
    yield reduce(lambda x, y: x * y, range(1, n + 1))


for el in fact_v2(x):
    print(f'Факториал числа {x} = {el}')
