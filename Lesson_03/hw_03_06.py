# 6.	Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.


def int_func(text):
    if text.islower():
        text = list(text.split(' '))
        result = ''
        for el in text:
            letter_1st = el[0].upper()
            el_up = letter_1st + el[1:]
            result = result + ' ' + str(el_up)
        return result[1:]
    else:
        print('Строка/слово должны состоять из букв нижнего регистра.')
        return ''


print(int_func('text one two three'))
