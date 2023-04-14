"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" исключение,
придумайте как это сделать
"""


def b_words(array):
    res_arr = []
    try:
        for el in array:
            res_arr.append(bytes(el, 'ascii'))
    except UnicodeEncodeError:
        print("Слово невозможно записать в байтовом типе с помощью маркировки b''")
    return res_arr


words = ['attribute', 'класс', 'функция', 'type']
result = b_words(words)
print(result)
