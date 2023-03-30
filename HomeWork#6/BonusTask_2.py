# 2. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

# Реализуйте вариант без и с LC



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


# Заполнение с LC
def array_filler(arr_size, left_min, right_max):
    new_list = [random.randint(left_min, right_max) for i in range(arr_size)]
    return new_list


def border_compare(l_b, r_b):
    try:
        if r_b < l_b:
            raise BorderException()
    except BorderException:
        exit('Правая граница не должна быть меньше левой.')


# Без LC
def select_elems(array):
    new_list = list()
    for i in range(1, len(array)):
        if array[i] > array[i - 1]:
            new_list.append(array[i])
    return new_list


# С LC
def select_elems_lc(array):
    new_list = [array[i] for i in range(1, len(array)) if array[i] > array[i-1]]
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

result_array = select_elems(generated_array)
print(f'Массив нужных элементов: {result_array}')

result_array_lc = select_elems_lc(generated_array)
print(f'Массив искомых элементов через LC {result_array_lc}')
