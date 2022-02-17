numbers = []

list_n = int(input('Ведите количество элементов списка: '))

for el in range(list_n):
    el_n = int(input(f'Введите {el + 1}-й элемент списка: '))
    numbers.append(el_n)

print('Исходный список: ', numbers)

i = 0

while i < len(numbers):
    pop_el = numbers.pop(i)
    numbers.insert(i + 1, pop_el)
    i += 2

print('Измененный список: ', numbers)
