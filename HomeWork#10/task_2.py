"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""


# Хотел сделать просто через приписку b'', но не понимаю
# как внутрь поместить содержимое елемента массива, а не слово 'el'
def b_words(array):
    res_arr = []
    for el in array:
        res_arr.append(bytes(el, 'utf-8'))
    return res_arr


def result_print(array):
    for el in array:
        print(f'Содержимое: {el}. Тип: {type(el)}. Длина: {len(el)}')


words = ['class', 'function', 'method']
result_print(b_words(words))
