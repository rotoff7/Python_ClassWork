# 1. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите два варианта решения: через list и через dict.

# Пример:
# Введите номер месяца: 10
# Результат через список: Осень
# Результат через словарь: Осень

class MonthNumRange(Exception):
    pass

def ValueCheck():
    try:
        val = int(input('Введите номер месяца: '))
        if val < 1 or val > 12:
            raise MonthNumRange()
    except ValueError:
        print('Введено некорректное значение.')
        exit(0)
    except MonthNumRange:
        print('Месяца под таким номером не существует.')
        exit(0)
    else:
        return val


# Решение через список. V1.
seasons = ['Зима', 'Весна', 'Лето', 'Осень']
month = ValueCheck()
if 3 <= month <= 5:
    print(seasons[1])
elif 6 <= month <= 8:
    print(seasons[2])
elif 9 <= month <= 11:
    print(seasons[3])
else:
    print(seasons[0])

# Решение через список. V2.
# Не знаю как корректно избавиться от дублирования элементов массива.
seasons2 = ['Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето', 'Осень', 'Осень', 'Осень', 'Зима']
month2 = ValueCheck()
print(f'Сезон соответствующий номеру месяца: {seasons2[month2 - 1]}')

# Решение через словарь
seasons_dict = {'Зима': [1,2,12], 'Весна': [3,4,5], 'Лето': [6,7,8], 'Осень':[9,10,11]}
month_dict = ValueCheck()
for k, v in seasons_dict.items():
    for el in v:
        if el == month_dict:
            print(f'Сезон соответствующий номеру месяца: {k}')