# 1.	Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = [1, 'two', 'three', 3.14, 4, 'five', True, False, None]
print(my_list)

for el in my_list:
    print(type(el))
