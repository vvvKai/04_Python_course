# 1.	Создать класс TrafficLight (светофор).
#
# ●	определить у него один атрибут color (цвет) и метод running (запуск);
# ●	атрибут реализовать как приватный;
# ●	в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# ●	продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# ●	переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# ●	проверить работу примера, создав экземпляр и вызвав описанный метод.
#
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и завершать скрипт.

import time


class TrafficLight:
    red_color = 'Красный'
    orange_color = 'Желтый'
    green_color = 'Зеленый'

    red_time = 7
    orange_time = 2
    green_time = 4

    def __init__(self, color=red_color):
        self.__color = color
        print(f'Создан новый объект СвЕтОфОр с начальным цветом {self.__color}')

    def change_color(self, color, wait_period):
        self.wait_period = wait_period
        print(f'Включен {color} свет, время ожидания {self.wait_period} сек')
        time.sleep(self.wait_period)

    def running(self, color=red_color):
        if not color:
            loc_color = self.__color
        else:
            loc_color = color

        if loc_color == self.red_color:
            self.change_color(TrafficLight.red_color, self.red_time)
            self.change_color(TrafficLight.orange_color, self.orange_time)
            self.change_color(TrafficLight.green_color, self.green_time)
        elif loc_color == self.orange_color:
            self.change_color(TrafficLight.orange_color, self.orange_time)
            self.change_color(TrafficLight.green_color, self.green_time)
        elif loc_color == self.green_color:
            self.change_color(TrafficLight.green_color, self.green_time)
        else:
            print("ВВЕДЕН НЕВЕРНЫЙ АРГУМЕНТ")

        print('Цикл переключения цветов завершен')


a = TrafficLight()
a.running()
a.running('Желтый')
a.running('Зеленый')
a.running('Синий')
