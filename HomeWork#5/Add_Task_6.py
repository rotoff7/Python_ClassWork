# Задание 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток. После каждой
# неудачной попытки должно сообщаться больше или меньше введенное пользователем
# число, чем то, что загадано. Если за 10 попыток число не отгадано,
# то вывести загаданное число.
# Решите через рекурсию. В задании нельзя применять циклы.

import random


class IncorrectRange(Exception):
    pass


def value_check():
    try:
        val = int(input('Введите число от 0 до 100: '))
        if val < 0 or val > 100:
            raise IncorrectRange()
    except ValueError:
        print('Введено некорректное значение.')
        exit(0)
    except IncorrectRange:
        print('Введено некорректное значение.')
        exit(0)
    else:
        return val


def find_num(num, counter):
    print(f'Осталось попыток: {counter}')
    maybe_num = value_check()
    if maybe_num == num:
        print('Вы угадали число!')
    elif counter == 1:
        print(f'Попытки закончились. Загаданное число -> {num}')
    else:
        if maybe_num < num:
            print('Не угадали, попробуйте ввести число побольше.')
            find_num(num, counter - 1)
        else:
            print('Не угадали, попробуйте ввести число поменьше.')
            find_num(num, counter - 1)


magic_num = random.randint(0, 100)
attempts = 10
print('Угадайте загаданное число.')
find_num(magic_num, attempts)
