# 4.	Реализуйте базовый класс Car.
#
# ●	у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# ●	опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# ●	добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# ●	для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

class Car():
    def __init__(self, name, color, max_speed, is_police=False):
        self.max_speed = max_speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.status = 'Остновлена'
        self.speed = 0
        print(f'Создан автомобиль: {self.name}, цвет: {self.color}')

    def go(self):
        print(f'{self.name} - поехала')
        self.status = 'Движеться'
        self.speed = self.max_speed

    def stop(self):
        print(f'{self.name} - остановилась')
        self.status = 'Остновлена'
        self.speed = 0

    def turn(self, direction):
        self.direction = direction
        print(f'{self.name} - движется {self.direction}')
        self.status = 'Движеться'
        self.status_speed = self.speed

    def show_speed(self):
        print(f'Текущая скорость авто: {self.speed} \nТекщее состояние авто: {self.status}')

    def change_speed(self, speed):
        self.speed = speed
        print(f'{self.name} - изменила скорость движения, новая скорость {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, name, color, max_speed=60, is_police=False):
        super().__init__(name, color, max_speed, is_police)

    def show_speed(self):
        print(f'Текущая скорость авто: {self.speed} \nТекщее состояние авто: {self.status}')
        if self.speed >= 60:
            print(f'ПРЕДУПРЕЖДЕНИЕ: ПРЕВЫШЕНИЕ СКОРОСТИ, Макс. допусутимая скорость 60 км/ч')


class WorkCar(Car):
    def __init__(self, name, color, max_speed=40, is_police=False):
        super().__init__(name, color, max_speed, is_police)

    def show_speed(self):
        print(f'Текущая скорость авто: {self.speed} \nТекщее состояние авто: {self.status}')
        if self.speed >= 40:
            print(f'ПРЕДУПРЕЖДЕНИЕ: ПРЕВЫШЕНИЕ СКОРОСТИ, Макс. допусутимая скорость 40 км/ч')


class SportCar(Car):
    def __init__(self, name, color, max_speed=180, is_police=False):
        super().__init__(name, color, max_speed, is_police)


class PoliceCar(Car):
    def __init__(self, name, color, max_speed=210, is_police=True):
        super().__init__(name, color, max_speed, is_police)


car_1 = TownCar('Lada Vesta', 'Красный', 50)
car_1.show_speed()
car_1.go()
car_1.show_speed()
car_1.turn("Направо")
car_1.show_speed()
car_1.change_speed(80)
car_1.show_speed()
car_1.stop()
car_1.show_speed()
print('')

car_2 = PoliceCar('Skoda Octavia', 'Белый', 80)
car_2.show_speed()
car_2.go()
car_2.show_speed()
car_2.turn("Прямо")
car_2.change_speed(180)
car_2.show_speed()
car_2.stop()
car_2.show_speed()
print('')

car_3 = TownCar('Lada Granta', 'Синий', 80)
car_3.show_speed()
car_3.go()
car_3.show_speed()
car_3.turn("Направо")
car_3.change_speed(100)
car_3.show_speed()
car_3.stop()
car_3.show_speed()
print('')

car_3 = WorkCar('Камаз', 'Зеленый', 50)
car_3.show_speed()
car_3.go()
car_3.show_speed()
car_3.turn("Прямо")
car_3.show_speed()
car_3.stop()
car_3.show_speed()
