# Вычислить количество отрицательных чисел в массиве:

from random import randint

arr = [randint(-10, 10) for i in range(20)]
count = 0


def num_negative(lst):
    global count
    if not lst:
        return count
    if lst[0] < 0:
        count += 1
        return num_negative(lst[1:])
    else:
        return num_negative(lst[1:])


print(arr)
print("n =", num_negative(arr))
