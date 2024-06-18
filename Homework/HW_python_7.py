# Заполнить список уникальными случайными числами

import random

n = int(input("Размер списка: "))
a = []
while len(a) != n:
    i = random.randint(0, n - 1)
    if i not in a:
        a.append(i)
print(a)
