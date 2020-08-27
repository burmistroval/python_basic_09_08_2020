"""Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
str_print = ''

with open('text4.txt', 'r', encoding='UTF-8') as file_reed:
    for line_reed in file_reed:
        for en in my_dict:
            line_reed = line_reed.replace(en, my_dict[en])
        str_print = str_print + line_reed + '\t'

with open('text4-ru.txt', 'w', encoding='UTF-8') as file_write:
    print(str_print, file=file_write)
