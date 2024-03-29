# """
# 1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
# осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
# info_3.txt и формирующий новый «отчетный» файл в формате CSV.
#
# Для этого:
#
# Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
# с данными, их открытие и считывание данных. В этой функции из считанных данных
# необходимо с помощью регулярных выражений извлечь значения параметров
# «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
# Значения каждого параметра поместить в соответствующий список. Должно
# получиться четыре списка — например, os_prod_list, os_name_list,
# os_code_list, os_type_list. В этой же функции создать главный список
# для хранения данных отчета — например, main_data — и поместить в него
# названия столбцов отчета в виде списка: «Изготовитель системы»,
# «Название ОС», «Код продукта», «Тип системы». Значения для этих
# столбцов также оформить в виде списка и поместить в файл main_data
# (также для каждого файла);
#
# Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
# В этой функции реализовать получение данных через вызов функции get_data(),
# а также сохранение подготовленных данных в соответствующий CSV-файл;
#
# Пример того, что должно получиться:
#
# Изготовитель системы,Название ОС,Код продукта,Тип системы
#
# 1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based
#
# 2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based
#
# 3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based
#
# Обязательно проверьте, что у вас получается примерно то же самое.
#
# ПРОШУ ВАС НЕ УДАЛЯТЬ СЛУЖЕБНЫЕ ФАЙЛЫ TXT И ИТОГОВЫЙ ФАЙЛ CSV!!!
# """


import csv
import re


def get_data(files):
    res_array = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    file_count = 1
    for i in range(len(files)):
        os_prod_list = [i + 1]
        with open(files[i], 'r') as f_obj:
            file_content = f_obj.read()
            os_prod_reg = re.compile(r'Изготовитель системы:\s*\S*')
            os_prod_list.append(os_prod_reg.findall(file_content)[0].split()[2])
            os_prod_reg2 = re.compile(r'Название ОС:\s*\S*')
            os_prod_list.append(os_prod_reg2.findall(file_content)[0].split()[2])
            os_prod_reg3 = re.compile(r'Код продукта:\s*\S*')
            os_prod_list.append(os_prod_reg3.findall(file_content)[0].split()[2])
            os_prod_reg4 = re.compile(r'Тип системы:\s*\S*')
            os_prod_list.append(os_prod_reg4.findall(file_content)[0].split()[2])
            res_array.append(os_prod_list)
    return res_array


def write_to_csv(csv_name, data):
    with open(csv_name, 'w') as csv_obj:
        csv_obj_writer = csv.writer(csv_obj, quoting=csv.QUOTE_NONNUMERIC)
        csv_obj_writer.writerows(data)


files_to_read = ['info_1.txt', 'info_2.txt', 'info_3.txt']
write_to_csv('data_report.csv', get_data(files_to_read))
with open('data_report.csv') as f_n:
    print(f_n.read())

# os_prod_reg = re.compile(r'Изготовитель системы:\s*\S*')
# os_prod_list.append(os_prod_reg.findall(data)[0].split()[2])
