# 5.	Реализовать класс Stationery (канцелярская принадлежность).
#
# ●	определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# ●	создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# ●	в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# ●	создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery():
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('«Запуск отрисовки»')


class Pen(Stationery):
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('«Запуск отрисовки: метод РУЧКА»')


class Pencil(Stationery):
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('«Запуск отрисовки метод: КАРАНДАШ»')


class Handle(Stationery):
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('«Запуск отрисовки: метод МАРКЕР»')


a = Pen('1')
a.draw()

b = Pencil('2')
b.draw()

c = Handle('3')
c.draw()
