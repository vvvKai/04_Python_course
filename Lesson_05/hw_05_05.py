# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран

from random import randint

with open('task_05_file.txt', 'w', encoding="UTF-8") as num_file:
    n = 10
    numbers = [randint(1, 100) for el in range(n)]
    print('Сгенерированная последовательность: ', numbers)
    print('Сгенерированная последовательность: ', file=num_file)
    for el in numbers:
        print(str(el) + " ", end ='', file=num_file)

with open('task_05_file.txt', 'r', encoding="UTF-8") as r_file:
    content = r_file.readlines()
    content = content[1].split()
    content_sum = sum([int(el) for el in content])
    print('Прочитанная последовательность: ', content)
    print('Сумма чисел последовательности = ', content_sum)
