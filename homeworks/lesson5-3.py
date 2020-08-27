"""Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

sum_salary = 0
stuff = 0

with open('text3.txt', 'r', encoding='UTF-8') as file_obj:
    for line in file_obj:
        my_list = line.split()
        salary = 0
        if my_list[1].isdigit():
            salary = int(my_list[1])
            if salary < 20000:
                print(my_list[0], 'получает меньше 20 тыс')
            sum_salary += salary
        else:
            print('Ошибка преобразования к числу')

        stuff += 1

print('Средняя зарплата ', sum_salary/stuff)