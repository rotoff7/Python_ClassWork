# Задание 3.
#
# Узнайте у пользователя целое положительное число n.
# Найдите сумму чисел n + nn + nnn.
#
# Пример:
# Введите число n: 3
# n + nn + nnn = 369
# """
# """

# Первый вариант решения (простой). Работает только с однозначными числами.

number = int(input('Введите целое положительное число n: '))
nn = number * 10 + number
nnn = number * 100 + number * 10 + number
print(f'n + nn + nnn = {number + nn + nnn}')

# Второй вариант решения. Работает с числами больше 9.

number2 = input('Введите целое положительное число n: ')
nn2 = (number2 + number2)
nnn2 = (number2 + number2 + number2)

nn2_to_int = int(nn2)
nnn2_to_int = int(nnn2)
number1_to_int = int(number2)

answer = nnn2_to_int + nn2_to_int + number1_to_int
print(f'n + nn + nnn = {answer}')
