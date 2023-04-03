# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, 
# насколько легко он их придумывает, Вам стоит написать программу. 
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) 
# в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, 
# если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке 
# и “Пам парам”, если с ритмом все не в порядке

# *Пример:*
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  


def vowel_in_phrase(array, vow_arr):
    new_list = list()
    for el in array:
        count = 0
        for i in range(len(el)):
            if el[i] in vow_arr:
                count +=1
        new_list.append(count)
    return new_list


def rhythm_check(count_array):
    check_num = count_array[0]
    flag = True
    for el in count_array:
        if el != check_num:
            flag = False
    return flag


vowels = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']

poem = input('Введите стихотворение: ')
poem_parts = poem.split(' ')
print(f'Ваше стихотворение по отдельным фразам: {poem_parts}')
vowels_phrase_count = vowel_in_phrase(poem_parts, vowels)
print(f'Количество слогов в отдельных фразах: {vowels_phrase_count}')
print(f'Парам пам-пам' if rhythm_check(vowels_phrase_count) == True else 'Пам парам')
