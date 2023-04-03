# Задание 2.
# Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
# length (длина в метрах), width (ширина в метрах).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
# всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
# метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
# Массу и толщину сделать публичными атрибутами.
# Проверить работу метода.

# Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т


def val_check():
    try:
        val = int(input())
    except ValueError:
        exit('Введено некорректное значение.')
    else:
        return val


def road_param():
    print('Введите длину дороги:')
    user_length = val_check()
    print('Введите ширину дороги:')
    user_width = val_check()
    return user_length, user_width

# можно ли помещать параметры необходимые для конкретной функции в виде вызова в теле самой функции?
class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_of_asphalt(self):
        square_meter = int(input('Введите массу асфальта для покрытия одного метра: '))
        depth = float(input('Введите толщину покрытия в метрах (0.05): '))
        res = self._length*self._width*square_meter*depth
        return int(res / 1000)

road_length, road_width = road_param()

obj1 = Road(road_length, road_width)
print(obj1.__dict__)
print(f'Масса, необходимая для покрытия всей дороги: {obj1.mass_of_asphalt()} т')
