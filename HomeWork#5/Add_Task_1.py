# Задание 1. Написать программу, которая будет складывать, вычитать,
# умножать или делить два числа. Числа и знак операции вводятся пользователем.
# После выполнения вычисления программа не должна завершаться, а должна
# запрашивать новые данные для вычислений. Завершение программы должно
# выполняться при вводе символа '0' в качестве знака операции. Если пользователь
# вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
# сообщать ему об ошибке и снова запрашивать знак операции.
# Также сообщать пользователю о невозможности деления на ноль,
# если он ввел 0 в качестве делителя.
# Подсказка:
# Вариант исполнения:
# - условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
# - условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ
# Решите через рекурсию. В задании нельзя применять циклы.
# Пример:
# Введите операцию (+, -, *, / или 0 для выхода): +
# Введите первое число: 214
# Введите второе число: 234
# Ваш результат 448
# Введите операцию (+, -, *, / или 0 для выхода): -
# Введите первое число: вп
# Вы вместо трехзначного числа ввели строку (((. Исправьтесь
# Введите операцию (+, -, *, / или 0 для выхода):


# В условии не было сказано о том, что произойдет если пользователь
# введет некорректное число, поэтому в данном решении программа просто
# завершает работу с сообщением о неверном значении.

def value_check():
    try:
        val = int(input())
    except ValueError:
        exit('Введено некорректное значение.')
    else:
        return val


def first_num():
    print('Введите первое число: ', end='')
    num1 = value_check()
    return num1


def second_num():
    print('Введите второе число: ', end='')
    num2 = value_check()
    return num2


def calculations():
    sign = input('Введите операцию (+, -, *, / или 0 для выхода): ')
    if sign == '0':
        print('Завершение работы программы.')
        return
    elif sign == '+':
        user_num1 = first_num()
        user_num2 = second_num()
        print(f'Ваш результат: {user_num1 + user_num2}')
        calculations()
    elif sign == '-':
        user_num1 = first_num()
        user_num2 = second_num()
        print(f'Ваш результат: {user_num1 - user_num2}')
        calculations()
    elif sign == '*':
        user_num1 = first_num()
        user_num2 = second_num()
        print(f'Ваш результат: {user_num1 * user_num2}')
        calculations()
    elif sign == '/':
        user_num1 = first_num()
        user_num2 = second_num()
        if user_num2 != 0:
            print(f'Ваш результат: {user_num1 // user_num2}')
        else:
            print('Деление на ноль невозможно')
        calculations()
    else:
        print('Введен некорректный знак операции. Повторите ввод.')
        calculations()


calculations()
