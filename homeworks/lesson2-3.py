"""Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

while True:
    month = input('Введите номер месяца')
    if month.isdigit():
        month = int(month)
        if 0 < month < 13:
            break
        else:
            print('Это не номер месяца!')
    else:
        print('Это вообще не число!')

# решение через словарь

my_dict = {'зима': [1,2,12], 'весна': [3,4,5], 'лето': [6,7,8], 'осень': [9,10,11],}

for key, list in my_dict.items():
    for mon in list:
        if month == mon:
            print(key)

# решение через список

my_list = [[1,2,12], [3,4,5], [6,7,8], [9,10,11],]

for num, el in enumerate(my_list):
    for mon in el:
        if month == mon:
            if num == 0:
                print('зима')
            if num == 1:
                print('весна')
            if num == 2:
                print('лето')
            if num == 3:
                print('осень')