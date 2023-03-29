# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8 

def value_check():
    try:
        val = int(input())
    except ValueError:
        print("Введено некорректное значение.")
        exit(0)
    else:
        return val
    
def num_degree(num1, num2):
    if num2 == 1:
        return num1
    return num1 * num_degree(num1, num2 - 1)



print('Введите целое число A: ')
num_a = value_check()
print('Введите целое число B: ')
num_b = value_check()

result = num_degree(num_a, num_b)
print(f'{num_a} в степени {num_b} = {result}')