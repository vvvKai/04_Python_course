# 1.	Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.

from hw_04_01_script import salary_calc
from sys import argv

script_name, hours, hour_rate, prize = argv

print("Имя скрипта: ", script_name)
print("Кол-во отработанных часов: ", hours)
print("Ставка в час: ", hour_rate)
print("Премия: ", prize)
print('ЗП составляет: ', salary_calc(int(hours), int(hour_rate), int(prize)))
