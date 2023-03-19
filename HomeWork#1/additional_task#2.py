# Задача 2: Найдите сумму цифр трехзначного числа.
#
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# Решение работает не только для трехзначных чисел.
# Ввел доп. ограничение, чтобы решение запускалось только трехзначных.
number = int(input('Введите трехзначное число: '))
if number > 99 and number < 1000:
    print(f'Сумма цифр числа {number} -> ', end='')
    # Сперва у меня после цикла стоял вывод в виде: print ({number} -> {digitals_sum})
    # Но он выводит уже измененный циклом number (0). Пока решил проблему вводом доп. переменной.
    digitals_sum = 0
    while number > 0:
        digitals_sum += number % 10
        number //= 10
    print(digitals_sum)
else:
    print('Введено не трехзначное число!')
    exit(0)

# Решение с более красивым выводом.
number = int(input('Введите трехзначное число: '))
if number > 99 and number < 1000:
    digitals_sum = 0
    help = number
    while help > 0:
        digitals_sum += help % 10
        help //= 10
    print(f'Сумма цифр числа {number} -> {digitals_sum}')
else:
    print('Введено не трехзначное число!')
    exit(0)
