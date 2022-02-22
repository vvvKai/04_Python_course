debit = int(input('Введите значение выручки: '))
credit = int(input('Введите значение издержек: '))

if debit > credit:
    print('Вы успешны, дела идут прибыльно!')
    rent = int((debit/credit)*100-100)
    print(f'Рентабельность фирмы составляет {rent}%')
    people = int(input('Введите количество сотрудников: '))
    profit = int((debit-credit)/people)
    print(f'Прибыль фирмы в расчёте на одного сотрудника составляет {profit} рублей')
else:
    print('Упс, убытки, задумайтесь!')

    # Коментарий для Git. Все задания выполнены