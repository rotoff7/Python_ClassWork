# 2. Задание на закрепление знаний по модулю json. Есть файл orders
# в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий
# его заполнение данными.
#
# Для этого:
# Создать функцию write_order_to_json(), в которую передается
# 5 параметров — товар (item), количество (quantity), цена (price),
# покупатель (buyer), дата (date). Функция должна предусматривать запись
# данных в виде словаря в файл orders.json. При записи данных указать
# величину отступа в 4 пробельных символа;
# Проверить работу программы через вызов функции write_order_to_json()
# с передачей в нее значений каждого параметра.
#
# ПРОШУ ВАС НЕ УДАЛЯТЬ ИСХОДНЫЙ JSON-ФАЙЛ
# ПРИМЕР ТОГО, ЧТО ДОЛЖНО ПОЛУЧИТЬСЯ
#
# {
#     "orders": []
# }
#
# вам нужно подгрузить JSON-объект
# и достучаться до списка, который и нужно пополнять
# а потом сохранять все в файл

import json


def write_order_to_json(item, quantity, price, buyer, date):
    current_dict = {'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date}
    return current_dict


def user_value():
    item_name = input('Введите название товара: ')
    quantity_count = input('Введите кол-во товара: ')
    price_size = input('Введите стоимость товара: ')
    buyer_name = input('Имя покупателя: ')
    date_order = input('Дата заказа: ')
    return item_name, quantity_count, price_size, buyer_name, date_order


with open('orders.json', 'r', encoding='utf-8') as f_n:
    dict_obj = json.load(f_n)
order_add = int(input('Нужно добавить заказ? 1 - да, 0 - нет: '))
if order_add == 1:
    orders_count = int(input('Введите кол-во заказов: '))
    for i in range(1, orders_count + 1):
        print(f'Введите данные по заказу №{i}:')
        i_n, q_c, p_s, b_n, d_o = user_value()
        dict_obj['orders'].append(write_order_to_json(i_n, q_c, p_s, b_n, d_o))
    with open('orders.json', 'w', encoding='utf-8') as f_r:
        json.dump(dict_obj, f_r, indent=4, ensure_ascii=False)
else:
    with open('orders.json', 'r', encoding='utf-8') as f_n:
        print(f_n.read())
