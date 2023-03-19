# Задача 14: Требуется вывести все целые степени двойки 
# (т.е. числа вида 2k), не превосходящие числа N.

# Из тз не ясно, что не должно превосходить число N результат возведения в степень
# или числа которые мы возводим в степень?
class NaturalNamEx(Exception):
    pass

try:
    num = int(input('Введите натуральное число n: '))
    if num <= 0:
        raise NaturalNamEx()
except ValueError:
    print('Введенно некорректное значение.')
    exit(0)
except NaturalNamEx:
    print('Введено не натуральное число.')
    exit(0)

i = 0
while 2**i <= num:
    print(2**i)
    i+=1

# # В случае если n - задает кол-во выводимых степеней двойки.
# print('')
# print('second option')
# for i in range(num):
#     print(2**i)