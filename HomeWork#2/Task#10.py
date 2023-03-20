# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток,
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

import random


class CorrectNums(Exception):
    pass


try:
    coins = int(input('Введите кол-во монеток: '))
    if coins <= 0:
        raise CorrectNums()
except ValueError:
    print('Введено некорректное значение.')
    exit(0)
except CorrectNums:
    print('Число должно быть больше нуля.')
    exit(0)

tails = random.randint(1, coins - 1)
eagle = coins - tails

print(f'Кол-во монеток повернутых орлом вверх: {eagle}')
print(f'Кол-во монеток повернутых решкой вверх: {tails}')

if tails > eagle:
    print(f'Нужное перевернуть {eagle} монетки, чтобы все монетки были повернуты одной стороной')
else:
    print(f'Нужное кол-во монет, необходимых перевернуть, чтобы все монетки были повернуты одной стороной: {tails}')

# С циклом.

print('')
print('Второй способ.')
try:
    coins2 = int(input('Введите кол-во монеток: '))
    if coins2 <= 0:
        raise CorrectNums()
except ValueError:
    print('Введено некорректное значение.')
    exit(0)
except CorrectNums:
    print('Число должно быть больше нуля.')
    exit(0)

tails2 = 0
eagles2 = 0
for i in range(coins2):
    try:
        help_val = int(input('Какой стороной повернута монетка? 0 - орел, 1 - решка: '))
        if help_val != 0 and help_val != 1:
            raise CorrectNums()
    except ValueError:
        print('Введено некорректное значение.')
        exit(0)
    except CorrectNums:
        print('Число должно быть равное 0 или 1.')
        exit(0)
    if help_val == 0:
        eagles2 += 1
    else:
        tails2 += 1

print(f'Кол-во монеток повернутых орлом вверх: {eagles2}')
print(f'Кол-во монеток повернутых решкой вверх: {tails2}')

if tails2 > eagles2:
    print(f'Нужное перевернуть {eagles2} монетки, чтобы все монетки были повернуты одной стороной')
else:
    print(f'Нужное кол-во монет, необходимых перевернуть, чтобы все монетки были повернуты одной стороной: {tails2}')
