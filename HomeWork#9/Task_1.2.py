# 1) реализовать дескрипторы для любых двух классов


class NaturalValue:

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError('Значение параметров дороги должно быть больше нуля.')
        instance.__dict__[self.attr] = value

    def __set_name__(self, owner, attr):
        self.attr = attr


class Road:
    square_meter = 25
    depth = 0.05
    _length = NaturalValue()
    _width = NaturalValue()

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_of_asphalt(self):
        res = self._length * self._width * self.square_meter * self.depth
        return int(res / 1000)


obj1 = Road(2000, 20)
print(f'Масса асфальта, необходимая для покрытия всей дороги: {obj1.mass_of_asphalt()} т')
# obj2 = Road(-2000, 20)
