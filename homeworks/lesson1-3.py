"""Узнайте у пользователя число n. Найдите сумму чисел
n + nn + nnn. Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369.
"""
user_number = input('Введите число')

n = user_number
nn = user_number + user_number
nnn = user_number + user_number + user_number

sum = int(n) + int(nn) + int(nnn)

print(sum)