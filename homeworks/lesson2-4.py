"""Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
"""

user_str = input('Введите несколько слов, разделенных пробелами')

my_list = user_str.split(' ')
result_list = []

for tmp in my_list:
    add_to_result = False
    for char in tmp:
        if char != ' ':
            add_to_result = True
    if add_to_result:
        result_list.append(tmp)

for num, tmp in enumerate(result_list):
    tmp_print = ''
    num_char = 0
    if len(tmp) > 10:
        while num_char < 10:
            tmp_print = tmp_print + tmp[num_char]
            num_char += 1
    else:
        tmp_print = tmp
    print(num + 1, tmp_print)