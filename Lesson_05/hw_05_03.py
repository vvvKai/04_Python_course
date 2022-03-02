# Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

with open('task_03_file.txt') as import_list:
    import_list = import_list.read().splitlines() # удаляем символ "\n" переноса строки
    import_list = [el.split(' ') for el in import_list]  # убираю пробелы и создаю вложенные списки для каждого человека

    # создаем словарь из списка
    new_dict = {}
    for el in import_list:
        new_dict[el[0]] = el[1]
    print(new_dict)

    # ищем наибольшую ЗП и человека, список сотрудников с ЗП меньше 20000, среднюю ЗП
    max_salary = 0
    min_salary = 20000
    low_salary = []
    sum_salary = 0
    i = 0
    for key in new_dict:
        if int(new_dict.get(key)) > max_salary:
            max_salary = int(new_dict.get(key))
            name_max_salary = key
        if int(new_dict.get(key)) <= min_salary:
            i += 1
            low_salary.append(f'{key}: {new_dict.get(key)}')
        sum_salary += int(new_dict.get(key))

    print(f'Наибольшая ЗП у {name_max_salary} = {max_salary}')
    print(f'Сотрудников с ЗП меньше 20000 рублей - {i} человек: ', low_salary)
    print('Средняя ЗП: ', sum_salary / len(new_dict))
