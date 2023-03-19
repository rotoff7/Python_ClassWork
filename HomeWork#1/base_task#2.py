# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
#
# Пример:
# Введите время в секундах: 3600
# Время в формате ч:м:с - 1.0 : 60.0 : 3600
# """
# """

# Решение без ввода доп. переменных

time_in_seconds = int(input('Введите время в секундах: '))
print(f'Время в формате ч:м:с - {time_in_seconds / 3600} : {time_in_seconds / 60} : {time_in_seconds}')

# Решение с вводом доп. переменных

time_in_seconds = int(input('Введите время в секундах: '))
time_in_hours = time_in_seconds / 3600
time_in_minutes = time_in_seconds / 60
print(f'Время в формате ч:м:с - {time_in_hours} : {time_in_minutes} : {time_in_seconds}')
