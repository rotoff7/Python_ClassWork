# Задача 6: Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
#
# *Пример:*
# 385916 -> yes
# 123456 -> no

ticket_number = int(input('Введите номер билета: '))
if ticket_number > 99999 and ticket_number < 1000000:
    sum_first_digits = 0
    sum_last_digits = 0
    print(f'Билет с номером: {ticket_number} -> ', end='')
    while ticket_number > 999:
        sum_last_digits += ticket_number % 10
        ticket_number //= 10
    while ticket_number > 0:
        sum_first_digits += ticket_number % 10
        ticket_number //= 10
    if sum_first_digits == sum_last_digits:
        print('является счастливым.')
    else:
        print('не является счастливым.')
else:
    print('Введен некорректный номер билета. Номер должен содержать 6 цифр.')