"""Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""
class Worker:
    name = ''
    surname = ''
    position = ''
    _income = {"wage": 0, "bonus": 0}
    def __init__(self, name, surname, position, wage,bonus):
        Worker.name = name
        Worker.surname = surname
        Worker.position = position
        Worker._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage,bonus):
        super().__init__(name, surname, position, wage,bonus)

    def get_full_name(self):
        print(Position.name, Position.surname)

    def get_total_income(self):
        print(Position._income['wage'] + Position._income['bonus'])

p = Position('Misha', 'Lermontov', 'writer', 50000, 15000)
print(p.surname)
print(p._income)
p.get_full_name()
p.get_total_income()