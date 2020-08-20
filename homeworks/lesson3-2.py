"""Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""
def my_zip(*args):
    idx = 0
    while True:
        result = []
        try:
            for itm in args:
                result.append(itm[idx])
        except IndexError:
            break
        yield tuple(result)
        idx += 1

def user_data(**kwargs):
    """ Получает данные пользователя и выводит на печать.
    Возвращает None
    **kwargs строковые данные пользователя. например, имя, телефон и др.
    :return: None
    """
    print('User data - ', kwargs)
    return None

data_tuple = ('name', 'surname', 'birdth_yaer', 'sity', 'email', 'phone')

data = []
for key in data_tuple:
    value = input(key)
    data.append(value)

data_zip = my_zip(data_tuple, data)

dict_param = dict(data_zip)

user_data(**dict_param)
