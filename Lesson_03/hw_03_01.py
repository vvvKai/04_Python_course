# 1.	Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division_2_numbers():
    my_list = input('Введите 2 числа через пробел: ').split(' ')
    try:
        divis = int(my_list[0]) / int(my_list[1])
    except ZeroDivisionError:
        print('Делить на 0 нельзя, попробуйте другое число')
    else:
        return divis


print(division_2_numbers())
