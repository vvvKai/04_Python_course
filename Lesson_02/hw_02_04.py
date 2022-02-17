user_str = input('Вводите строку из нескольких слов, разделённых: ')

user_list = list(user_str.split())

for ind, el in enumerate(user_list, 1):
    if len(el) > 10:
        el = el[:10]
    print(f'{ind} - {el}')
