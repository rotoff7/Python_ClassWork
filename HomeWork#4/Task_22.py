# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

class IncorrectValue(Exception):
    pass


def value_check():
    try:
        val = int(input())
        if val < 1:
            raise IncorrectValue()
    except ValueError:
        print('Введено некорректное значение.')
        exit(0)
    except IncorrectValue:
        print('Введено некорректное значение.')
        exit(0)
    else:
        return (val)


def set_filling(set_size):
    new_array = [int(input()) for i in range(set_size)]
    return new_array


print('Введите размер первого набора чисел: ', end='')
array1_size = value_check()
print('Введите размер второго набора чисел: ', end='')
array2_size = value_check()

print('Введите элементы первого массива (enter - подтверждение ввода элемента): ')
array1 = set_filling(array1_size)
print('Введите элементы второго массива (enter - подтверждение ввода элемента): ')
array2 = set_filling(array2_size)

print('Получившиеся массивы чисел:')
print(array1)
print(array2)

array1.sort()
array2.sort()

set1 = set(array1)
set2 = set(array2)

print('Получившиеся множества без дубликатов элементов: ')
print(set1)
print(set2)

print(f'В обоих массивах встречаются следующие числа: {(set1 & set2)}')
