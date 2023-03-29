# Задание 4. Найти сумму n элементов следующего ряда чисел:
# 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.
# Пример:
# Введите количество элементов: 3
# Количество элементов - 3, их сумма - 0.75
# Решите через рекурсию. В задании нельзя применять циклы.
# Нужно обойтисть без создания массива!

class NaturalNum(Exception):
    pass


def value_check():
    try:
        val = int(input('Введите кол-во элементов ряда: '))
        if val <= 0:
            raise NaturalNum()
    except ValueError:
        exit('Введено некорректное значение.')
    except NaturalNum:
        exit('Введено некорректное значение.')
    else:
        return val


def row_sum(quantity, start_point=1, index=1):
    if quantity == 1:
        if index % 2 == 0:
            start_point = start_point * -1
            return start_point
        return start_point
    if index % 2 == 1:
        return start_point + row_sum(quantity - 1, start_point / 2, index + 1)
    else:
        return -1 * start_point + row_sum(quantity - 1, start_point / 2, index + 1)


n_quantity = value_check()
result = row_sum(n_quantity)
print(f'Кол-во элементов - {n_quantity}, их сумма - {result}')
