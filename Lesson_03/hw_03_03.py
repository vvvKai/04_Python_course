# 3.	Реализовать функцию my_func(),
# которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.

def my_func(*args):
    return print(sum(args) - min(args))


my_func(20, 30, 50)
