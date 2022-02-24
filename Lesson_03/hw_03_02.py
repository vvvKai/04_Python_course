# 2.
# Выполнить функцию, которая принимает несколько параметров,
# описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.
# name, surname, birth, city, email, phone

def data_user(name, surname, birth, city, email, phone):
    print(f'Имя - {name}, Фамилия - {surname}, Год рождения - {birth}, Город проживания - {city}, email - {email}, Телефон - {phone}')
    return

data_user(name='Vasya', surname='Pupkin', birth='2000', city='Moscow', email='vasya@mail.ru', phone='880080055')
data_user(name='Петя', surname='Петров', birth='2005', city='Ростов', email='petya@mail.ru', phone='880080056')
data_user(name='Маша', surname='Иванова', birth='1985', city='Сочи', email='masha@mail.ru', phone='880080057')
