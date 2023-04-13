# 1) реализовать дескрипторы для любых двух классов

class ArrayOnly:

    def __set__(self, instance, value):
        if type(value) != list or type(value[0]) != list:
            raise TypeError('Матрица должна принимать массив массивов (список списков).')
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Matrix:
    lists_matrix = ArrayOnly()

    def __init__(self, list_of_lists):
        self.lists_matrix = list_of_lists

    def __str__(self):
        new_string = ''
        for el in self.lists_matrix:
            for el2 in el:
                new_string += f'{el2}  '
            new_string += '\n'
        return new_string


array_of_array = [[1, 2, 3], [3, 2, 1]]
not_array = '12321'
not_array_of_array = [1, 2, 3]
user_matrix = Matrix(array_of_array)
print(user_matrix)
# user_matrix2 = Matrix(not_array)
# user_matrix3 = Matrix(not_array_of_array)
# print(user_matrix3)
