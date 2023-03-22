# 3. Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Далее необходимо собрать аналитику о товарах. Реализовать словарь,
# в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “названия”: [“компьютер”, “принтер”, “сканер”],
# “цены”: [20000, 6000, 2000],
# “количества”: [5, 2, 7],
# “ед”: [“шт.”]
# }


# i = 1
# goods = list()
# goods.append((i, {input('Название характеристики: '): input('Значение: ')}))

class QuestionCheck(Exception):
    pass


def value_check():
    try:
        val = int(input())
    except ValueError:
        print('Введено некорректное значение.')
        exit(0)
    else:
        return val


# Не придумал как в такой функции обрабатывать исключения, чтоб сохранить пояснение.
def add_product(goods_array, index):
    goods_array.append((index, {'Название': input('Введите название товара:'),
                                'Цена': int(input('Введите стоимость товара: ')),
                                'Кол-во': int(input('Введите кол-во товара: ')),
                                'Ед': input('Введите единицу измерения товара (шт./кг/л): ')}))


def goods_printing(goods_array):
    print('Текущий список товаров: ')
    for el in goods_array:
        print(el)


goods = list()

print('Хотите добавить товар? (1 - да, 0 - нет):')
try:
    question = value_check()
    if question != 0 and question != 1:
        raise QuestionCheck()
except QuestionCheck:
    print('Введено некорректное значение. Допустимые значения: 1/0')
    exit(0)

if question == 1:
    flag = True
    i = 1
    while flag:
        add_product(goods, i)
        print(f'Товар с идентификатором "{i}" успешно добавлен.')
        i += 1
        tmp = int(input('Хотите продолжить добавлять товары? (1 - да, 0 - нет):'))
        if tmp == 0:
            flag = False
    goods_printing(goods)

    goods_names = []
    goods_prices = []
    goods_counts = []
    goods_unit_type = []
    goods_analys = {}

    for i in range(len(goods)):
        goods_names.append(goods[i][1]['Название'])
        goods_prices.append(goods[i][1]['Цена'])
        goods_counts.append(goods[i][1]['Кол-во'])
        goods_unit_type.append(goods[i][1]['Ед'])

    goods_analys.update({'Названия': goods_names, 'Цены': goods_prices, 'Кол-ва': goods_counts, 'Ед': goods_unit_type})
    print('Аналитика товарной информации:')
    for k, v in goods_analys.items():
        print(f'{k}: ', v)

else:
    print('Сохраненные товары отсутствуют.')
