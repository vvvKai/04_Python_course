# n = int(input('Введите число N: '))
# print(n)
# print(n*11)
# print(n*111)
# print(n+n*11+n*111)

# or_password = '1234'
# password = input('Enter pass: ')
#
# if password == or_password:
#     print('OK')
# else:
#     print('NOT OK')

# num = int(input('Введите число 0-9: '))
#
# while num <= 10:
#     print(num)
#     num += 1

# i = 0
# while True:
#     i +=1
#     if i >= 10:
#         break
#     if i % 2 == 0:
#         continue
#     print(i)

age = 29
name = 'Gary'
print('Вас зовут %s, Вам %d лет' % (name, age))
print('Вас зовут {}, Вам {} лет'.format (age, name))
print(f'Вас зовут {name}, Вам {age} лет')

print(f'{8/11:.5f}')
print(f'{55:05d}')
print(f'Dear {name:^25}!')


