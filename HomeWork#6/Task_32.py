# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)


import random


class BorderException(Exception):
    pass


def value_check():
    try:
        val = int(input())
    except ValueError:
        exit('Введено некорректное значение.')
    else:
        return val


def array_filler(arr_size, left_min, right_max):
    new_list = [random.randint(left_min, right_max) for i in range(arr_size)]
    return new_list


def index_finder(array, min_val, max_val):
    new_list = [i for i in range(len(array)) if min_val <= array[i] <= max_val]
    return new_list


def border_compare(l_b, r_b):
    try:
        if r_b < l_b:
            raise BorderException()
    except BorderException:
        exit('Правая граница не должна быть меньше левой.')

print('Введите размер массива:')
array_size = value_check()
print('Введите нижнюю границу значений массива:')
arr_min = value_check()
print('Введите верхнюю границу значений массива:')
arr_max = value_check()
border_compare(arr_min, arr_max)

generated_array = array_filler(array_size, arr_min, arr_max)
print(f'Получившийся исходный массив: {generated_array}')

print('Введите левую границу значений искомых индексов:')
left_val_border = value_check()
print('Введите правую границу значений искомых индексов:')
right_val_border = value_check()
border_compare(left_val_border, right_val_border)

index_array = index_finder(generated_array, left_val_border, right_val_border)
print(f'Искомые индексы: {index_array}')
