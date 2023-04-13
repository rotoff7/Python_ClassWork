"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""


def bytes_convert(array):
    res_arr = []
    for el in array:
        res_arr.append(el.encode('utf-8'))
    return res_arr


def words_convert(array):
    res_arr = []
    for el in array:
        res_arr.append(el.decode('utf-8'))
    return res_arr


words = ['разработка', 'администрирование', 'protocol', 'standard']
print('Байтовое представление:')
b_words = bytes_convert(words)
for element in b_words:
    print(element)
print('')
print('Буквенное представление:')
let_words = words_convert(b_words)
print(let_words)
