# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное
# число». Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте
# работу проекта. Для этого создаёте экземпляры класса (комплексные числа), выполните
# © geekbrains.ru 17
# сложение и умножение созданных экземпляров. Проверьте корректность полученного
# результата.

class complex():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return complex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return complex(self.a * other.a - self.b * other.b, self.a * other.b + self.b *other.a)

    def __str__(self):
        return f'{self.a} + {self.b} * i'

c1 = complex(1, 2)
c2 = complex(4, 9)
c3 = c1 + c2
c4 = c1 * c2
print(f'c1 = {c1}')
print(f'c2 = {c2}')
print(f'c3 = {c3}')
print(f'c4 = {c4}')