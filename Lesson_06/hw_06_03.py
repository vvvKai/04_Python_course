# 3.	Реализовать базовый класс Worker (работник).
#
# ●	определить атрибуты: name, surname, position (должность), income (доход);
# ●	последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# ●	создать класс Position (должность) на базе класса Worker;
# ●	в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
# ●	проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров

class Worker():
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self._income = {'wage': self.wage, 'bonus': self.bonus}


class Position(Worker):
    def get_full_name(self):
        return print('Полное имя и фамилия: ', self.name + ' ' + self.surname)

    def get_total_income(self):
        return print('Полный доход: ', self._income.get('wage') + self._income.get('bonus'), 'руб. \n')


person_1 = Position('Иван', 'Иванов', 'Кладовщик', 1000, 200)
person_2 = Position('Василий', 'Пупкин', 'Любитель Python', 1000, 1000)
person_3 = Position('Алла', 'Пугачева', 'Певица', 9999, 999999)

person_list = [person_1, person_2, person_3]

for el in person_list:
    print('Проверяем значения переданных атрубтов:')
    print(
        f'Имя - {el.name} \nФамилия - {el.surname} \nДолжность - {el.position} \nОклад - {el.wage} руб. \nБонус - {el.bonus} руб.')
    print('Проверяем методы экземляра класса:')
    el.get_full_name()
    el.get_total_income()
