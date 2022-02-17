my_list = [7, 5, 3, 3, 2]
print('Исходный список: ', my_list)
print('Для выхода из программы введите: 0')

while True:
    user_number = int(input('Введите натуральное число: '))
    my_list.append(user_number)
    my_list = sorted(my_list, key=None, reverse=True)
    print(my_list)
    if user_number == 0:
        break
