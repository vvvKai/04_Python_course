# 6.	Реализовать два небольших скрипта:
# ●	итератор, генерирующий целые числа, начиная с указанного;
# ●	итератор, повторяющий элементы некоторого списка, определённого заранее.
# Подсказка: используйте функцию count() и cycle() модуля itertools. Обратите внимание,
# что создаваемый цикл не должен быть бесконечным. Предусмотрите условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3.
# При достижении числа 10 — завершаем цикл.
# Вторым пунктом необходимо предусмотреть условие, при котором повторение элементов списка прекратится.
#

from itertools import count, cycle
from random import random

# итератор, генерирующий целые числа, начиная с указанного
start_num = 3
stop_num = 10
gen_1 = []
for el in count(start_num):
    gen_1.append(round(random() * (stop_num - start_num) + start_num))
    if el > stop_num:
        break
print(gen_1)


# итератор, повторяющий элементы некоторого списка, определённого заранее.
list_cities = ['Moscow', 'London', 'New York', 'Paris']
for el in cycle(list_cities):
    if start_num > stop_num:
        break
    print(el)
    start_num += 1


