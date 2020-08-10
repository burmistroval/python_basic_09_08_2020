""" Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк и сохраните в переменные,
выведите на экран.
"""

name = input('Как Вас зовут?')
age = int(input('Сколько Вам лет?'))
smokes = bool(int(input('Вы курите? 0 - нет, 1 - да')))
long_life_family = bool(int(input('Ваши родственники в целом долгожители? 0 - нет, 1 - да')))


if long_life_family == 0:
    rest_life = 80
else:
    rest_life = 90

if smokes != 0:
    rest_life = rest_life - 15

if rest_life > age:
    rest_life = rest_life - age
    print(name, ', Вам осталось жить', rest_life, 'лет')
else:
    print(name, ', Вы скоро умрёте')






