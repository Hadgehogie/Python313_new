# Дана строка, в которой буква h встречается как минимум два раза. Разверните последовательность символов, заключенную
# между первым и последним появлением буквы h, в противоположном порядке.

import re

s = input("Введите строку: ")
reg = 'h'
lst = re.split(reg, s)
mid = []

if len(lst) == 3:
    mid = lst[1]

elif len(lst) > 3:
    mid = reg
    mid = mid.join(lst[1:-1])
else:
    print("Ошибка ввода данных - строка должна содержать минимум 2 'h'")
    s = input("Введите строку: ")

rev = []
for i in mid:
    rev.insert(0, i)

fin = ""
for x in rev:
    fin += x

print(lst[0] + reg + fin + reg + lst[-1])
