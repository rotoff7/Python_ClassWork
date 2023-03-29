# Задание 2. Подсчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры
# (4, 6 и 0) и 2 нечетные (3 и 5).
# Подсказка:
# На каждом шаге вам нужно 'доставать' из числа очередную цифру
# и смотреть является ли она четной или нечетной.
# При этом увеличиваем соответствующий счетчик
# Пока все числа не извлечены, рекурсивные вызовы продолжаем
# Условие завершения рекурсии - все числа извлечены
# Используем операции % //. Операции взятия по индексу применять нельзя.
# Решите через рекурсию. В задании нельзя применять циклы.
# Пример:
# Введите число: 123
# Количество четных и нечетных цифр в числе равно: (1, 2)

class NaturalNum(Exception):
    pass


def value_check():
    try:
        val = int(input('Введите натуральное число: '))
        if val <= 0:
            raise NaturalNum()
    except ValueError:
        exit('Введено некорректное значение.')
    except NaturalNum:
        exit('Введено некорректное число.')
    else:
        return val


def even_odd_count(num, even_count = 0, odd_count=0):
    if num == 0:
        result_tuple = (even_count, odd_count)
        return result_tuple
    if num % 10 % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    return even_odd_count(num // 10, even_count, odd_count)


user_num = value_check()
result = even_odd_count(user_num)
print(f'Количество четных и нечетных цифр в числе {user_num} равно: {result}')
