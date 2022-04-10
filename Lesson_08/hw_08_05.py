# Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём
# оргтехники на склад и передачу в определённое подразделение компании. Для хранения
# данных о наименовании и количестве единиц оргтехники, а также других данных, можно
# использовать любую подходящую структуру (например, словарь).

import shop

s1 = shop.store(1, 'Основной склад', 'ул. Ленина, 1', 'Иванов И.И.', {})
s1.store_info()

s2 = shop.store(2, 'Магазин-1', 'ул. Московская, 1', 'Петров П.П.', {})
s2.store_info()

s3 = shop.store(3, 'Магазин-2', 'ул. Ломоносова, 1', 'Сидоров С.С.', {})
s3.store_info()

dev1 = shop.projector(1, 'Проектор Philips NeoPix Easy+ серебристый', '111111', 'China', 'LCD', '800x600', 10000)
# dev1.info()

dev2 = shop.printer(2, 'Принтер лазерный HP Laser 107r', '12345', 'China', 'laser', 'mono', '16ppm')
# dev2.info()

dev3 = shop.scanner(3, 'Сканер Epson Perfection V19', '222222', 'Hungary', 'Планшетный', 'A4', '4096x4096', '4ppm')
# dev3.info()

s1.move_dev('in', {dev1: 2, dev2: 4, dev3: 5})
s1.print_dev_count()
s1.move_dev('in', {dev2: 1, dev3: 1, dev1: 2})
s1.print_dev_count()

s2.move_dev('in', {dev1: 1, dev2: 1, dev3: 1})
s2.print_dev_count()

s3.move_dev('in', {dev2: 2, dev3: 2, dev1: 2})
s3.print_dev_count()

# перемещение товара между складами:
s1.move_dev('out', {dev1: 1, dev2: 2, dev3: 5})
s2.move_dev('in', {dev1: 1, dev2: 2, dev3: 5})
s1.print_dev_count()
s2.print_dev_count()
