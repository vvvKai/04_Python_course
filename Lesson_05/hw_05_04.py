# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

# создаем словарь перевода
translate_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

# 1ый способ решения, длинный

# открываем файл и преобразуем в список
my_f = open("task_04_file.txt", "r")
content = my_f.read().splitlines()
content = [el.replace(' — ', ' ') for el in content]
content = [el.split() for el in content]
my_f.close()

# преобразуем в словарь
content_dict = {}
for el in content:
    content_dict[el[0]] = el[1]

# созадем новый словарь
new_dict = {}
for trans_key in translate_dict:
    for content_key in content_dict:
        if trans_key == content_key:
            new_dict[translate_dict.get(trans_key)] = content_dict[content_key]

# Содаем новые строки из словаря и записываем в файл
n_obj = open("task_04_rus_file.txt", 'w', encoding="UTF-8")
for key in new_dict:
    n_obj.write(key + ' - ' + new_dict.get(key) + "\n")
n_obj.close()

# 2-ой способ, короткий

with open('task_04_file.txt', 'r') as content:
    with open('task_04_rus_file2.txt', 'w', encoding="UTF-8") as new_file:
        for i in content:
            new_str = i.strip().split(' — ')
            print(translate_dict.get(new_str[0]) + ' - ' + new_str[1], file=new_file)
