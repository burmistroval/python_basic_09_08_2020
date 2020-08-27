""" Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""


with open('text1.txt', 'w') as file_obj:
    end = False
    while not end:
        user_str = input('Введите строки. Для окончания введите пустую строку и нажмите Enter')
        if user_str == '':
            end = True
        else:
            print(user_str + '\t', file=file_obj)


