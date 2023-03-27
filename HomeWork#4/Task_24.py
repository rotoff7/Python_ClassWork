# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, 
# причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. 
# Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью, 
# поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.




import random

class IncorrectValue(Exception):
    pass

def value_check():
    try:
        val = int(input())
        if val < 1:
            raise IncorrectValue()
    except ValueError:
        print('Введено некорректное значение.')
        exit(0)
    except IncorrectValue:
        print('Введено некорректное значение.')
        exit(0)
    else:
         return(val)
    
def bushes_filling(hom_many):
    harvest_array = [random.randint(1, 50) for i in range(hom_many)]
    return harvest_array

def from_3_bushes_harvest(array):
    result_list = list()
    for i in range(len(array) - 1):
        result_list.append(array[i-1] + array[i] + array[i+1])
    result_list.append(array[len(array) - 2] + array[len(array) - 1] + array[0])
    return result_list

print('Введите кол-во кустов: ')
bushes_num = value_check()
bushes_array = bushes_filling(bushes_num)
print(f'Кол-во ягод на каждом кусте: {bushes_array}')
harvest_3_nums = from_3_bushes_harvest(bushes_array)
print(f'Все возможные варианты кол-ва собранных ягод за 1 заход, с каждого куста + 2 соседних: {harvest_3_nums}')
print(f'Максимально возможное кол-во собранных ягод за 1 заход: {max(harvest_3_nums)}')
