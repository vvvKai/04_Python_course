# Создать программный файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

f_name = "task_01_file.txt"
text_file = open(f_name, "a", encoding='utf-8')
input_txt = None
while input_txt != '':
    input_txt = input('Введите текст для записи в файл: ')
    print(input_txt + '\n', file=text_file)
text_file.close()
