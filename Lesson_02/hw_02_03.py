# Решение с использованием dict

months_dict = {
    'Зима': (12, 1, 2),
    'Весна': (3, 4, 5),
    'Лето': (6, 7, 8),
    'Осень': (9, 10, 11)
}

user_month = int(input('Введите номер месяца: '))

for key in months_dict:
    if user_month in months_dict[key]:
        print('Введенный номер месяца относится к сезону:', key)

# Решение с использованием list

month_list = [['Зима', 12, 1, 2], ['Весна', 3, 4, 5], ['Лето', 6, 7, 8], ['Осень', 9, 10, 11]]


for i, el in enumerate(month_list):
    if user_month in el[1:4]:
        print(f'Введенный номер месяца относится к сезону: {el[0]}')
