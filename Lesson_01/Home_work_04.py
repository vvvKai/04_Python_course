num = int(input('Введите целое положительное число n: '))
num_max = 0

while num > 0:
    num_part = num % 10
    if num_part > num_max:
        num_max = num_part
    num = num // 10

print('Cамую большая цифра в числе: ', num_max)
