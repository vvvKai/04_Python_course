# Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка будет содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки,
# также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.
import json


with open('task_07_file.txt', 'r') as firm_list:
    average_profit = 0
    i = 0
    firm_dict = {}
    output_firm_list = []
    average_dict = {}
    for firm in firm_list:
        firm_list = firm.split()

        firm_profit = int(firm_list[2]) - int(firm_list[3])
        if firm_profit > 0:
            average_profit += firm_profit
            i += 1
        firm_dict[firm_list[0]] = firm_profit
    average_dict = {'average_profit': int(average_profit/i)}
    output_firm_list = [firm_dict, average_dict]
    print(output_firm_list)

with open("task_07_file.json", "w", encoding="UTF-8") as write_f:
    json.dump(output_firm_list, write_f, ensure_ascii=False)
