""" Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open('text2', 'r', encoding='UTF-8') as file_obj:
    lines = 0
    for line in file_obj:
        lines += 1
        list_words = line.split(' ')
        print('В строке ', lines, ' слов: ', len(list_words))

print('Всего строк ', lines)

