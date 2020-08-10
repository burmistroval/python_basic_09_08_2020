"""Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

user_number = int(input('Введите число до 1 000 000'))

figure = 0
max_figure = 0
position = 6
while position >= 0:
    user_number = user_number - figure*10**position
    figure = user_number// 10**(position - 1)
    if figure > max_figure:
        max_figure = figure
    position -= 1

print(max_figure)