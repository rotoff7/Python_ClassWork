# Задание 7. Напишите программу, доказывающую или проверяющую, что для множества
# натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
# где n - любое натуральное число.
# Пример:
# для n = 5
# 1+2+3+4+5 = 5(5+1)/2
# Нужно написать рекурсивную ф-цию только для левой части выражения!
# Результат нужно сверить с правой частью.
# Правой части выражения в рекурсивной ф-ции быть не должно!
# Решите через рекурсию. В задании нельзя применять циклы.


class NaturalNum(Exception):
    pass

def value_check():
    try:
        val = int(input('Введите натуральное число: '))
        if val <= 0:
            raise NaturalNum()
    except ValueError:
        exit('Введено некорректное число.')
    except NaturalNum:
        exit('Введено некорректное число.')
    else:
        return val

# Рекурсия
def left_part(val):
    if val == 1:
        return val
    return val + left_part(val - 1)

def parts_compare(left, right):
    if left == right:
        print(f'При значении n={user_num}, данное равенство: "1+2+3...n = n(n+1)/2" -> выполняется ({left} = {right}).')
    else:
        print(f'Равенство: "1+2+3...n = n(n+1)/2", при n={user_num}, не выполняется.')

user_num = value_check()
left_part_sum = left_part(user_num)
right_part_sum = user_num * (user_num + 1) // 2
parts_compare(left_part_sum, right_part_sum)
