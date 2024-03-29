# Задание 3.
# Реализовать базовый класс Worker (работник),
# в котором определить публичные атрибуты name, surname, position (должность),
# и защищенный атрибут income (доход). Последний атрибут должен ссылаться
# на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
#
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
# получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
#
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).
#
# П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку str
# str(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.


class Worker:

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname}. Должность: {self.position}')

    def get_total_income(self):
        res = sum(self._income.values())
        print(f'Доход на должности {self.position} составляет: {res}')

    def __str__(self):
        return f'{self.name} {self.surname}. Должность: {self.position}.'


worker_income = {'wage': 30000, 'bonus': 15000}

obj1 = Position('Джим', 'Рейнор', 'Шериф', worker_income)
obj1.get_full_name()
obj1.get_total_income()
print(obj1.__dict__)

obj2 = Position('Сара', 'Керриган', 'Королева', {'wage': 100000, 'bonus': 50000})
obj2.get_full_name()
obj2.get_total_income()
print(obj1)
