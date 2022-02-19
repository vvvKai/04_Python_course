# УРОК №2
from copy import deepcopy

my_list = [12, 23.56, 'dsafds', False, [1, 2, 3, 4], (9, 8, 7)]

print(my_list[0:6:2]) # срез списка
print(my_list[::-1]) # разворот списка
my_list_2 = my_list.copy()
print(my_list_2)

my_list_copy = deepcopy(my_list) # глубокая копия, вместе с вложенными списками кортежами и т.д.


