# Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

with open('task_02_file.txt', 'r') as text_file:
    i = 0
    for line in text_file:
        i += 1
        print(f'{i}-я строка состот из {len(line.split(" "))} слов: {line}', end='')
print('')
print(f'Всего в файле строк: {i} шт')
