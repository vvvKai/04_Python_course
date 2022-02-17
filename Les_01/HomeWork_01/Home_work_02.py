time_seconds = int(input('Введите время в секундах: '))

hours_in_seconds = 3600
minute_in_seconds = 60

hours = time_seconds // hours_in_seconds
minutes = (time_seconds % hours_in_seconds) // minute_in_seconds
seconds = (time_seconds % hours_in_seconds) % minute_in_seconds

print(f'Введеное время в формате "чч:мм:сс" составляет: {hours:02d}:{minutes:02d}:{seconds:02d}')


#Коментарий для Git. Все задания выполнены