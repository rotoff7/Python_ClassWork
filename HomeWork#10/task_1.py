"""
Задание 1.

Каждое из слов «разработка», «сокет», «декоратор» представить
в буквенном формате и проверить тип и содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать
в набор кодовых точек Unicode (НО НЕ В БАЙТЫ!!!)
и также проверить тип и содержимое переменных.

*Попытайтесь получить кодовые точки без онлайн-конвертера!
без хардкода!

Подсказки:
--- 'разработка' - буквенный формат
--- '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430' - набор кодовых точек
--- используйте списки и циклы, не дублируйте функции
"""


# 1 версия. Тип данных: байты (b'\\u0440....)
# def code_points(array):
#     c_p_array = []
#     for el in array:
#         c_p_array.append(el.encode("unicode_escape", "utf-8"))
#     return c_p_array

def code_points(array):
    c_p_array = []
    for el in array:
        temp = (el.encode("unicode_escape", "utf-8"))
        c_p_array.append(temp.decode('utf-8'))
    return c_p_array


def result_printing(w_array, cp_array):
    for i in range(len(w_array)):
        print(f'Слово "{w_array[i]}" - буквенный формат.')
        print(f'Тип данных: {type(w_array[i])}')
        print(f'{cp_array[i]} - набор кодовых точек')
        print(f'Тип данных: {type(cp_array[i])}')
        print('')


words = ['разработка', 'сокет', 'декоратор']
code_points_arr = code_points(words)
result_printing(words, code_points_arr)
