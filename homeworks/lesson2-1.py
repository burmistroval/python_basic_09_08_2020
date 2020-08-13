"""Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""

my_list = [1, 'text', True, 1, 25.5, [1, 2, 3]]

if type(my_list[0]) == int:
    print(my_list[0], ' - тип целое число')
else:
    print(my_list[0], ' - это не тип целое число!')

if type(my_list[1]) == str:
    print(my_list[1], ' - тип строка')
else:
    print(my_list[1], ' - это не тип строка!')

if type(my_list[2]) == bool:
    print(my_list[2], ' - тип булево')
else:
    print(my_list[2], ' - это не тип булево!')

if type(my_list[3]) == int:
    print(my_list[3], ' - тип целое число')
else:
    print(my_list[3], ' - это не тип целое число!')

if type(my_list[4]) == float:
    print(my_list[4], ' - тип дробное число')
else:
    print(my_list[4], ' - это не тип дробное число!')

if type(my_list[5]) == list:
    print(my_list[5], ' - тип список')
else:
    print(my_list[5], ' - это не тип список!')