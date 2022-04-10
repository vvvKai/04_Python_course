# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
# строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
# © geekbrains.ru 16
# декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип
# к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
# реальных данных.

from random import randint as rnd


class data_convert():
    def __init__(self, str_date):
        self.str_date = str_date
        self.dd, self.mm, self.yy = self.get_data_components(self.str_date)

    def __str__(self):
        return self.check_data_components(self.dd, self.mm, self.yy)

    @staticmethod
    def check_data_components(dd, mm, yy):
        ret_val = True
        print(f'\nДата на входе в функцию: {dd:02d}-{mm:02d}-{yy:04d}')

        is_leap = False
        if yy % 4 == 0 and yy % 400 == 0 and yy % 100 != 0:
            is_leap = True

        if yy < 1800 or yy > 2200:
            print(f'Некорректный номер года {yy:04d}')
            ret_val = False

        if mm > 12:
            print(f'Некорректный номер месяца {mm:02d}')
            ret_val = False

        if mm in (1, 3, 5, 7, 8, 10, 12):
            max_dd = 31
        elif mm == 2:
            if is_leap:
                max_dd = 29
            else:
                max_dd = 28
        else:
            max_dd = 30

        if dd > max_dd:
            print(f'Некорректный номер дня {dd:02d} для месяца {mm:02d}')
            ret_val = False

        if ret_val:
            return 'Корректная дата'
        else:
            return 'Некорректная дата'

    @classmethod
    def get_data_components(cls, str_data):
        data_list = str_data.split('-')
        return (int(data_list[i]) for i in range(len(data_list)))


d1 = data_convert('32-13-2400')
print(d1)

print('\nПроверка работы класса через создание экземпляра класса')
for i in range(20):
    dd = rnd(1, 33)
    mm = rnd(1, 15)
    yy = rnd(1700, 2300)
    d1 = data_convert(str(dd) + '-' + str(mm) + '-' + str(yy))
    print(d1)

print('\nПроверка работы класса с использованием @staticmethod')
for i in range(20):
    dd = rnd(1, 32)
    mm = rnd(1, 13)
    yy = rnd(1700, 2300)
    print(data_convert.check_data_components(dd, mm, yy))
