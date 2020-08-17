"""Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.
"""

def my_func(a: float, b: float):
    """Выполняет деление a на b
    При делении на 0 возвращает а
    :param a: float делимое
    :param b: float делитель
    :return: float частное
    """
    result = 0
    if b != 0:
        result = a / b
    else:
        result = a

    return result

while True:
    a = input('Введите делимое')
    if a.isdigit() == True:
        a = float(a)
        break
    else:
        print('Это не число!')

while True:
    b = input('Введите делитель')
    if b.isdigit() == True:
        b = float(b)
        break
    else:
        print('Это не число!')

print(my_func(a, b))
