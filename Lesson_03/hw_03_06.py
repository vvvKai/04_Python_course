# 6.	Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

def int_func(input_text):
    return input_text.title()

print(int_func('text one two true'))

