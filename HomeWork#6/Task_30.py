# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


def value_check():
    try:
        val = int(input())
    except ValueError:
        exit('Введено некорректное значение')
    else:
        return val


def arith_progression(first_el, difference, el_quantity):
    new_list = [first_el]
    for i in range(1, el_quantity):
        new_list.append(new_list[i - 1] + difference)
    return new_list


def print_in_diff_lines(array):
    for el in array:
        print(el)


print('Введите первый элемент прогрессии: ')
el_1 = value_check()
print('Введите разницу между элементами: ')
diff = value_check()
print('Введите кол-во элементов в прогрессии: ')
how_many = value_check()

progression_list = arith_progression(el_1, diff, how_many)
print(f'Получившийся массив прогрессии: {progression_list}')
print('Вывод построчно:')
print_in_diff_lines(progression_list)
