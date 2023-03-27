import random

from memory_profiler import profile

# from Task_24 import *
from timeit import timeit

how_many = 7


@profile()
def bushes_filling(hom_many):
    harvest_array = [random.randint(1, 50) for i in range(hom_many)]
    return harvest_array


@profile()
def from_3_bushes_harvest(array):
    result_list = list()
    for i in range(len(array) - 1):
        result_list.append(array[i - 1] + array[i] + array[i + 1])
    result_list.append(array[len(array) - 2] + array[len(array) - 1] + array[0])
    return result_list


new_list = bushes_filling(how_many)
harvest_3_nums = from_3_bushes_harvest(new_list)

# print(timeit("from_3_bushes_harvest(new_list)", globals=globals(), number=10000))
