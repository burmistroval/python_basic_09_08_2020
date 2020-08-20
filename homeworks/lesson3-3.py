"""Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""
def my_min(*args):
    res = args[0]
    for itm in args:
        if itm < res:
            res = itm
    return res

def my_func(arg1, arg2, arg3):
    """Возвращает сумму наибольших двух аргументов
    :param arg1: float
    :param arg2: float
    :param arg3: float
    :return: float
    """
    min_arg = my_min(arg1, arg2, arg3)

    sum = 0

    for tmp in (arg1, arg2, arg3):
        if tmp != min_arg:
            sum += tmp
    return sum

while True:
    user_str = input('Введите 3 числа через пробелы')
    my_list = user_str.split(' ')

    try:
        my_list = map(float, my_list)
        sum = my_func(*my_list)
        print(sum)
        break
    except:
        print('Ошибка!')
