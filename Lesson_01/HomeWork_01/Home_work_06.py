a = int(input('Сколько километров спортсмен пробежал в 1-ый день? : '))
b = int(input('Сколько километров спортсмен должен пробегать в день : '))

i = 1
print('Результат: ')

while True:
    print(f'{i}-й день: {a:.2f} км.')
    if a > b:
        break
    i += 1
    a *= 1.1


print(f'Ответ: На {i}-й день спортсмен достиг результата — не менее {a // 1:.0f} км.')

#Коментарий для Git. Все задания выполнены
