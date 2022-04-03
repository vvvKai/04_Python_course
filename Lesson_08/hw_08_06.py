# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
# пользователем данных. Например, для указания количества принтеров, отправленных на
# склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

import shop

store_lst = []
dev_lst = []

store_lst.append(shop.store(1, 'Основной склад', 'ул. Ленина, 1', 'Иванов И.И.', {}))
store_lst.append(shop.store(2, 'Магазин-1', 'ул. Московская, 1', 'Петров П.П.', {}))
store_lst.append(shop.store(3, 'Магазин-2', 'ул. Ломоносова, 1', 'Сидоров С.С.', {}))
dev_lst.append(shop.projector(1, 'Проектор Philips NeoPix Easy+ серебристый', '111111', 'China', 'LCD', '800x600', 10000))
dev_lst.append(shop.printer(2, 'Принтер лазерный HP Laser 107r', '12345', 'China', 'laser', 'mono', '16ppm'))
dev_lst.append(shop.scanner(3, 'Сканер Epson Perfection V19', '222222', 'Hungary', 'Планшетный', 'A4', '4096x4096', '4ppm'))
print('Выполняем заполнение складов остатками товара')
store_lst[0].move_dev('in', {dev_lst[0]: 2, dev_lst[1]: 4, dev_lst[2]: 5})
store_lst[0].move_dev('in', {dev_lst[1]: 1, dev_lst[2]: 1, dev_lst[0]: 2})
store_lst[1].move_dev('in', {dev_lst[0]: 1, dev_lst[1]: 1, dev_lst[2]: 1})
store_lst[2].move_dev('in', {dev_lst[1]: 2, dev_lst[2]: 2, dev_lst[0]: 2})

def check_store(store_id):
    # проверка пользовательского ввода номера склада
    store = None
    for i in store_lst:
        if i.store_id == store_id:
            store = i
            break

    return store


def print_store_list():
    for i, store in enumerate(store_lst):
        print(f'{i+1}. {store.store_name}')


def get_store(msg):
    print(msg)
    print_store_list()
    store_id = input('Введите id склада (пустую строку для отмены операции): ')

    store = None
    try:
        store_id = int(store_id)
    except ValueError:
        print('Введено не числовое значение либо пустая строка!')
    else:
        store = check_store(store_id)
        if not store:
            print('В списке складов отсутствует введенное значение!')

    return store

def get_dev_by_id(dev_id):
    # проверка пользовательского ввода id товара
    dev = None
    for i in dev_lst:
        if i.id == dev_id:
            dev = i
            break

    return dev


def parse_dev_count(store, str_dev_count):
    dev_count = {}

    try:
        # разбиваем строку  с количеством товара на отдельные позиции
        lst1 = str_dev_count.split(',')
    except:
        print(f'Ошибка при обработке введенной строки: {str_dev_count}')
    else:
        for i in lst1:
            try:
                # разбиваем каждую позицию на id товара и количество
                parse_dev_id, parse_dev_count = i.split(' ')
                parse_dev_id = int(parse_dev_id)
                parse_dev_count = int(parse_dev_count)
            except:
                print(f'Ошибка при обработке введенной подстроки: {i}, будет проигнорирована!')
            else:
                # записываем в возвращаемый словарь из пользовательского ввода количество по каждой позиции
                dev = get_dev_by_id(parse_dev_id)
                if not dev:
                    print(f'Товар с id = {parse_dev_id} не найден в справочнике, будет проигнорирован!')
                else:
                    dev_count[dev] = parse_dev_count

    return dev_count


while True:
    from_store = None
    to_store = None
    dev_count = None

    from_store = get_store('\nДля операции перемещения товара выберите склад-источник: ')
    if not from_store:
        print('Операция отменена!')
        break

    to_store = get_store('\nВыберите склад-получатель: ')
    if not to_store:
        print('Операция отменена!')
        break

    from_store.print_dev_count()
    str_dev_count = input('Введите через запятую количество перемещаемого товара в формате: <№ товара><пробел><количество>: ')

    dev_count = parse_dev_count(from_store, str_dev_count)
    if len(dev_count) == 0:
        print('Не удалось распознать введенную строку!')
    else:
        if from_store.check_count(dev_count):
            from_store.move_dev('out', dev_count)
            to_store.move_dev('in', dev_count)
            print('Операция перемещения товара выполнена. Остатки товара на складах после перемещения:')
            from_store.print_dev_count()
            to_store.print_dev_count()
        else:
            print('Операция перемещения товаров не выполнена!')
