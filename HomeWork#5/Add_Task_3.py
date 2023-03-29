# Задание 3. Сформировать из введенного числа
# обратное по порядку входящих в него
# цифр и вывести на экран. Например, если введено число 3486,
# то надо вывести число 6843.
# Подсказка:
# На каждом шаге вам нужно 'доставать' из числа очередную цифру
# Пока все числа не извлечены рекурсивные вызовы продолжаем
# Условие завершения рекурсии - все цифры извлечены
# Используем операции % //. Операции взятия по индексу применять нельзя.
# Решите через рекурсию. В задании нельзя применять циклы.
# Пример:
# Введите число, которое требуется перевернуть: 123
# Перевернутое число: 321
# Не забудьте проверить на числе, которое оканчивается на 0.
# 1230 -> 0321


# Мой первоначальный вариант решения.
def value_check():
    try:
        val = int(input('Введите число: '))
    except ValueError:
        exit('Введено некорректное значение.')
    else:
        return val


# Разворот числа, без учета незначимых нулей
def num_reverse(num, rev_num=0):
    if num == 0:
        return rev_num
    rev_num = rev_num * 10 + num % 10
    return num_reverse(num // 10, rev_num)


# Подсчет незначимых в реверсе нулей
def zero_counter(num):
    if num % 10 != 0:
        return 0
    return 1 + zero_counter(num // 10)


# Учет незначимых нулей в виде дополнения к числу
def adding_zero(zeroes):
    if zeroes == 1:
        return '0'
    return '0' + adding_zero(zeroes - 1)


user_num = value_check()
result = num_reverse(user_num)
how_many_zero = zero_counter(user_num)
if how_many_zero > 0:
    bonus_part = adding_zero(how_many_zero)
    result = bonus_part + str(result)
    print(f'{user_num} --> {result}')
else:
    print(f'{user_num} --> {result}')


# Оптимальный вариант решения (С подсказкой):

def num_reverse_optimal(num):
    return str(num) if num < 10 else str(num % 10) + num_reverse_optimal(num // 10)


new_user_num = value_check()
new_result = num_reverse_optimal(new_user_num)
print(f'{new_user_num} --> {new_result}')
