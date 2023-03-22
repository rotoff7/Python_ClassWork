# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5


# Решение находит первый встретившийся наиболее близкий по значению элемент.

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

index = 0
difference = abs(nums_array[0] - look_for_num)
for i in range(how_many):
    if abs(nums_array[i] - look_for_num) < difference:
        index = i
        difference = abs(nums_array[i] - look_for_num)

print(f'Наиболее близкий по значению к "{look_for_num}" {index + 1}-й '
      f'элемент массива, имеющий значение: {nums_array[index]}')
