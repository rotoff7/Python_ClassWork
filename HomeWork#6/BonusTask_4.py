# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать LC.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

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


def border_compare(l_b, r_b):
    try:
        if r_b < l_b:
            raise BorderException()
    except BorderException:
        exit('Правая граница не должна быть меньше левой.')


# Выборка нужны элементов с использование LC
def elems_select(array):
    new_list = [el for el in array if array.count(el) == 1]
    return new_list


print('Введите размер массива:')
array_size = value_check()
print('Введите нижнюю границу значений массива:')
arr_min = value_check()
print('Введите верхнюю границу значений массива:')
arr_max = value_check()
border_compare(arr_min, arr_max)

generated_array = array_filler(array_size, arr_min, arr_max)
print(f'Получившийся исходный массив: {generated_array}')

result_array = elems_select(generated_array)
print(f'Результирующий массив: {result_array}')
