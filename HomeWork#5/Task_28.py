# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму 
# двух целых неотрицательных чисел. Из всех арифметических операций 
# допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*
# 2 2
#     4 

class PositiveNums(Exception):
    pass


def value_check():
    try:
        val = int(input())
        if val < 0:
            raise PositiveNums
    except ValueError:
        print("Введено некорректное значение.")
        exit(0)
    except PositiveNums:
        print("Введено некорректное значение.")
        exit(0)
    else:
        return val


def num_sum(num1, num2):
    if num1 == 0:
        return num2
    return 1 + num_sum(num1 - 1, num2)


print('Введите целое число A: ')
num_a = value_check()
print('Введите целое число B: ')
num_b = value_check()

result = num_sum(num_a, num_b)
print(f'Сумма чисел {num_a} и {num_b} = {result}')
