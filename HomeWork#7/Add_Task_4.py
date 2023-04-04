# Задание 4.
# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), 
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

# 31 22
# 37 43
# 51 86

# 3 5 32
# 2 4 6
# -1 64 -8

# 3 5 8 3
# 8 3 7 1

# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц). 
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы 
# складываем с первым элементом первой строки второй матрицы и т.д.


class Matrix:

    def __init__(self, list_of_lists):
        self.lists_matrix = list_of_lists

    def __str__(self):
        new_string = ''
        for el in self.lists_matrix:
            for el2 in el:
                new_string += f'{el2}  '
            new_string += '\n'
        return new_string

    # # Альтернативный вариант
    # def __str__(self):
    #     new_string = ''
    #     for el in self.lists_matrix:
    #         new_string += str(el) + '\n'
    #     return new_string

    def __add__(self, other_matrix):
        if len(self.lists_matrix) != len(other_matrix.lists_matrix):
            exit('Ошибка! Размеры матриц не равны! (Разное кол-во строк.)')
        res_finish = []
        for i in range(len(self.lists_matrix)):
            if len(self.lists_matrix[i]) != len(other_matrix.lists_matrix[i]):
                exit('Ошибка! Размеры матриц не равны! (Разное кол-во столбцов.)')
            res_list = []
            for j in range(len(self.lists_matrix[i])):
                res_list.append(self.lists_matrix[i][j] + other_matrix.lists_matrix[i][j])
            res_finish.append(res_list)
        result_obj = Matrix(res_finish)
        return result_obj


array = [[3, 5, 8, 5], [8, 3, 7, 2], [4, 5, 1, 7]]
array2 = [[2, 5, 1, 2], [2, 4, 7, 5], [2, 5, 1, 9]]

first_matrix = Matrix(array)
print('Первая матрица:')
print(first_matrix)
second_matrix = Matrix(array2)
print('Вторая матрица:')
print(second_matrix)

matrix_sum = first_matrix + second_matrix
print('Сумма двух матриц:')
print(matrix_sum)
