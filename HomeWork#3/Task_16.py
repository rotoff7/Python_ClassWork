# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

# Задача решалась в натуральных числах.
# Также из условия не до конца понятно откуда берутся числа в массиве.
# Если от 1 до N, то поиск повторяющихся элементов лишен смысла, 
# поэтому число в данном решении генерировались рандомно в диапазоне указанным пользователем.


import random


class NonNaturalNum(Exception):
    pass


def value_check():
    try:
        val = int(input())
        if val <= 0:
            raise NonNaturalNum()
    except ValueError:
        print('Введено некорректно значение.')
        exit(0)
    except NonNaturalNum:
        print('Число должно быть больше 0.')
        exit(0)
    else:
        return val


print('Желаемое кол-во элементов в массиве: ', end='')
how_many = value_check()
# В данной задаче можно не задавать левую границу, поскольку из условия она должна быть равна 1. (A[1..N])
print('Левая граница генерации чисел: ', end='')
left_border = value_check()
print('Правая граница генерации чисел: ', end='')
right_border = value_check()
if right_border <= left_border:
    print('Указан некорректный диапазон чисел.')
    exit(0)
nums_array = [random.randint(left_border, right_border) for i in range(how_many)]
print(f'Получившийся массив: {nums_array}')

print('Что ищем? ', end='')
look_for_num = value_check()
print(f'Искомое число "{look_for_num}" встречается в массиве {nums_array.count(look_for_num)} раз(а)')
