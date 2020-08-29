"""Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""
import random
class Car:
    speed = 0
    color = 0
    name = ''
    is_police = False
    def __init__(self, color, name, is_police):
        Car.color = color
        Car.name = name
        Car.is_police = is_police
    def go(self):
        print('car goes')
    def stop(self):
        print('car stops')
    def turn(self, direction):
        print('car turns to ', direction)
    def show_speed(self):
        Car.speed = random.random()*100
        print(Car.speed)

class TownCar(Car):
    color = ''
    name = ''
    def __init__(self, color, name):
        super().__init__(color, name, False)
    def show_speed(self):
        Car.speed = random.random()*100
        print(Car.speed)
        if Car.speed > 60:
            print('Превышение скорости!')

class SportCar(Car):
    color = ''
    name = ''
    def __init__(self, color, name):
        super().__init__(color, name, False)

class WorkCar(Car):
    color = ''
    name = ''
    def __init__(self, color, name):
        super().__init__(color, name, False)
    def show_speed(self):
        Car.speed = random.random()*100
        print(Car.speed)
        if Car.speed > 40:
            print('Превышение скорости!')

class PoliceCar(Car):
    color = ''
    name = ''
    is_police = True
    def __init__(self, color, name):
        super().__init__(color, name, True)

tachka = TownCar('red', 'tachka')
tachka.go()
tachka.show_speed()

mashina = WorkCar('blue', 'mashina')
print(mashina.color)
mashina.turn('left')
mashina.show_speed()

