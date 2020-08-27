"""Создать (программно) текстовый файл,
записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open('text5.txt', 'w', encoding='UTF-8') as file_write:
    print('1 2 3 0 55 4 5 6', file=file_write)

    sum = 0

with open('text5.txt', 'r', encoding='UTF-8') as file_reed:
    for line in file_reed:
        line_list = line.split()
        try:
            line_list = map(int, line_list)
            for itm in line_list:
                sum = sum + itm
        except:
            print('Ошибка преобразования к числу')

print(sum)