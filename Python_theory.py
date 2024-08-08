# -----------------------------------------------------
# Введение
# import random
# import random
# name = "Alina"  # Инициация переменной
# print("Hello,", name)
# age = 17
# print(age)
# text = "Hello"
# print(text)
# print(text + str(age))  # Не работает неявное приведение данных => Python - язык с сильным типом типизации данных
# print(type(age))  # int - 17
# num = 20.4
# print(type(num))  # float - 20.4
# print(type(text))  # str - "Hello"
# a = True
# print(type(a))  # bool - True, False
# import re
# import re
# import Geometry


# a = 4
# b = 5
# print(a, id(a))
# print(b, id(b))
# a = b
# print(a, id(a))
# print(b, id(b))

# a = b = c = 1
# print(a)
# print(b)
# print(c)

# a, b, c = 5, "Hello", 9.2
# print(a)
# print(b)
# print(c)

# Name = "Igor"
# name6 = "Igor"
# name_new = "Igor"
# ____name6 = "Igor"
# # 6name = "Igor"
# # name-one = "Igor"
# # name$ = "Igor"

# PI = 3.14
# print(PI)
# PI = 2
# print(PI)

# a = 1
# b = 2
# print("a:", a)
# print("b:", b)
# # c = a  # 1
# # a = b  # 2
# # b = c  # 1
# a, b = b, a
# print("a:", a)
# print("b:", b)

# print("line of symbols")
# print('line of symbols')
# print("line of \
# symbols")
# print("line of "
#       "symbols")
# print('line \nof symbols \'file.txt\'')
# print('line \nof symbols \rfile.txt')
# print('line of symbols D:\\folder\\file.txt')
# print('\t line \n       of symbols D:\\folder\\file.txt')

# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + ", " + s2 + "!\t\t"
# # print(s1, ",", s2, "!")
# print(s3 * 3)

# print(12375623745613501873598137457365703451607382)
# print(1.2375623745613501873598137457365703451607382)

# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(6 / 2)  # 3.0
# print(6 / 4)  # 1.5
# print(6 // 2)  # 3 - целочисленное деление
# print(6 // 4)  # 1 - целочисленное деление
# print(6 ** 2)
# print(6 % 4)  # 2 - остаток от деления


# -----------------------------------------------------
# Действия с операторами и преобразование данных

# number = (6 + 4) * (5 ** 2 + 7)
# print(number)  # 113

# num = 10
# num += 5
# print(num)
#
# num -= 3
# print(num)

# num = 6375
# print("Исходное число:", num)
# a = (num // 1000)  # 6
# b = num // 100 % 10  # 3
# c = num // 10 % 10  # 7
# d = num % 10  # 5
# print("Результат:", d * 1000 + c * 100 + b * 10 + a)

# num = 4325
# print("Исходное число:", num)
# a = num % 10
# print(a)  # 5
# num //= 10
# # print(num)  # 432
# b = num % 10
# print(b)  # 2
# num //= 10
# # print(num)  # 43
# c = num % 10
# print(c)  # 3
# num //= 10
# # print(num)  # 4
# d = num % 10
# print(d)  # 4
# print(a * 1000 + b * 100 + c * 10 + d)

# num = 4325
# print("Исходное число:", num)
# res = num % 10 * 1000
# num //= 10
# res += num % 10 * 100
# num //= 10
# res += num % 10 * 10
# num //= 10
# res += num % 10
# print(res)

# num1 = "2"
# num2 = 3
# res1 = num1 + str(num2)  # 23
# res2 = int(num1) + num2  # 5
# print(res1)
# print(res2)

# print(int(-3.8))  # -3
# print(round(3.891, 2))  # 3.89
# print(type(round(3.891, 2)))  # float

# num1 = "2.3"
# num2 = 3
# # res = int(num1) + num2
# res = float(num1) + num2
# print(res)

# name = "Victor"
# age = 27
# print("My name is " + name + ". I'm " + str(age) + " years old.")
# print("My name is", name, ". I'm", age, "years old.", sep='---', end='  --//--  ')
# print("I learn Python.")

# name = input("Name: ")
# print(name)

# num = input("Введите число: ")
# power = input("Введите степень: ")
# res = int(num) ** int(power)
# # print("Число", num, "в степени", power, "равно", res)

# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))
# print("Число", num, "в степени", power, "равно", num ** power)
# print(type(num))  # int

# b1 = True
# b2 = False
# print(b1 + 5)  # True => 1, " ", "x", True
# print(b2 + 5)  # False => 0, "", False, None

# print(bool("python"))  # True
# print(bool(""))  # False
# print(bool(" "))  # True
# print(bool(-0.2))  # True
# print(bool(0))  # False
# print(bool(False))  # False
# print(bool(None))  # False
# test = None
# print(test)

# print(7 == "7")  # False
# print(7 == 7)  # True
# print(2 + 5 == 7)  # True
# print(7 != 10 - 7)  # True
# print(8 <= 5)  # False
# print("hello" > "HELLO")  # True

# print(2 < 4 < 9)  # 2 < 4 < 8 => True && True => True
# print(2 * 5 > 7 >= 4 + 3)  # True && True => True
# print(3 * 3 <= 7 >= 2)  # False && True => False

# a = 10
# b = 5
# c = a == b
# print(a, b, c)  # 10 5 False

# print(5 - 3 == 2 and 1 + 3 == 4)  # True (True:True)
# print(5 - 3 == 2 and 1 + 3 < 4)  # False (True:False)
# print(5 - 3 > 2 and 1 + 3 == 4)  # False (False:True)
# print(5 - 3 > 2 and 1 + 3 < 4)  # False (False:False)

# print(5 - 3 == 2 or 1 + 3 == 4)  # True (True:True)
# print(5 - 3 == 2 or 1 + 3 < 4)  # True (True:False)
# print(5 - 3 > 2 or 1 + 3 == 4)  # True (False:True)
# print(5 - 3 > 2 or 1 + 3 < 4)  # False (False:False)

# print(9 - 7)  # 2
# print(not 9 - 7)  # False
# print(not 7 - 7)  # True

# cnt = 5
# if cnt < 10:
#     cnt += 2
#     print(cnt)

# age = int(input("Insert your age, please: "))
# if age >= 18:
#     print("Access allowed")
# else:
#     print("Access denied")

# a = 25
# b = 15
# if a > b:
#     print("a > b")
# elif a < b:
#     print("a < b")
# else:
#     print("a = b")

# a = input("Введите первую сторону: ")
# b = input("Введите вторую сторону: ")
# c = input("Введите третью сторону: ")
# if a == b == c:
#     print("Треугольник равносторонний")
# elif (a == b) or (a == c) or (b == c):
#     print("Треугольник равнобедренный")
# else:
#     print("Треугольник разносторонний")

# day = int(input("Insert the weekday (using numbers): "))
# if 1 <= day <= 5:
#     print("Working day - ", end="")
#     if day == 1:
#         print("Monday")
#     if day == 2:
#         print("Tuesday")
#     if day == 3:
#         print("Wednesday")
#     if day == 4:
#         print("Thursday")
#     if day == 5:
#         print("Friday")
# elif day == 6 or day == 7:
#     print("Weekend - ", end="")
#     if day == 6:
#         print("Saturday")
#     if day == 7:
#         print("Sunday")
# else:
#     print("There isn't such a weekday")

# -----------------------------------------------------
# Тернарные выражения + Исключения

# a = int(input("Введите количество ворон: "))
# if 0 <= a <= 9:
#     print("На ветке", a, end=" ")
#     if a == 1:
#         print("ворона")
#     elif 2 <= a <= 4:
#         print("вороны")
#     else:
#         print("ворон")
# else:
#     print("Ошибка ввода данных")

# password = "me"
#
# match password:
#     case 'admin':
#         print("Администратор")
#     case "user":
#         print("Пользователь")
#     case _:
#         print("Логин не найден")

# day = 'Friday'
# time = 14
#
# match day:
#     case 'Monday' | 'Tuesday' | 'Wednesday' | 'Thursday' | 'Friday' if 9 <= time <= 13 or 15 <= time <= 16:
#         print('Working day')
#     case 'Saturday' | 'Sunday':
#         print('Weekend')
#     case _:
#         print("There isn't such a weekday/non-working time")

# a, b = 20, 30
# print('a == b' if a == b else 'a > b' if a > b else "b > a")

# a, b = 10, 0
# print("На нуль делить нельзя" if b == 0 else a / b)
# print(a / b)

# try:
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except ValueError:
#     print("Something's gone wrong")
#
# print("Next line")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("Нельзя вводить строки")
# except ZeroDivisionError:
#     print("Нельзя делить на ноль")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Нельзя вводить строки или нельзя делить на ноль")
# else:  # Когда в блоке try не возникло исключения
#     print("Все нормально, вы ввели числа", m, "и", n)
# finally:  # Выполнится в любом случае
#     print("Конец программы")

# a = input("Insert the first number: ")
# b = input("Insert the second number: ")
# try:
#     print(int(a) + int(b))
# except ValueError:
#     print(str(a) + str(b))

# a = input("Insert the first number: ")
# b = input("Insert the second number: ")
# try:
#     a = int(a)  # a = 5
#     b = int(b)  # b = 'six'
# except ValueError:
#     a = str(a)  # a = '5'
# finally:
#     print(a + b)


# -----------------------------------------------------
# Циклы
# While

# i = 0
# while i < 20:
#     print("i =", i)
#     i += 1

# i = 10
# while i > 0:
#     print("i =", i)
#     i -= 1

# i = 2
# while i <= 20:
#     print("i =", i)
#     i += 2

# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print("i =", i)
#     i += 1

# a = int(input("Укажите количество символов: "))
# i = 0
# while i < a:
#     print("*", end='\n')
#     i += 1

# a = int(input("Введите начало диапазона: "))
# b = int(input("Введите конец диапазона: "))
# res = 0
# while a <= b:
#     if a % 2:  # a % 2 != 0 => True
#         res += a
#         print("a =", a)
#     a += 1
# print("Сумма целых нечетных чисел:", res)


# -----------------------------------------------------
# Циклы 2
# While

# n = input("Insert a number: ")
#
# while type(n) is not int and type(n) is not float:
#     try:
#         n = int(n)
#
#     except ValueError:
#         try:
#             n = float(n)
#         except ValueError:
#             print("That's not an integer nor real number")
#             print(type(n))
#             n = input("Insert an integer number: ")
#
# if n % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=' ')
#     if i == 5:
#         break
#     i += 1
# print("\nThe cycle is finished")

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# while True:
#     a = int(input("Insert a positive number: "))
#     if a < 0:
#         break

# res = 1
# while True:
#     a = int(input("insert an integer number: "))
#     if a == 0:
#         break
#     res *= a
# print("Result:", res)

# i = 0
# while i < 10:
#     if i == 5:
#         i += 1
#         continue
#     print(i, end=' ')
#     i += 1
# else:
#     print("\nThe cycle is finished, i =", i)

# i = 1
# while i < 5:
#     print("The outer cycle: i =", i)
#     j = 1
#     while j < 4:
#         print("\tThe inner cycle: j =", j)
#         j += 1
#     i += 1

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end='\t\t')
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 3:
#     j = 0
#     while j < 6:
#         print("^", end='')
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if i % 2:
#             print("-", end='')
#         else:
#             print("+", end='')
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if j % 2:
#             print("-", end='')
#         else:
#             print("+", end='')
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < i:
#         print(" ", end='')
#         j += 1
#     print("*")
#     i += 1

# i = 0
# while i < 5:
#     print(" " * i, "*")
#     i += 1


# -----------------------------------------------------
# Циклы 2
# For

# for element in collection:
#      print(element)
# for element in range(n):
#      print(element)

# for i in "Hello", "World", "!":
#     print(i)

# print(list(range(5)))

# for i in range(0, 9 + 1):  # range(start, stop, step)
#     print(i, end=' ')
# print()
#
# i = 0
# while i <= 9:
#     print(i, end=' ')
#     i += 1

# a = int(input("Insert a number: "))
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=' ')

# for i in range (10, 101):
#     if i % 11 == 0:
#         print(i, end=' ')

# for i in range (10, 100):
#     if i % 10 == i // 10:
#         print(i, end=' ')


# -----------------------------------------------------
# Циклы 2
# For

# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print("done")

# for i in range(3):
#     print("+++ i =", i)
#     for j in range (2):
#         print("----- j =", j)

# a = int(input("Введите длину прямоугольника: "))
# b = int(input("Введите высоту прямоугольника: "))
#
# for i in range(b):
#     for j in range(a):
#         print("*", end='')
#     print()

# a = int(input("Введите ширину прямоугольника: "))
# b = int(input("Введите высоту прямоугольника: "))
#
# for i in range(b):
#     for j in range(a):
#         if i == 0 or i == (b - 1) or j == 0 or j == a - 1:
#             print("*", end='')
#         else:
#             print(' ', end='')
#     print()


# -----------------------------------------------------
# Список (list)
# [Выражение for переменная in последовательность]

# nums = [letter * 2 for letter in "Banana"]
# print(nums)

# nums = [i for i in range(30) if i % 2 == 0]
# print(nums)

# nums = [8, 3, 9, 11, 23, 'one']
# print(nums)
# print(type(nums))
# print(nums[0])
# print(nums[2])
# # print(nums[6])  # IndexError: list index out of range
# print(nums[-1])  # nums[5]
# nums[1] = 256
# print(nums)
# nums[3] += 100
# print(nums)
# print(len(nums))  # Длина списка
# for i in range(len(nums)):
#     print(nums[i] * 2)  # Каждое из значений списка умножается на 2

# s = []  # Пустой список
# print(s)
#
# b = list()  # Тоже пустой список
# print(b)

# b = list("Hello")
# print(b)
# print(b[0])

# print(range(6))
# n = list(range(6))
# print(n)

# print(list(range(2, 10)))
# print(list(range(2, 10 + 1, 2)))

# a = [0 for _ in range(5)]  # Генератор списка
# print(a)
# b = [i for i in range(5)]
# print(b)

# n = 5
# b = [i ** 2 for i in range(1, n + 1)]
# print(b)

# a, b = [1, 2], [3, 4, 5]
# c = a + b
# print(c)
# d = b * 3
# print(d)

# a = [0] * int(input("Введите количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)

# a = [input("-> ") for i in range(int(input("Введите количество элементов списка: ")))]
# print(a)

# a = [int(input("-> ")) for i in range(int(input("Введите количество элементов списка: ")))]
# res = 0
# for i in range(len(a)):
#     if a[i] < 0:
#         res += a[i]
# print("Сумма отрицательных элементов:", res)

# a = [int(input("-> ")) for i in range(int(input("Введите количество элементов списка: ")))]
# res = 0
# for i in a:
#     if i < 0:
#         res += i
# print("Сумма отрицательных элементов:", res)

# a = list(range(10, 100, 10))
# print(a)
# for i in range(len(a)):
#     print(a[i], end=' ')
# print()
# for i in a:
#     print(i, end=' ')

# a = list(range(21, 41))
# print("Список: ", a)
# odd = even = 0
# for i in a:
#     if i % 2:
#         odd += i
#     else:
#         even += 1
# print("Количество четных элементов списка: ", even)
# print("Сумма нечетных элементов списка: ", odd)

# a = [(int(input("-> "))) for i in range(int(input("Введите элементы списка: \nn = ")))]
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=' ')


# -----------------------------------------------------
# Срез (часть списка)
# Список[start:stop:step]

# a = [7, 8, 2, 1, 17, 9]
# print(a)
# # a[0], a[1] = a[1], a[0]
# # print(a)
# print(a[1:4])
# print(a[1:])
# print(a[:1])
# print(a[:])
# print(a[::2])
# print(a[5:0:-1])  # в этом случае 0 выкалывается
# print(a[0:5:-1])  # []
# # print(a[10])  # IndexError
# print(a[10:20])  # []

# a = list(range(1, 8))
# print(a)
# print(a[::-1])
# print(a[::2])
# print(a[1::2])
# print(a[:1])
# print(a[6:])  # -1
# print(a[3:4])
# print(a[4:])  # -3
# print(a[4:1:-1])
# print(a[2:5])

# s = [5, 9, 3, 7, 1, 8]
# print(s)
# s[1:3] = [0, 0, 0, 0]
# print(s)
# # s[1:2] = 20  # TypeError
# s[1:2] = [20]
# print(s)
# s[1] = [20]
# print(s)
# s[2:5] = []
# print(s)
# del s[1:2]
# print(s)


# -----------------------------------------------------
# Методы списков

# s = [5, 9, 3, 7, 1, 8]
# print(s)
# s.append(99)  # добавляет 1 элемент в конец списка
# print(s)
# s.extend([1, 2, 3])  # добавляет список в конец списка
# print(s)
# s.extend('add')   # добавляет строку в конец списка
# print(s)
# s.insert(2, 100)  # добавляет элемент в заданный индекс списка
# print(s)
# s.insert(-1, 200)
# print(s)
# s.insert(20, 200)
# print(s)

# s = []
# n = int(input("Количество элементов в списке: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     # s.append(x)
#     s.insert(0, x)
# print(s)

# s = []
# n = int(input("Количество элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число, кратное 3: "))
#     if x % 3:
#         print(x, "не делится на 3 без остатка.")
#     else:
#         s.append(x)
# print(s)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break  # Ускоряет код, т.к. лишние значения не проверяются после найденного совпадения
# print(c)  # [2, 1, 4, 3]

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
#
# for element in a:
#     if element not in c and element in b:
#         c.append(element)
# print(c)

# a = [1, 2, 3, 4, 5, 6]
# b = [11, 22, 33, 44]
# c = []
# if len(a) <= len(b):
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
# print(c)

# s = [5, 9, 3, 7, 9, 1, 8, 9]
# print(s)
# s.remove(9)  # Удаляет первый элемент списка по значению
# # print(s.remove(9))  # None
# print(s)
# s.remove(9)
# s.remove(9)
# print(s)
# s.pop()  # Удаляет последний элемент из списка (без параметров)
# print(s)
# print(s.pop(1))  # Удаляет выбранный по индексу элемент списка, может его вернуть
# print(s)
# s.clear()  # Очистка всех элементов списка
# print(s)

# a = [(int(input("-> "))) for i in range(int(input("Введите элементы списка: \nn = ")))]
# k = int(input("Введите индекс: \nk = "))
# a.pop(k)
# print(a)

# s = [5, 9, 3, 7, 9, 1, 8, 9]
# print(s)
# print(s.count(9))  # Считает количество определенных элементов в списке (по значению)
# ind = s.index(9)  # Возвращает индекс первого искомого элемента
# print(ind)
# ind = s.index(9, 2)
# print(ind)
# ind = s.index(9, 5, -1)  # ValueError
# print(ind)

# a = [1, 2, 3]
# b = a.copy()  # Теперь переменные ссылаются на разные области в памяти
# print("a =", b)
# print("b =", b)
# a.append(20)
# print("a =", b)
# print("b =", b)
# b.append(120)
# print("a =", b)
# print("b =", b)

# a = [5, 4, 1, 2, 3]
# print(a)
# a.reverse()  # разворачивает элементы списка
# print(a)
# print(a.reverse())  # None

# a = [5, 4, 1, 2, 3]
# print(a)
# a.sort()  # Элементы расположены по возрастанию
# print(a)
# a.sort(reverse=False)  # Сортировка в порядке возрастания
# print(a)
# a.sort(reverse=True)  # Сортировка в порядке убывания
# print(a)

# b = ['Виталий', 'Сергей', 'Александр', 'Анна']
# b.sort()
# print(b)  # Имена в алфавитном порядке
# b.sort(key=len, reverse=True)
# print(b)  # Имена по длине в порядке убывания

# a = [5, 4, 1, 2, 3]
# print(a)
# sort = sorted(a)
# print(sort)  # Не изменяет изначальный список
# a.sort()
# print(a)


# -----------------------------------------------------
# Генерация случайных данных

# import random

# print(random.random())  # случайное число (0;1)
# print(random.randint(0, 9))  # случайное число [0;9]
# # print(random.randint(3, 9.2))  # ValueError
# # print(random.randint(3))  # TypeError
# print(random.randrange(9))  # случайное число [0;9)
# print(random.randrange(3, 9, 2))  # случайное число [3;9) с шагом 2
#
# print(random.uniform(10.5, 25.0))
# print(round(random.uniform(10.5, 25.5), 2))  # Округление до заданного знака после запятой

# city_list = ['Москва', 'Новосибирск', 'Воронеж', 'Сочи', 'Екатеринбург']
# print(random.choice(city_list))
# print(random.choices(city_list, k=3))
# random.shuffle(city_list)  # Список перемешивается
# print(city_list)

# s = [55, 66, 77, 88, 99, 9, 8, 7, 6, 5, 4, 1, 2, 3]
# print(random.choice(s))
# print(random.choices(s, k=5))

# lst = [5, 4, 3, 2, 1]
# # lst = ['5', '4', '3', '2', '1']  # Идет сложение 0 + '5' => TypeError
# print(len(lst))
# print(sum(lst))  # Дает ошибку при использовании строк
# print(min(lst))
# print(max(lst))

# sum = 5
# print(sum)
# s = [55, 66, 77, 88, 99, 9, 8, 7, 6, 5, 4, 1, 2, 3]
# print(sum(s))  # TypeError, функция превращается в переменную

# import random
# lst = [random.randint(10, 99) for i in range(10)]
# print(lst)
# max_ = max(lst)
# print("Max:", max_)
# lst.remove(max_)
# lst.insert(0, max_)
# print(lst)

# import random
# mas = [random.randint(10, 99) for i in range(10)]
# print(mas)
# min_ = min(mas)
# print('Min:', min_)
# print('Index min:', mas.index(min_))
# # for i in range(len(mas)):
# #     while i < mas.index(min_):
# #         mas.pop(i)
# #         # mas.insert(i - 1, 0)
#
# # del mas[0: mas.index(min_)]
# # print(mas)
#
# print(mas[mas.index(min_):])

# x = list('1a2b3c4d')
# print(x)
# print('a' in x)  # True
# print('f' in x)  # False
#
# print('a' not in x)  # False
# print('f' not in x)  # True

# lst = [1, 2, 3]
# if len(lst) == 0:
#     print("The list is empty")
# else:
#     print("There are elements in the list")

# lst = []
# print(bool(lst))  # [] => False, [x] => True
# if not lst:
#     print("The list is empty")
# else:
#     print("There are elements in the list")

# import random
#
# lst1 = [random.randint(0, 10) for i in range(int(input("Введите размер первого списка: ")))]
# lst2 = [random.randint(0, 10) for j in range(int(input("Введите размер второго списка: ")))]
# print("Первый список:", lst1)
# print("Второй список:", lst2)
#
# # lst1.extend(lst2)
# # print("Третий список:", lst1)
# lst3 = lst1 + lst2
# print("Третий список:", lst3)
#
# no_reps = []
# reps = []
# for i in lst1:
#     if i not in no_reps:
#         no_reps.append(i)
#     if i in lst1 and i in lst2 and i not in reps:
#         reps.append(i)
#         no_reps.remove(i)
# for j in lst2:
#     if j not in no_reps:
#         no_reps.append(j)
# print("Элементы обоих списков без повторений", no_reps)
# print("Элементы, общие для двух списков:", reps)
#
# lst1_min = min(lst1)
# lst1_max = max(lst1)
# lst2_min = min(lst2)
# lst2_max = max(lst2)
# print("Минимальное и максимальное значения каждого из списков", [lst1_min, lst1_max, lst2_min, lst2_max])

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# # m = ['Hello', 'World']
# print(m)
# # print(len(m))  # 3
# # print(m[1][2])  # 7/r (строка - итерируемый объект)
# print()
# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end='\t')
#     print()

# w, h = 4, 3
# # matrix = [[0 for x in range(w)] for y in range(h)]
# matrix = []
# for y in range(h):
#     new_row = []
#     for x in range(w):
#         new_row.append(0)
#     matrix.append(new_row)
# print(matrix)
#
# for row in matrix:
#     for x in row:
#         print(x, end='\t')
#     print()

# import random
#
# w, h = 4, 3
# matrix = [[random.randint(1, 30) for x in range(w)] for y in range(h)]
#
# for row in matrix:
#     for x in row:
#         print(x, end='\t')
#     print()

# import random
#
# matrix = [[random.randint(-20, 10) for x in range(4)] for y in range(3)]
#
# res = 0
# for row in matrix:
#     for x in row:
#         print(x, end='\t\t')
#         if x < 0:
#             res += 1
#     print()
#
# print("Количество отрицательных элементов: ", res)

# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, '+', y, '=', x + y)

# w, h = 4, 3
# matrix = [[int(input("-> ")) for x in range(w)] for y in range(h)]
#
# for row in matrix:
#     for x in row:
#         print(x, end='\t')
#     print()


# -----------------------------------------------------
# Математические операции
# import Geometry

# import Geometry
#
# num1 = Geometry.sqrt(121)  # 11.0
# num2 = Geometry.ceil(3.1)  # Округление в верхнюю сторону
# num3 = Geometry.floor(3.8)  # Округление в нижнюю сторону
#
# print(num1)
# print(num2)
# print(num3)
# print(Geometry.pi)

# import Geometry as m  # from Geometry import *
# from Geometry import sqrt, ceil
#
# num1 = sqrt(4)
# num2 = ceil(3.1)
#
# print(num1)
# print(num2)

# import time
# import locale
#
# locale.setlocale(locale.LC_ALL, 'ru')
#
# seconds = time.time()
# print('Кол-во секунд с начала цифровой эпохи', seconds)  # 1 January 1970
#
# locale_time = time.ctime()  # time.ctime(seconds)
# ran_time = time.ctime(1454691600)
# print('Местное время: ', locale_time)
# print('Важная дата: ', ran_time)
#
# res = time.localtime()
# print(res)
# print(res.tm_mday, '.', res.tm_mon, '.', res.tm_year, sep='')
#
# print(time.strftime("Today is %B %d, %Y"))
#
# print(time.strftime("%d/%m/%Y, %H:%M:%S"))
# print(time.strftime("%d/%m/%Y, %H:%M:%S", time.localtime(1454691600)))
#
# print(time.strftime("Сегодня %B %d, %Y"))

# import time
#
# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# res = finish - start
# print(res)  # 5.0


# -----------------------------------------------------
# Функция (Function)

# print()
#
#
# def hello(name):
#     print("Hello,", name)
#
#
# hello("Irina")
# hello("Igor")


# def get_sum(a, b):  # Конфликт областей видимости
#     print(a + b)
#
#
# a = 2
# b = 5
# get_sum(a, b)
# get_sum("abc", "def")


# def line(a, b, n):
#     # pass / ...
#     for i in range(n):
#         if i % 2 == 0:
#             print(a, end='')
#         else:
#             print(b, end='')
#     print()
#
#
# line("+", "-", 9)
# line("X", "0", 9)


# def get_sum(a, b):  # Конфликт областей видимости
#     print("Summ:", end=' ')
#     return a + b  # Прерывает выполнение функции
#
#
# x = 2
# y = 5
# res = get_sum(x, y)
# print(res)


# def maximum(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
#
# print(maximum(9, 36))


# def func(a, b):
#     if a > b:
#         return a - b
#     elif a < b:
#         return a + b
#
#
# one = int(input("Insert the 1-st number: "))
# two = int(input("Insert the 2-nd number: "))
# print("Result:", func(one, two))


# def cube(a):
#     return a ** 3
#
#
# for i in range(1, 11):
#     print(i, 'в кубе =', cube(i))

# mas1 = [1, 2, 3]
# mas2 = [9, 12, 33, 54, 105]
# mas3 = ["с", "л", "о", "н"]
# print("Исходные данные:", mas1, mas2, mas3, sep='\n')
#
#
# def change(lst):
#     # last = lst.pop()
#     # first = lst.pop(0)
#     # lst.insert(0, last)
#     # lst.append(first)
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst
#
#
# print("Результат:", change(mas1), change(mas2), change(mas3), sep='\n')


# def is_greater(x, y):
#     if x > y:
#         return True  # x => True
#     else:
#         return False  # y => True
#
#
# a = 10
# b = 15
# print(is_greater(a, b))
# print(is_greater(5, 10))
#
# if is_greater(a, b):
#     print(a, "is greater than", b)
# else:
#     print(b, "is greater than", a)

# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         elif 'a' <= ch <= 'z':
#             has_lower = True
#         elif '0' <= ch <= '9':
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input("Insert password: ")
# if check_password(p):
#     print("The password is secure")
# else:
#     print("The password is non-secure")


# -----------------------------------------------------
# Типы аргументов функций

# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))  # TypeError, d=1 => ok
# print(get_sum(1, 5))
# print(get_sum(1, 5, d=2))

# def set_param(c=20, s='-'):
#     return s * c
#
#
# print(set_param(10, '+'))
# print(set_param(5, '*'))
# print(set_param(s='#'))
# print(set_param(7))
# print(set_param())

# def digit_sum(a, even=True):
#     s = 0
#     while a > 0:
#         current = a % 10
#         if even and current % 2 == 0:
#             s += current
#         if not even and current % 2:
#             s += current
#         a //= 10
#     return s
#
#
# print("Сумма четных цифр:")
# print(digit_sum(9874023))
# print(digit_sum(38271))
# print(digit_sum(123456789))
# print("\nСумма нечетных цифр:")
# print(digit_sum(9874023, even=False))
# print(digit_sum(38271,  even=False))
# print(digit_sum(123456789,  even=False))

# def display_info(name, age):
#     print("Name:", name, "\nAge:", age)
#
#
# display_info("Ira", 23)
# display_info(23, "Ira")
# display_info(age=23, name="Ira")
# display_info("Igor", age=23, name="Ira")  # TypeError


# -----------------------------------------------------
# Изменяемые и неизменяемые объекты
# Изменяемые типы данных: list
# Неизменяемые типы данных: str, int, tuple (кортеж)

# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(id(lt1))
# print(id(lt2))
# print(lt1 == lt2)  # True
# print(lt1 is lt2)  # False

# a = "Hello"
# b = "Hello"
# print(id(a))
# print(id(b))
# print(a == b)  # True
# print(a is b)  # True

# n = 5
# m = 5
# print(id(n))
# print(id(m))
# print(n == m)  # True
# print(n is m)  # True

# n = 5
# print(id(n))  # 140706800912952
# n = 6
# print(id(n))  # 140706800912984

# n = 'Hello'
# print(id(n))  # 1925552700176
# n = 'Python'
# print(id(n))  # 140706799801120

# n = [1, 2, 3]
# print(id(n))  # 1744319926528
# n.append(4)
# print(n)
# print(id(n))  # 1744319926528


# -----------------------------------------------------
# Кортеж (tuple) - неизменяемый список

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())  # 72 / 104
# print(tpl.__sizeof__())  # 48

# a = 5, 9, 7, 8  # (5, 9, 7, 8) / 5,
# # b = tuple()
# print(type(a))  # tuple
# # print(type(b))
# print(a)
# # print(b)

# n = [1, 2, 3]
# # b = tuple("Hello")
# b = tuple(("Hello", "Python"))
# print(type(b))
# print(b)

# n = ['Hello', 'Python']
# b = tuple(n)
# print(type(b))
# print(b)

# a = (1, 2, 3, 4, 5, 6)
# print(a)
# print(a[3])  # 4
# print(a[1:3])  # (2, 3)
# # a[1] = 3  # TypeError (кортежи нельзя изменять)

# s = [i for i in range(5)]
# print(s)  # [0, 1, 2, 3, 4]

# k = (i for i in range(5))
# print(k)  # <generator object <genexpr> at 0x000001C8C2254B80>

# k1 = tuple(i for i in range(5))
# print(k1)  # (0, 1, 2, 3, 4)

# k2 = tuple(int(input("-> ")) for i in range(int(input("n = "))))
# print(k2)

# from random import randint
#
# k3 = tuple(randint(0, 100) for i in range(5))
# print(k3)  # (0, 1, 2, 3, 4)

# a = tuple(2 ** i for i in range(1, 13))
# print(a)

# t1 = tuple("hello")
# t2 = tuple("world")
# print(t1)
# print(t2)
# t3 = t1 + t2
# print(t3)
# # print(t1 * 2)
#
# # print(t3.count("l"))  # 3
# # if 'e' in t3:
# #     print(t3.index('e'))  # 1
#
# for i in t3:
#     print(i, end=' ')

# def slicer(tpl, n):
#     if tpl.count(n) == 0:
#         return ()
#     if tpl.count(n) == 1:
#         return tpl[tpl.index(n):]
#     if tpl.count(n) > 1:
#         ind1 = tpl.index(n)
#         ind2 = tpl.index(n, ind1 + 1)
#         return tpl[ind1:ind2 + 1]
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# t = (10, 11, [1, 2, 3], [4, 5, 6], ['hello', 'world'])
# print(t, id(t))  # 1527482904272
# t[4][0] = 'new'
# print(t, id(t))  # 1527482904272
# t[4].append('hi')
# print(t, id(t))  # 1527482904272

# t = (1, 2, 3)
# x, y, z = t  # Распаковка кортежа
# print(x, y, z)  # 1 2 3

# def get_user():
#     name = 'Tom'
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# user = get_user()
# first_name, year, married = user
# # print(user)  # ('Tom', 22, False)
# # print(user[0])  # Tom
# print(first_name, year, married)  # Tom 22 False

# tpl = (1, 2, 3, 4, 5, 6)
# print(tpl)  # (1, 2, 3, 4, 5, 6)
# lst = list(tpl)
# print(lst)  # [1, 2, 3, 4, 5, 6]
# ptl1 = tuple(lst)
# print(ptl1)  # (1, 2, 3, 4, 5, 6)
# del ptl1  # Кортеж перестает существовать
# # print(ptl1)  # NameError

# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# )
# print(countries, end='\n\n')
#
# for country in countries:
#     # print(country)
#     country_name, country_population, cities = country
#     print("\nСтрана:", country_name, "население =", country_population)
#     for city in cities:
#         city_name, city_population = city
#         print("\tГород:", city_name, "население =", city_population)

# print("Some random changes")

# print("Cloned repository")


# -----------------------------------------------------
# Множества (set)
# Значения не упорядочены, дубликаты не выводятся, нет индексов или ключей

# s = {'banana', 'apple', 'orange', 'banana', 'apple'}
# print(s)  # {'orange', 'banana', 'apple'}
# print(s[0])  # TypeError: 'set' object is not subscriptable
# print(type(s))
# print(len(s))  # 3

# a = {}
# b = set('hello')
# print(a, type(a))  # {} <class 'dict'>
# print(b, type(b))  # {'l', 'h', 'e', 'o'} <class 'set'>

# c = ['red', 'blue', 'green', 'red']
# a = set(c)
# print(a, type(a))

# mas = [1, 2, 3, 2, 3, 4, 4, 5]
# s = {x for x in mas if x % 2 == 0}
# print(s)

# def to_set(a):
#     b = set(a)
#     return b, len(b)
#
#
# print(to_set('я обычная строка'))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))

# t = {'red', 'green', 'blue'}
# # print('green' in t)  # True
# for i in t:
#     print(i)

# r = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# # a = [i for i in r if 'a' not in i]
# # a = ['A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r]
# a = ['A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r if i[1] == 'c']
# print(a)

# a = {'Tom', 'Bob', 'Alice'}
# print(a)
# a.add('Ann')
# print(a)
# a.remove('Ann')
# # a.remove('Ann1')  # KeyError (обратились к несуществующему элементу)
# print(a)
# # user = 'Tom'
# # if user in a:
# #     a.remove(user)
# # print(a)
# # a.discard('Ann')  # = remove
# # a.discard('Ann1')  # NO ERROR
# # print(a)
# n = a.pop()
# print(a)
# print(n)
# a.clear()
# print(a)  # set()

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# # c = a.union(b)  # {0, 1, 2, 3, 4}
# # a |= b
# c = a | b  # {0, 1, 2, 3, 4}
# print(c)
# # a &= b
# d = a & b  # {1, 2, 3}
# print(d)
# # a -= b
# e = a - b  # {0}
# print(e)
# # a ^= b
# f = a ^ b
# print(f)  # {0, 4}

# a, b, c, d, e, f, g = {1, 2}, {3}, {4, 5}, {3, 2, 6}, {6}, {7, 8}, {9, 8}
# unique = a | b | c | d | e | f | g
# print(unique)
# print('Unic elems count:', len(unique))
# print('Min elem:', min(unique))
# print('Max elem:', max(unique))
# print('Sum elem:', sum(unique))

# a = set(input('Введите первую строку: '))
# b = set(input('Введите вторую строку: '))
# c = a & b
# print('Общими буквами являются:')
# for i in c:
#     print(i, end=' ')

# a = set(input('Введите первую строку: '))
# b = set(input('Введите вторую строку: '))
# c = a - b
# print('Искомыми буквами являются:')
# for i in c:
#     print(i, end=' ')

# Drawing = {'Marina', 'Jenya', 'Sveta'}
# Music = {'Kostya', 'Jenya', 'Ilya'}
#
# print('Only one hobby:', Drawing ^ Music)
# print('Both hobbies:', Drawing & Music)
# print('Drawing:', Drawing - Music)

# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# print(a <= b)  # False
# print(a >= b)  # True


# -----------------------------------------------------
# Тип замороженные множества (frozenset)

# s = frozenset([1, 2, 3, 4, 5])
# print(s)  # frozenset({1, 2, 3, 4, 5})
# print(type(s))
# a = frozenset({'hello', 'world'})
# print(a)  # frozenset({'hello', 'world'})

# a = [7, 4, 5, 6, 6, 8, 2, 3, 5, 8, 9, 1, 2, 4, 0, 8]
# print(a)
# b = set(a)
# # print(b)
# a = list(b)
# c = tuple(b)
# print(a)
# print(c)


# -----------------------------------------------------
# Словари (dict)
# Ключи: int, str, tuple, bool (неизменяемые)
# Значения: любой тип данных

# lst = [1, 2, 3]
# d = {'one': 1, 'two': 2, 'three': 3, 4: 'four'}
# lst[0] = 10
# print(lst[0])  # 10
# d['one'] = 10
# print(d['one'])  # 10
# print(d[4])  # four

# d = {'one': 1, 'two': 2}
# print(d)
# print(type(d))  # dict
#
# d1 = dict({'one': 1, 'two': 2, 4: 'four'})
# d2 = dict(one=1, two=2, four='four')
# print(d1)
# print(type(d1))  # dict
# print(d2)
# print(type(d2))  # dict

# # d = {0: 1, 'two': 2, 1: 45, (1, 2.3): 'tuple', True: [1, 2, 7], False: 'hehe'}
# # {0: 'hehe', 'two': 2, 1: [1, 2, 7], (1, 2.3): 'tuple}
# d = {0: 1, 'two': 2, (1, 2.3): 'tuple', True: [1, 2, 7]}
# print(d)
# print(d[True][1])  # 2
# print(d[(1, 2.3)])  # tuple

# lst = [1, 2, 3]
# d = dict(lst)  # TypeError

# lst = [('one', 1), ['two', 2], ['three', 3]]
# d = dict(lst)
# print(d)  # {'one': 1, 'two': 2, 'three': 3}

# d = {a: a ** 2 for a in range(7)}
# print(d, type(d))  # dict

# d = {'one': 1, 'two': 2, 'four': 4}

# print('one' in d)  # True
# print(1 in d)  # False

# key = 'four'
# del d[key]

# key = 'four1'
# if key in d:
#     del d[key]

# key = 'four1'
# try:
#     del d[key]
# except KeyError:
#     print("There's no such key in this dictionary")
#
#
# for i in d:
#     print(i, '->', d[i])

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# print(d, end='\n\n')
# res = 1
# for i in d:
#     res *= d[i]
# print(res)

# orig = {i: input("-> ") for i in range(1, 5)}
# print(orig)
# exc = int(input("Какой элемент исключить: "))
# try:
#     del orig[exc]
#     print(orig)
# except KeyError:
#     print("Пожалуйста, выберите существующий элемент")

# myDict = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# print(len(myDict))  # 4
# print(min(myDict))  # x1
#
# myDict1 = {3: 'x1', 7: 'x2', 5: 'x3', -1: 'x4'}
# print(sum(myDict1))  # 14

# goods = {
#     '1': ['Core-i3-4330', 9, 4500],
#     '2': ['Core-i5-4670K', 3, 8500],
#     '3': ['AMD FX-6300', 6, 3700],
#     '4': ['Pentium 63220', 8, 2100],
#     '5': ['Core-i5-34500', 5, 6400]
# }
# for i in goods:
#     print(i, ') ', goods[i][0], ' - ', goods[i][1], ' шт. по ', goods[i][2], 'руб', sep='')
#
# while True:
#     num = input("№: ")
#     if num != '0':
#         try:
#             goods[num][1] = int(input('Количество: '))
#         except KeyError:
#             pass
#     else:
#         break
#
# for i in goods:
#     print(i, ') ', goods[i][0], ' - ', goods[i][1], ' шт. по ', goods[i][2], 'руб', sep='')

# d = {'a': 1, 'b': 2, 'c': 3}
#
# print(d.keys())  # список ключей
# print(d.values())  # список значений
# print(d.items())  # список ключей и значений (кортежи)
#
# # for i in d.values():
# #     print(i)  # 1 2 3
# #
# # for i in d.items():
# #     print(i)  # ('a', 1) ('b', 2) ('c', 3)
# #
# # for i, j in d.items():
# #     print(i, '->', j)
#
# print(list(d))  # список ключей
# print(list(d.values()))  # список значений
# print(list(d.items()))  # список ключей и значений (кортежи)

# d = {'a': 1, 'b': 2, 'c': 3}
#
# # # d2 = d
# # d2 = d.copy()
# # print('d:', d, id(d))
# # print('d2:', d2, id(d2))
# #
# # d2['a'] = 5
# # d['e'] = 7
# # print('d:', d, id(d))
# # print('d2:', d2, id(d2))
# #
# # d.clear()  # очищает тот же словарь
# # print('d:', d, id(d))
# # print('d2:', d2, id(d2))
#
# # # print(d['e'])  # KeyError
# # value = d.get('e', "There's no such key")  # None
# # print(value)  # 2
# # item = d.pop('b')  # обязательно значение
# # item = d.pop('e', "there's no such key")  # KeyError
# item = d.popitem()
# print(item)  # 2 / there's no such key / ('c', 3)
# print(d)  # {'a': 1, 'c': 3} / {'a': 1, 'b': 2, 'c': 3} / {'a': 1, 'b': 2}
#
# a = [1, 2, 3]
# n = a.pop(0)
# print(n)  # 1

# d = {'a': 1, 'b': 2, 'c': 3}
# d1 = {'r': 7, 'q': 40}
#
# # d2 = d + d1  # TypeError
# # print(d)
# d.update(d1)
# # d2 = {'a': 20, 'b': 9}
# d2 = [('a', 20), ('b', 9)]
# d.update(d2)
# print(d)  # {'a': 1, 'b': 2, 'c': 3, 'r': 7, 'q': 40}
# # {'a': 20, 'b': 9, 'c': 3, 'r': 7, 'q': 40}

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
#
# # z = {}
# # z.update(x)
# # z.update(y)
#
# # z = x.copy()
# # z.update(y)
#
# z = x | y
# print(z)

# a = {
#     'first': {
#         1: 'one',
#         2: 'two',
#         3: 'three'
#     },
#     'second': {
#         4: 'four',
#         5: 'five'
#     }
# }
# print(a)
# for x in a:
#     print(x)
#     # print(a[x])
#     for y in a[x]:
#         print('\t', y, ': ', a[x][y], sep='')

# sales = {'John': {'N': 3056, 'S': 8463, 'E': 8441, 'W': 2694},
#          'Tom': {'N': 4832, 'S': 6786, 'E': 4737, 'W': 3612},
#          'Anne': {'N': 5239, 'S': 4802, 'E': 5820, 'W': 1859},
#          'Fiona': {'N': 3904, 'S': 3645, 'E': 8821, 'W': 2451}}
#
# for x in sales:
#     print(x)
#     for y in sales[x]:
#         print('\t', y, ': ', sales[x][y], sep='')
#
# person = input("Name: ")
# region = input("Region: ")
# print(sales[person][region])
# new_data = int(input("New data: "))
#
# sales[person][region] = new_data
# print(sales[person])

# d = {'N': 3056, 'S': 8463, 'E': 8441, 'W': 2694}
# d = {value: key for key, value in d.items()}
# print(d)
#
# d = {'N': 3056, 'S': 8463, 'E': 8441, 'W': 2694}
# d.update({value: key for key, value in d.items()})
# print(d)

# d = {'N': 1, 'S': 2, 'E': 3, 'W': 4}
# # new_d = {k: v for k, v in d.items() if v <= 2}
# for i in range(2):
#     print('key:', list(d.items())[i][0], 'value:', list(d.items())[i][1])

# a = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
#
# d = {}
# current_key = ''
#
# for i in a:
#     if type(i) is str:
#         d[i] = []
#         current_key = i
#     else:
#         d[current_key].append(i)
#
# for i in range(len(a)):
#     if type(a[i]) is str:
#         d[a[i]] = []
#         for j in range(i + 1, len(a)):
#             if type(a[j]) is int:
#                 d[a[i]].append(a[j])
#             else:
#                 break
#
# print(d)

# print(list(d.items()))  # [(1, 'one'), (2, 'two'), (3, 'three')]
# d = dict(zip([1, 2, 3, 4, 5], ['one', 'two', 'three']))
# print(d)  # {1: 'one', 2: 'two', 3: 'three'}
#
# a = [1, 2, 3]
# b = ['one', 'two', 'three']
# f = {k: v for k, v in zip(a, b)}
# print(f)  # {1: 'one', 2: 'two', 3: 'three'}

# a = [1, 2, 3]
# b = ['one', 'two', 'three']
# c = [4.5, 7.4, 9.6]
# # c = zip(a, b)
# # print(c)  # <zip object at 0x000002E463372E80>
#
# # c = tuple(zip(a, b))
# # d = list(zip(a, b))
# # e = set(zip(a, b))
# # print(c)  # ((1, 'one'), (2, 'two'), (3, 'three'))
# # print(d)  # [(1, 'one'), (2, 'two'), (3, 'three')]
# # print(e)  # {(2, 'two'), (1, 'one'), (3, 'three')}
#
# # c = list(zip(a, ))
# # print(c)
#
# d = list(zip(a, b, c))
# print(d)  # [(1, 'one', 4.5), (2, 'two', 7.4), (3, 'three', 9.6)]

# d1 = {'name': 'Igor', 'last_name': 'Petrov', 'job': 'Consultant'}
# d2 = {'name': 'Irina', 'last_name': 'Irisova', 'job': 'Manager'}
#
# for (k1, v1), (k2, v2) in zip(d1.items(), d2.items()):
#     print(k1, '->', v1)
#     print(k2, '->', v2)

# d = [(1, 'one'), (2, 'two'), (3, 'three')]
# a, b = zip(*d)
# print(a)  # (1, 2, 3)
# print(b)  # ('one', 'two', 'three')


# a = ['two', 'one', 'three']
# b = [3, 2, 1]

# d = dict(zip(a, b))
# print(d)
# d1 = sorted(d.items())
# print(d1)  # [('one', 2), ('three', 1), ('two', 3)]
# print(dict(d1))  # {'one': 2, 'three': 1, 'two': 3}

# d = list(zip(a, b))
# print(d)
# d.sort()
# print(d)  # [('one', 2), ('three', 1), ('two', 3)]
# print(dict(d))  # {'one': 2, 'three': 1, 'two': 3}

# one = {'apple': 0.45, 'orange': 0.35}
# two = {'pepper': 0.2, 'onion': 0.55}
# print({**one, **two})  # {'apple': 0.45, 'orange': 0.35, 'pepper': 0.2, 'onion': 0.55}
#
# # print({**one})  # Распаковка словаря {'apple': 0.45, 'orange': 0.35}
#
# for k, v in {**one, **two}.items():
#     print(k, '->', v)

# data = ['red', 'green', 'blue']
# num = 1
# for val in data:
#     print(num, ") ", val, sep='')
#     num += 1
#
# print()
# for num, val in enumerate(data, 1):
#     print(num, ") ", val, sep='')


# -----------------------------------------------------
# Функции (func) - *args, **kwargs
# * - распаковка кортежа

# a = [1, 2, 3]
# b = [*a, 4, 5, 6]  # [1, 2, 3, 4, 5, 6]
# print(b)

# def func(*args):
#     # print(args)
#     # print(type(args))
#     # print()
#     return args
#
#
# print(func(2))
# print(func(2, 3, 4, 'abc'))
# print(func())  # ()

# def summa(*params):
#     res = 0
#     for i in params:
#         res += i
#     return res
#
#
# print(summa(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(summa(3, 4, 5))

# def my_dict(*args):
#     return {i: i for i in args}
#
#
# print(my_dict(1, 2, 3, 4))
# print(my_dict('grey', (2, 17), 3.11, -4))

# def mean(*args):
#     print(sum(args) / len(args))
#     res = []
#     for i in args:
#         if i < (sum(args) / len(args)):
#             res.append(i)
#     return res
#
#
# print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(mean(3, 6, 1, 9, 5))

# def func(a, *args):
#     return a, args
#
#
# print(func(1))  # (1, ())
# print(func(1, 2, 3, 4, 5, 6))  # (1, (2, 3, 4, 5, 6))

# def print_score(student, *scores):
#     print("Student name:", student)
#     for score in scores:
#         print(score)
#
#
# print_score("Irina", 5, 4, 3, 2, 5)
# print_score("Igor", 5, 4, 2, 3, 4)
# print_score("Lev")

# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(d=9))

# def intro(**data):
#     for k, v in data.items():
#         print(k, '->', v)
#     print()
#
#
# intro(name='Irina', surname='Reznikova', age=22)
# intro(name='Igor', surname='Berukov', email='igor@mail.ru', age=25, phone='8(800)555-35-35')

# def db(**kwargs):
#     my_dict.update(kwargs)
#     print("Inside the function:", id(my_dict))
#
#
# my_dict = {'one': 'first'}
# # print(id(my_dict))
# db(k1=22, k2=31, k3=11, k4=91)
# db(name='Bob', age=31, weight=61, eyes_color='grey')
# # print(id(my_dict))
# print(my_dict)

# def func(a, b, *args, d, e, **kwargs):
#     return a, b, args, e, kwargs, d
#
#
# print(func(5, 5, 7, 9, 3, k1=22, k2=31, d=55, e=100))


# -----------------------------------------------------
# Области видимости (onsets)
# LEGB (Local, Enclosed, Global, Built-in)

# name = 'Tom'
#
#
# def hi():
#     global name
#     name = 'Sam'
#     surname = 'Johnson'
#     print('Hello', name, surname)
#
#
# def bye():
#     print('Good bye', name)
#
#
# hi()
# bye()
# print(name)
# print("Global onset:", id(name))

# i = 5
#
#
# def func(arg=i):
#     print(arg)
#
#
# i = 6
# func()  # 5

# x = 4
#
#
# def add_five(a):
#     # x = 2
#
#     def add_some():
#         # x = 1
#         print('x =', x)
#         return a + x
#     return add_some()
#
#
# print(add_five(5))

# import builtins
#
# name = dir(builtins)
#
# for i in name:
#     print(i)

# def outer(who):
#     def inner():
#         print("Hello,", who)
#
#     inner()
#
#
# outer("World!")

# def fun1():
#     a = 6
#
#     def fun2(b):
#         a = 4
#         print(a + b)
#
#     print("a:", a)
#     fun2(4)
#
#
# fun1()

# x = 25
#
#
# def fn():
#     global t  # выводит переменную в глобальную ОВ
#     a = 30
#
#     def inner():
#         nonlocal a  # выводит переменную на уровень выше
#         a = 35
#         print('a:', a)
#
#     inner()
#     t = a
#
#
# fn()
# c = x + t
# print(c)

# x = 5
#
#
# def fn1():
#     x = 25
#
#     def fn2():
#         x = 33
#
#         def fn3():
#             nonlocal x
#             x = 55
#
#         fn3()
#         print('fn2, x =', x)  # 33 -> 55
#
#     fn2()
#     print('fn1, x =', x)  # 25
#
#
# fn1()

# def outer(a1, b1, a2, b2):
#     a = 0  # 1
#     b = 0  # 7
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
#
# res = outer(2, 3, -1, 4)
# print(res)  # [0, 0] -> [1, 7]


# -----------------------------------------------------
# Замыкание (одна функция возвращает другую без ее вызова)

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# item1 = outer(5)  # function inner
# print(item1(10))  # inner(x) -> 15
#
# item2 = outer(5)
# print(item2(1))  # 6
#
# # print(outer(20)(5))  # 25

# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a += 1
#         b += '_new'
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())

# def func(city):
#     s = 0
#
#     def inner():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return inner
#
#
# res1 = func('Москва')
# res1()
# res1()
# res2 = func('Сочи')
# res2()
# res2()
# res2()
# res1()


# -----------------------------------------------------
# Lambda (анонимные функции)

# print((lambda x, y: x + y)(1, 2))  # 3
#
# func = lambda x, y: x + y  # есть имя => def
# print(func(1, 2))
# print(func('a', 'b'))

# print((lambda x, y: x ** 2 + y ** 2)(2, 5))  # 29
# print((lambda x=2, y=5: x ** 2 + y ** 2)(1, 7))  # 50

# print((lambda *args: args)(1, 2, 3, 4, 5))

# y = (
#     lambda x: x * 2,
#     lambda x: x * 3,
#     lambda x: x * 4
# )
#
# for i in y:
#     print(i('abc__'))

# def outer(n):
#     def inner(x):
#         return x + n
#
#     return inner
#
#
# f = outer(5)
# print(f(10))  # 15
#
#
# def outer1(n):
#     return lambda x: x + n
#
#
# f1 = outer1(5)
# print(f1(10))  # 15
#
#
# outer2 = lambda n: lambda x: x + n
# f1 = outer2(5)
# print(f1(10))  # 15
#
#
# print((lambda n: lambda x: x + n)(5)(10))  # 15

# print((lambda a: lambda b: lambda c: a + b + c)(2)(4)(6))  # 12

# def func(item):
#     return item[1]
#
#
# d = {'b': 3, 'c': 1, 'a': 2}  # {'c': 1, 'a': 2, 'b': 3}
# print(d)
# lst = list(d.items())
# print(lst)
# # lst.sort(key=lambda i: i[1])  # [('c', 1), ('a', 2), ('b', 3)]
# lst.sort(key=func)  # [('c', 1), ('a', 2), ('b', 3)]
# print(lst)
# d1 = dict(lst)
# print(d1)

# players = [
#     {'name': 'Антон', 'last name': 'Бирюков', 'rating': 9},
#     {'name': 'Алексей', 'last name': 'Бодня', 'rating': 10},
#     {'name': 'Федор', 'last name': 'Сидоров', 'rating': 4},
#     {'name': 'Михаил', 'last name': 'Семенов', 'rating': 6},
# ]
#
# res1 = sorted(players, key=lambda i: i['last name'])
# print(res1)
#
# res2 = sorted(players, key=lambda i: i['rating'])
# print(res2)
#
# res3 = sorted(players, key=lambda i: i['rating'], reverse=True)
# print(res3)

# a = [
#     lambda x, y: x + y,  # a[0] -> 7
#     lambda x, y: x - y,  # a[1] -> 3
#     lambda x, y: x * y,  # a[2] -> 10
#     lambda x, y: x / y,  # a[3] -> 2.5
# ]
#
# print(a[0](5, 2))
# print(a[1](5, 2))
# print(a[2](5, 2))
# print(a[3](5, 2))

# d = {
#     1: lambda: print('Monday'),
#     2: lambda: print('Tuesday'),
#     3: lambda: print('Wednesday'),
#     4: lambda: print('Thursday'),
#     5: lambda: print('Friday'),
#     6: lambda: print('Saturday'),
#     7: lambda: print('Sunday'),
# }
#
# d[6]()  # Saturday

# print((lambda a, b: a if a > b else b)(15, 23))

# print((lambda a, b, c: a if (a < b and a < c) else (b if b < c else c))(9, 8, 5))


# -----------------------------------------------------
# map(func, *iterables)

# def mult(t):
#     return t * 2
#
#
# lst1 = [2, 8, 12, -5, -10]
#
# lst2 = list(map(mult, lst1))
# # lst2 = list(map(lambda t: t * 2, [2, 8, 12, -5, -10]))
# print(lst2)  # [4, 16, 24, -10, -20]

# t = (2.88, -1.75, 100.55)
# # t2 = tuple(map(int, t))
# t2 = tuple(map(lambda x: int(x), t))
# print(t2)  # (2, -1, 100)

# print(int((2.88, -1.75, 100.55)))  # TypeError

# t = "Hello"
# t2 = tuple(map(str, t))
# print(t2)  # ('H', 'e', 'l', 'l', 'o')

# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5, 6]
#
# res = list(map(lambda x, y: (x, y), st, num))
# print(res)
#
# res1 = list(map(lambda x, y: x * y, st, num))
# print(res1)

# num = ['1', '2', '3', '4', '5']
# # print(int(num))  # TypeError
# print(list(map(int, num)))  # [1, 2, 3, 4, 5]

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# print(list(map(lambda x, y: x + y, l1, l2)))

# t = ('kdfjs', 'ewhehf', 'jshfiu', 'hfru', 'eufvb')
# t2 = filter(lambda s: len(s) == 5, t)
# print(tuple(t2))

# b = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# res = list(filter(lambda s: s > 75, b))
# print(res)  # [90, 76, 88, 81]
#
# res1 = list(map(lambda x: x + 5, b))
# print(res1)  # [71, 95, 73, 64, 81, 65, 93, 79, 86, 70]

# m = list(map(lambda x: x ** 2, range(10)))
# print(m)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#
# n = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(10))))
# print(n)  # [1, 9, 25, 49, 81]
#
# n1 = [x ** 2 for x in range(10) if x % 2]
# print(n1)  # [1, 9, 25, 49, 81]

# from random import randint
# a = list(randint(0, 50) for i in range(10))
# print(a)
#
# print('[10; 20] =', list(filter(lambda x: 10 <= x <= 20, a)))

# def hello():
#     return "Hello, I'm func 'hello'"
#
#
# def super_func(func):
#     print("Hello, I'm func 'super_func'")
#     print(func())
#
#
# super_func(hello)

# def hello():
#     return "Hello, I'm func 'hello'"
#
#
# test = hello
# print(test())  # Hello, I'm func 'hello'

# def my_decorator(func):
#     def wrap():
#         print("Before the function")
#         func()
#         print("After the function")
#     return wrap
#
#
# def func_test():
#     print("Hello, I'm func 'func_test'")
#
#
# test = my_decorator(func_test)
# test()

# def my_decorator(func):  # декорирующая функция
#     def wrap():
#         print('+' * 30)
#         func()
#         print('=' * 30)
#     return wrap
#
#
# @my_decorator  # декоратор
# def func_test():  # декорируемая функция
#     print("Hello, I'm func 'func_test'")
#
#
# @my_decorator
# def hello():
#     print("Hello I'm func 'hello'")
#
#
# func_test()
# hello()

# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#
#     return wrap
#
#
# @bold
# @italic
# def hello():
#     return 'text'
#
#
# print(hello())

# def quant(func):
#     n = 0
#
#     def wrap(arg1, arg2):
#         nonlocal n
#         n += 1
#         func(arg1, arg2)
#         print("Вызов функции: ", n, "\n", "*" * 20, sep='')
#         return func
#
#     return wrap
#
#
# @quant
# def hello(a, b):
#     print('Hello,', a, '\nHello,', b)
#
#
# hello('Python', 'JavaScript')
# hello('one', 'two')
# # hello()

# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print('args:', args)
#         print('kwargs:', kwargs)
#         fn(*args, **kwargs)
#
#     return wrap
#
#
# @args_decorator
# def print_data(a, b, c, study='Python'):
#     print(a, b, c, 'изучают', study, '\n')
#
#
# print_data("Борис", "Елизавета", "Светлана", study='JavaScript')
# print_data("Владимир", "Екатерина", "Виктор")

# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=' ')
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
#
# @decor("Сумма:", '+')
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность:", '-')
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)

# def multiply(args1):
#     def test(fn):
#         def wrap(x):
#             return fn(x) * args1
#
#         return wrap
#     return test
#
#
# @multiply(3)
# def return_num(num):
#     return num
#
#
# print('Result:', return_num(5))


# -----------------------------------------------------
# str (строки)
# Префиксы строк:
# U/u => строка выводится в юникоде
# R/r => подавление экранирования элементов
# F/f => вывод переменных в составе строки
# fr => сборка адреса файла/папки т.д. в памяти

# print(05)  # SyntaxError

# print(int('18'))
# print(int(18.5))
# # print(int('18.5'))  # ValueError

# print(int('100', 2))  # 10
# print(int('100', 8))  # 64
# print(int('100', 10))  # 100
# print(int('100', 16))  # 256
#
# print(bin(18))  # двоичная СИ -> 0b10010
# print(oct(18))  # восьмеричная СИ -> 0o22
# print(hex(18))  # двенадцатеричная СИ -> 0x12
#
# print(0b10010)  # десятичная СИ -> 18
# print(0o22)  # десятичная СИ -> 18
# print(0x12)  # десятичная СИ -> 18
# print(0b10010 + 0o22 + 0x12 + 18)  # 72

# q = 'Pyt'
# w = 'hon'
# e = q + w
# print(e)
# # print(e * -3)  # (empty)
# # print('y' in e)  # True
# # print('y1' in e)  # False
# # print(e[1])  # y
# # print(e[-6])  # P
# # print(e[1:4])  # yth
# # print(e[::-1])  # nohtyP
#
# # e[3] = 't'  # TypeError (str - неизменяемый тип данных)
# e = e[:3] + 't' + e[4:]
# print(e)  # Pytton

# def changeCharToStr(s, c_old, c_new):
#     s2 = ""
#     i = 0
#
#     while i < len(s):
#         if s[i] == c_old:
#             s2 += c_new
#         else:
#             s2 += s[i]
#         i += 1
#
#     return s2
#
#
# str1 = 'Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования.'
#
# str2 = changeCharToStr(str1, 'N', 'P')
# print('str1 =', str1)
# print('str2 =', str2)

# print("Привет")
# print(u"Привет")  # U/u => строка выводится в юникоде

# print("C:\\folder\\file.txt\\")
# print(r"C:\folder\file.txt")  # R/r => подавление экранирования элементов
# print(r"C:\folder\file.txt\\"[:-1])
# print(R"C:\folder\file.txt" + "\\")

# name = "Dmitry"
# age = 25
# print(f"My name is {name}, I'm {age} years old.")  # F/f => вывод переменных в составе строки
# m = 2.27456287
# print(f'Number: {round(m, 2)}')  # 2.27 (str)
# print(f'Number: {m:.3f}')  # 2.27 (str)

# x = 10
# y = 5

# print(f"{x = }, {y = }")  # x=10, y=5
# print("x = ", x, ", y = ", y, sep='')
# # print(x=, y=)  # SyntaxError

# print(f"{x} x {y} / 2 = {x * y / 2}")  # 10 x 5 / 2 = 25.0

# num = 74
# print(f'{{num}}')  # {num}
# print(f'{{{num}}}')  # {74}
# print(f'{{{{{num}}}}}')  # {{74}}

# dir_name = "my_doc"
# file_name = "data.txt"
# print(fr"home\{dir_name}\{file_name}")
# print("home\\" + dir_name + "\\" + file_name)

# s = """
# Многострочный\n
# текст
# """
# print(s)
#
# s1 = '''
# Многострочный 'самый' "новый"
#         текст
# '''
# print(s1)
#
# s2 = "Te\n        xt"
# print(s2)

# def square(n):
#     """Принимает число n, возвращает его квадрат"""
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)
# print(sum.__doc__)
# print(min.__doc__)
# print(len.__doc__)


# from Geometry import pi
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданных высоты и радиуса основания
#
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     print('Hello')
#     return 2 * pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)

# print(ord('a'))  # 97 - кодировка ASCII/Unicode
# print(ord('й'))  # 1081

# while True:
#     n = input("-> ")
#     if n != -1:
#         print(ord(n))
#     else:
#         break

# print(chr(1104))  # ѐ

# str1 = 'Test string for me'
# code = [ord(i) for i in str1]
# print('ASCII коды:', code)
#
# # mean = round(sum(code) / len(code))
# # code.insert(0, mean)
# # print('Среднее арифметическое:', code)
#
# code = [int(sum(code) / len(code))] + code
# print('Среднее арифметическое:', code)
#
# code += [ord(x) for x in input('-> ')[:3] if ord(x) not in code]
# print(code)
#
# print('Количество элементов, равных последнему:', code.count(code[-1]) - 1)
#
# code.sort(reverse=True)
# print(code)

# print(chr(97))  # a
# print(chr(1048))  # И
# print(chr(8364))  # €

# print("apple" == "Apple")  # False
# print("apple" > "Apple")  # True
#
# print(ord("a"))  # 97
# print(ord("A"))  # 65

# from random import randint
#
# SHORTEST = 7
# LONGEST = 10
# MIN_ASCII = 13
# MAX_ASCII = 126
#
#
# def random_password():
#     random_length = randint(SHORTEST, LONGEST)
#     result = ''
#     for x in range(random_length):
#         result += chr(randint(MIN_ASCII, MAX_ASCII))
#
#     return result
#
#
# print('Ваш случайный пароль:', random_password())


# -----------------------------------------------------
# Методы типа данных str (строки)
# s.capitalize() - первая буква прописная
# s.lower() - все буквы строчные
# s.upper() - капслок
# s.swapcase() - прописные и строчные меняются местами
# s.title() - каждое слово начинается с большой буквы
# s.count() - количество вхождений подстроки в строку
# s.find() - индекс подстроки в строке (иначе -1)
# s.rfind() - поиск подстроки справа (иначе -1)
# s.index() - индекс подстроки в строке (ValueError)
# s.rindex() - поиск подстроки справа (ValueError)
# s.startswith() - True, если строка начинается с указанной подстроки
# s.endswith() - True, если строка оканчивается указанной подстрокой
# s.isalpha() - True, если строка включает только буквы
# s.isdigit() - True, если строка включает только цифры
# s.isalnum() - True, если строка включает буквы и цифры
# s.islower() - True, если все буквы в строке строчные
# s.isupper() - True, если все буквы в строке прописные
# s.center() - Выравнивание строки по центру
# s.lstrip() - Удаление пробелов с левой стороны
# s.rstrip() - Удаление пробелов с правой стороны
# s.strip() - Удаление пробелов с обеих сторон
# s.replace() - Замена одного элемента другим
# s.join() - Объединяет str-элементы итерируемого объекта посредством строки ([a, b, c] -> a-b-c)
# s.split() - Делит строку по элементу-разделителю на список из подстрок
# s.rsplit() - Делит строку по элементу-разделителю на список из подстрок + сохраняет ссылки

# s = "hello, WORLD! I am learning Python."
# print(s.capitalize())  # Hello, world! i am learning python.
# print(s.lower())  # hello, world! i am learning python.
# print(s.upper())  # HELLO, WORLD! I AM LEARNING PYTHON.
# print(s.swapcase())  # HELLO, world! i AM LEARNING pYTHON.
# print(s.title())  # Hello, World! I Am Learning Python.
# print(s)  # hello, WORLD! I am learning Python.
# print(s.count('h'))  # 2
# print(s.count('h', 1, -4))  # 0
# print(s.find("Python"))
# print(s.find("Python", 10, -20))  # -1 => False
# print(s.find("hehe"))  # -1
# print(s.rfind("Python"))  # 28
# print(s.rfind("Python"))
# print(s.find('l'))  # 2
# print(s.rfind('l'))  # 19
# # print(s.rfind('l1'))  # -1
#
# print(s.index('l'))  # 2
# print(s.rindex('l'))  # 19
#
# print(s.index('l1'))  # ValueError

# orig = input("Введите два слова через пробел: ")
# space = orig.find(' ')
# if space == -1:
#     print("Ошибка ввода данных")
# else:
#     print(f'{orig[orig.find(' ') + 1:]} {orig[:orig.find(' ')]}')

# print(s.startswith('hello'))  # True
# print(s.find('I am'))  # 14
# print(s.startswith('I am'))  # False
# print(s.startswith('I am', 14))  # True
#
# print(s.endswith('on.'))  # True
# print(s.endswith('lo'))  # False
# print(s.endswith('lo', 3, 5))  # True

# print("abc123".isalpha())  # False
# print("abcDEF".isalpha())  # True
# print("abcDE!".isalpha())  # False
#
# print("123".isdigit())  # True
# print("12A3".isdigit())  # False
# print("123.234".isdigit())  # False
#
# print("Abc123".isalnum())  # True
# print("Abc$123".isalnum())  # False

# print("abc".islower())  # True
# print("a_bc4725".islower())  # True
#
# print("ABC".isupper())  # True
# print("ABC182749!&".isupper())  # True

# print('py'.center(10, '-'))  # ----py----
# print('py'.center(11, '-'))  # -----py----
# print('py'.center(1))  # py

# print("         py".lstrip())  # py
# print("         p y".lstrip())  # p y
# print("py          ".rstrip())  # py
# print("    py      ".strip())  # py

# print("https://www.python.org".lstrip())
# print("https://www.pythons.org".lstrip("/:pths").rstrip(".org"))
# print("https://www.pythons.org".strip("/:pths.org"))

# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# print(str1)
# print(str1.replace("Nython", "Python", 2))

# s1 = "-"
# seq = ("a", "b", "c")
# print(s1.join(seq))  # a-b-c
# print("..".join(['1', '2']))  # 1..2
# # print("..".join([1, 2]))  # TypeError
# print(":".join("Hello"))  # H:e:l:l:o

# print(s.split())  # ['hello,', 'WORLD!', 'I', 'am', 'learning', 'Python.']
# print('www.python.org.ru'.split('.', 2))  # ['www', 'python', 'org']
# print('www.python.org.ru'.rsplit('.'))
# print('www.python.org.ru'.rsplit('.', 2))

# a = input("Введите ФИО: ").split()
# print(a)
#
# print(f'{a[0]} {a[1][0]}.{a[2][0]}.')

# a = list(map(int, input("-> ").split()))
# print(a)


# -----------------------------------------------------
# Регулярные выражения
# re.findall() - возвращает список, содержащий все совпадения с шаблоном (совпадений нет => [])
# re.search() - возвращает месторасположение первого совпадения с шаблоном
# re.match() - возвращает месторасположение совпадения с шаблоном, но только в начале строки
# re.split() - возвращает список, в котором строка разбита по шаблону
# re.sub() - поиск совпадений и их замена

# import re
#
# s = "Я ищу совпадения в 2024 году. И я их найду в 2 счёта."
# reg = "я"
# reg1 = "Я ищу"
# reg2 = "."
# reg3 = "[.я2]"
# reg4 = r"\."

# print(re.findall(reg, s))  # ['я', 'я']
#
# print(re.search(reg, s))  # <re.Match object; span=(15, 16), match='я'>
# print(re.search(reg, s).span())  # (15, 16)
#
# print(re.search(reg, s).start())  # 15
# print(re.search(reg, s).end())  # 16
#
# print(re.search(reg, s).group())  # я

# print(re.match(reg, s))  # None
# print(re.match(reg1, s))  # <re.Match object; span=(0, 5), match='Я ищу'>

# print(re.split(reg, s, 1))  # ['Я ищу совпадени', ' в 2024 году. И я их найду в 2 счёта.']
# print(re.split(reg2, s))  # ['', '', ..., '', '']
# print(re.split(reg3, s))  # ['Я ищу совпадени', ' в ', '0', '4 году', ' И ', ' их найду в ', ' счёта', '']

# print(re.sub(reg4, "!", s, 1))  # Я ищу совпадения в 2024 году! И я их найду в 2 счёта.

# import re
#
# s = "Я ищу совпадения в 2024 году. И я их найду в 2 счёта. 198765"
# reg = r"2024"
# reg1 = r"[204]"
# reg2 = r"[0-9]"
# reg3 = r"[12][0-9][0-9][0-9]"
# reg4 = r"[А-яЁё]"
# reg5 = r"[^0-9]"
#
# print(re.findall(reg, s))  # ['2024']
# print(re.findall(reg1, s))  # ['2', '0', '2', '4', '2']
# print(re.findall(reg2, s))  # ['2', '0', '2', '4', '2', '1', '9', '8', '7', '6', '5']
# print(re.findall(reg3, s))  # ['2024', '1987']
# print(re.findall(reg4, s))  # все буквы

# print(ord('Ё'))  # 1025
# print(ord('А'))  # 1040
#
# print(ord('Я'))  # 1071
# print(ord('а'))  # 1072
#
# print(ord('я'))  # 1103
# print(ord('ё'))  # 1105

# print(re.findall(reg5, s))  # все, кроме цифр


# s = "Я ищу совпадения в 2024 году. И я их найду в 2 счёта. 198765 Hello[-World]"
# reg = r"[A-Za-z]"  # r"[a-zA-Z]"
# reg1 = r"[A-Za-z[]]"
# reg2 = r"[A-Za-z[\]]"
# # reg3 = r"[A-Za-z\]-\[]"  # re.error
# reg3 = r"[a-zA-Z\]\[-]"
#
# print(re.findall(reg, s))
# print(re.findall(reg1, s))  # ['d]']
# print(re.findall(reg2, s))
# print(re.findall(reg3, s))

# import re
#
# st = "Час в 24-часовом формате от 00 до 23. 2021-06-15Е21:45. Минуты в диапазоне от 00 до 59. 2021-06-15Т01:09"
#
# req = r"[0-2][0-9]:[0-5][0-9]"
# print(re.findall(req, st))

# s = "Я ищу совпадения в 2024 году. И я их найду в 2 счёта. 198.765 Hello[-World] 2000000"


# -----------------------------------------------------
# Параметры регулярных выражений:

# reg = r"."
# reg1 = r"\."
# reg2 = r"\d"  # выводятся только цифры
# reg3 = r"\D"  # выводится всё, кроме цифр
# reg4 = r"\s"  # выводятся только пробелы
# reg5 = r"\S"  # выводится всё, кроме пробелов
# reg6 = r"\w"  # выводятся все буквы, цифры и _
# reg7 = r"\W"  # выводится всё остальное
# reg8 = r"\AЯ ищу"  # элемент выводится, только если он находится в начале строки
# reg9 = r"-World]\Z"  # элемент выводится, только если он находится в конце строки
# reg10 = r"\bсов"  # элемент выводится, только если он находится в начале или конце слова в пределах строки
# reg11 = r"\B9876"  # элемент выводится, только если он находится в середине слова в пределах строки

# print(re.findall(reg, s))
# print(re.findall(reg1, s))
# print(re.findall(reg2, s))
# print(re.findall(reg3, s))
# print(re.findall(reg4, s))
# print(re.findall(reg5, s))
# print(re.findall(reg6, s))
# print(re.findall(reg7, s))
# print(re.findall(reg8, s))
# print(re.findall(reg9, s))
# print(re.findall(reg10, s))
# print(re.findall(reg11, s))


# -----------------------------------------------------
# Квантификаторы (указание количества повторений):
# ? = [0; 1]
# * = [0; +)
# + = [1; +)
# {x} = ровно x повторений
# {m,n} = от m до n повторений включительно
# {m,} = m или больше повторений
# {,n} = n или меньше повторений

# reg = r"\w"
# reg1 = r"\w+"
# reg2 = r"\d+"
# reg3 = r"20*"  # ['20', '2', '2', '2000000']
# reg4 = r"20?"  # ['20', '2', '2', '20']
# reg5 = r"20+"  # ['20', '2000000']
#
# print(re.findall(reg, s), end='\n\n')
# print(re.findall(reg1, s), end='\n\n')
# print(re.findall(reg2, s), end='\n\n')
# print(re.findall(reg3, s), end='\n\n')
# print(re.findall(reg4, s), end='\n\n')
# print(re.findall(reg5, s), end='\n\n')

# d = "Числа: 7, +17, --42, 0013, 0.3"
# print(re.findall(r"[+-]?\d+[.]?\d*", d))

# st = "05-03-1987  # Date of birth"
# print("Date of birth:", re.sub(r'\s#.*', "", st))  # Date of birth: 05-03-1987
# print("Date of birth:", re.sub('-', '.', re.sub(r'\s#.*', "", st)))  # Date of birth: 05.03.1987
# print("Date of birth:", re.sub(r'\s#.*', "", st).replace('-', '.'))  # Date of birth: 05.03.1987

# st = "author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 1831"
# req = r"\w+\s*=\s*\w+[^;]+"
# print(re.findall(req, st))

# st = "12 сентября 2021 года 235 1454691600"
# reg = r"\d{4}"  # ['2021', '1454', '6916']
# reg1 = r"\d{2,4}"  # ['12', '2021', '235', '1454', '6916', '00']
# reg2 = r"\d{2,}"  # = {2,10}
# reg3 = r"\d{,4}"  # = {0,4}
#
# print(re.findall(reg, st))
# print(re.findall(reg1, st))
# print(re.findall(reg2, st))
# print(re.findall(reg3, st))

# st = "+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578"
# reg = r"\+?7\d{10}"
# print(re.findall(reg, st))
# print(re.findall(r"\+?7\s?[(]?\d{3}[)]?\s?\d{3}-?\s?\d{2}-?\s?\d{2}", st))

# s = "Я ищу совпадения в 2024 году. И я их найду в 2 счёта. 198.765 Hello[-World] 2000010 002000"

# reg = r"\w+\s\w+"
# reg1 = r"\w+\s\w+$"
#
# print(re.findall(reg, s))
# print(re.findall(reg1, s))


# def valid_login(name):
#     # return re.findall(r"[A-Za-z0-9_-]{6,16}", name)  # length = 6-16, english letters, _, -, 0-9
#     return re.findall(r"^[A-Za-z0-9_-]{6,16}$", name)  # length = 6-16, english letters, _, -, 0-9
#
#
# print(valid_login("Python_master"))
# print(valid_login("Python!!!"))  # [Python] -> []
# print(valid_login("Pytho!!!"))  # [] -> []
# print(valid_login("Python@Python"))  # -> []


# -----------------------------------------------------
# Параметр flags= в модуле re:
# re.ASCII or re.A => только ASCII символы
# re.DEBUG
# re.IGNORECASE or re.I => вывод совпадений вне зависимости от регистра буквы
# re.DOTALL or re.S => \n выводится в составе . наравне с другими символами
# re.MULTILINE or re.M => ^ и $ действуют в пределах 1 строки многострочного текста
# re.VERBOSE or re.X => в регулярное выражение включаются пробелы и комментарии, считываются переносы

# print(re.findall(r"\w", "12 + й"))  # ['1', '2', 'й']
# print(re.findall(r"\w", "12 + й", flags=re.ASCII))  # ['1', '2']
# print(re.findall(r"\w", "12 + й", flags=re.A))  # ['1', '2']

# text = 'hello world'
# print(re.findall(r"\w+", text), end='\n\n')
# print(re.findall(r"\w+", text, re.DEBUG), end='\n\n')
# print(re.findall(r"\w\+", text, re.DEBUG), end='\n\n')

# s = "Я ищу совпадения в 2024 году. И я их найду в 2 счёта. 198.765 Hello[-World] 2000000"
# reg = r'я'
#
# print(re.findall(reg, s, re.IGNORECASE))

# text = """
# one
# two
# """
#
# # print(re.findall(r"one.\w+", text))  # []
# # print(re.findall(r"one.\w+", text, re.DOTALL))  # ['one\ntwo']
#
# print(re.findall(r'one$', text))  # []
# print(re.findall(r'one$', text, re.MULTILINE))  # ['one']

# print(re.findall("""[a-z.-]+@[a-z.-]+""", 'test@mail.ru'))
# print(re.findall("""
# [a-z.-]+    # part 1
# @           # @
# [a-z.-]+    # part 2
# """, 'test@mail.ru', re.VERBOSE))

# text = """Python,
# python,
# PYTHON"""
#
# reg = r"^python"
# reg1 = r"(?i)^python"
# reg2 = r"(?im)^python"
#
# print(re.findall(reg, text))  # ['python']
# print(re.findall(reg1, text))  # ['Python']
# print(re.findall(reg2, text))  # ['Python', 'python', 'PYTHON']


# -----------------------------------------------------
# Жадное и ленивое соответствие регулярных выражений

# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall("<.*>", text))
# print(re.findall("<.*?>", text))  # <body>, </body>
#
# # *?, +?, ??, {m,n}?, {,n}?, {m,}?
#
# st = "12 сентября 2021 года 1454691600"
# reg = r"\d{2,4}"  # разбиение по максимуму (4)
# req = r"\d{2,4}?"  # разбиение по минимуму (2)
# req1 = r"\d{2,}?"
#
# print(re.findall(reg, st))
# print(re.findall(req, st))
# print(re.findall(req1, st))

# s = "<p>Изображение <img  src='bg.jpg'  alt='картинка'> - фон страницы</p>"
# reg = r"<img.*>"  # <img src='bg.jpg'> - фон страницы</p>
# req = r"<img.*?>"  # <img src='bg.jpg'>
# req1 = r"<img[^>]*>"  # <img src='bg.jpg'>
# req2 = r"<img\s+[^>]*src\s*=\s*[^>]+>"  # верная работа кода HTML
#
# print(re.findall(req, s))
# print(re.findall(req1, s))
# print(re.findall(req2, s))

# text = "Python (в русском языке встречаются названия питон[16] или пайтон[17]) - высокоуровневый язык " \
#         "программирования общего назначения с динамической строгой типизаций " \
#         "и автоматическим управлением памятью[18][19]."
# reg = r"\[\d+]"
# reg1 = r"\[.*?]"
#
# print(re.findall(reg, text))
# print(re.findall(reg1, text))

# s = "Петр, Ольга и Виталий отлично учатся!"
# reg = 'Петр|Виктор|Ольга'
#
# print(re.findall(reg, s))

# s = "int = 4, float = 4.0f, double = 8.0"
# reg = r'\w+\s*=\s*\d[.\w]*'
# reg1 = r'int\s*=\s*\d[.\w]*'
# reg2 = r'int\s*=\s*\d[.\w]*|float\s*=\s*\d[.\w]*'
# reg3 = r'(int|float)\s*=\s*\d[.\w]*'
# reg4 = r'(?:int|float)\s*=\s*\d[.\w]*'
#
# print(re.findall(reg, s))
# print(re.findall(reg1, s))  # ['int = 4']
# print(re.findall(reg2, s))  # ['int = 4', 'float = 4.0f']
# print(re.findall(reg3, s))  # ['int', 'float']
# print(re.findall(reg4, s))  # ['int = 4', 'float = 4.0f']
#
#
# # (?:...) -> группирующие скобки перестают быть сохраняющими (актуально только для метода findall)

# s = '127.0.0.1'
# s1 = '127.168.255.255'
#
# reg = r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}'
# req = r'(?:\d{1,3}.){3}\d{1,3}'
#
# print(re.findall(reg, s))
# print(re.findall(reg, s1))
# print(re.findall(req, s))
# print(re.findall(req, s1))

# s = "5 + 7*2 - 4"
# reg = r'\s*[+*-]\s*'
# reg1 = r'\s*([+*-])\s*'
#
# print(re.split(reg, s))  # ['5', '7', '2', '4']
# print(re.split(reg1, s))  # ['5', '+', '7', '*', '2', '-', '4']

# date = '28-08-2021'
# pattern = r'(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(19[0-9][0-9]|20[01][0-9]|202[0-4])'
#
# print(re.findall(pattern, date))
# print(re.search(pattern, date).group())

# s = "Я ищу совпадения в 2024 году. И я их найду в 2 счёта."
# reg = r'[0-9]+\s\D+'
# reg1 = r'([0-9]+)\s(\D+)'
#
# print(re.findall(reg, s))
# # print(re.search(reg, s).group())
# # print(re.search(reg, s)[0])
# print(re.search(reg, s).group(0))
# print(re.findall(reg1, s))
# m = re.search(reg1, s)
# print(m)
# print(m[0])
# print(m[1])
# print(m[2])

# text = """
# Самара
# Москва
# Тверь
# Уфа
# Казань
# """
# count = 0
#
#
# def repl_find(m):
#     global count
#     count += 1
#     return f"<option value='{count}'>{m.group(1)}</option>\n"
#
#
# print(re.sub(r'\s*(\w+)\s*', repl_find, text))

# s = "<p>Изображение <img src=\"bg.jpg\"> - фон страницы </p>"
# reg = r"<img\s+[^>]*src\s*=['\"](.+?)['\"]>"
# reg1 = r"<img\s+[^>]*src\s*=(['\"])(.+?)\1>"
# reg2 = r"<(img)\s+[^>]*src\s*=(?P<q>['\"])(.+?)(?P=q)>"
#
# print(re.findall(reg, s))
# print(re.findall(reg1, s))
# print(re.findall(reg2, s))


# (?P<name>...)  (?P=name) - обращение к круглой скобке по имени

# s = "Самолет прилетает 10/23/2024. Будем рады вас видеть после 10/24/2024"  # 23.10.2024
# reg = r'(?P<mon>\d{2})/(?P<day>\d{2})/(?P<year>\d{4})'
#
# print(re.sub(reg, r'\2.\1.\3', s))
# # print(re.sub(reg, r'(?P=day).(?P=mon).(?P=year)', s))

# s = "yandex.com and yandex.ru"
# reg = r'(([a-z0-9-]{2,}\.)+[a-z]{2,4})'
#
# print(re.sub(reg, r'http://\1', s, re.IGNORECASE))


# -----------------------------------------------------
# Рекурсия (вызов функцией самой себя)

# def elevator(n):  # 5 -> 4 -> 3 -> 2 -> 1 -> 0
#     if n == 0:
#         print("You're in the basement")
#         return n
#     print("=>", n)
#     elevator(n - 1)  # 5 4 3 2 1 (stack)
#     print(n, end=' ')  # 1 2 3 4 5
#
#
# n1 = int(input("Insert the floor you're on: "))  # 5
# elevator(n1)
#
#
# # stack - область в памяти (аля стопка книг)
# # stack => 5 4 3 2 1
# # print(stack) => 1 2 3 4 5


# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res
#
#
# def sum_list(lst):  # [1, ..., 9] -> [3, ..., 9] -> [5, ..., 9] -> [7, ..., 9] -> 9
#     if len(lst) == 1:
#         print(lst, "=> lst[0] =", lst[0])
#         return lst[0]  # 9
#     else:
#         print(lst, "=> lst[0] =", lst[0])
#         return lst[0] + sum_list(lst[1:])  # 1 + ... 3 + ... 5 + ... 7 +
#
#
# print(sum_list([1, 3, 5, 7, 9]))

# def to_str(n, base):  # n = 254 -> 15
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n]  # 'F'
#     else:
#         return to_str(n // base, base) + convert[n % base]  # convert[14] => 'E'
#     # 'F' + 'E' = FE
#
#
# print(to_str(365, 10))
# # print(to_str(18, 2))
# # print(to_str(18, 8))
# print(to_str(254, 16))

# names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Bard', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
# print(names)
# print(len(names))  # 5
# print(names[0])
# print(isinstance(names[0], list))  # False
# print(isinstance(names[3], list))  # True
# print(isinstance(names[1][1], list))  # True
# print(names[1][1][0])  # Chet


# def count_items(lst):
#     count = 0
#     for item in lst:
#         if isinstance(item, list):
#             count += count_items(item)
#         else:
#             count += 1
#     return count
#
#
# print(count_items(names))

#
# def remove(text):
#     if not text:
#         return ""
#     if text[0] == "\t" or text[0] == " ":  # False or True => True
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])
#
#
# print(remove(" Hel     lo\tWor     l\t\td "))


# -----------------------------------------------------
# Работа с файлами
# Текстовые файлы: txt -> читабельные
# Бинарные файлы: изображения, аудио -> нечитабельные
# f.read() - считывание всего файла
# f.readline() - считывание одной строки
# f.readlines() - считывание всех строк в виде списка
# 'r' - чтение файла
# 'w' - создание/перезапись файла
# 'a' - дозапись файла
# 'r+' - чтение ИЛИ перезапись файла
# 'w+' - чтение ИЛИ перезапись ИЛИ создание файла
# 'a+' - дозапись ИЛИ создание файла
# 'b' - бинарный (двоичный режим)

# f = open('test.txt')  # mode='r' / 'r'
# f1 = open(r'C:\Users\a_ego\Documents\Python 313\test.txt')  # Можно использовать файлы, лежащие вне папки проекта
# print(f)
# print(*f)  # Hello!
# print(*f1)  # Hello!
# print(f.closed)  # False
# f.close()
# print(f.closed)  # True
# print(f.mode)  # r
# print(f.name)  # test.txt
# print(f.encoding)  # cp65001


# f = open('test.txt')
# print(f.read(4))  # Hell
# print(f.read())  # o!!!!!
# print(f.read())  # * *
# f.close()

# f = open('test1.txt', 'r')
# print(f.readline())  # This is line1.\n
# print(f.readline(8))  # This is
# print(f.readline())  # line2.\n
# print(f.readline())  # This is line3.
# f.close()

# f = open('test1.txt', 'r')
# print(f.readlines())  # ['This is line1.\n', 'This is line2.\n', 'This is line3.\n']
# f.close()

# f = open('test1.txt', 'r')
# print(f.readlines(16))  # ['This is line1.\n', 'This is line2.\n']
# f.close()

# f = open('test1.txt', 'r')
# for line in f:
#     print(line)
# f.close()

# f = open('test1.txt', 'r')
# count = 0
# for i in f:
#     count += 1
# print("count =", count)

# f = open('test1.txt', 'r')
# print("count =", len(f.readlines()))
# f.close()

# f = open('xyz.txt', 'w')
# f.write("Hello\nWorld!\n")
# f.close()

# f = open('xyz.txt', 'a')
# f.write("New text\n")
# f.close()

# f = open('xyz.txt', 'w')
# line = ["This is line 1\n", "This is line 2\n"]
# f.writelines(line)
# f.close()

# f = open('xyz.txt', 'w')
# lst = [str(i) for i in range(1, 20)]
# print(lst)
# for index in lst:
#     f.write(index + "\t")
# f.close()

# f = open('text2.txt', 'w')
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n")
# f.close()

# f = open('text2.txt', 'r')
# rl = f.readlines()
# f.close()
#
# print(rl)
# rl[1] = "Hello World\n"
# print(rl)
#
# f = open('text2.txt', 'w')
# f.writelines(rl)
# f.close()


# f = open('text2.txt', 'r')
# lst = f.readlines()
# f.close()
#
# pos = int(input("pos = "))
# if 0 <= pos < len(lst):
#     lst.pop(pos)
# else:
#     print("Индекс введен неверно")
# print(lst)
#
# f = open('text2.txt', 'w')
# f.writelines(lst)
# f.close()

# f = open('test.txt', 'r')
# print(f.read(3))  # Hel
# print(f.tell())  # текущая позиция курсора (3)
# print(f.seek(1))  # перемещение курсора (1)
# print(f.read())  # ello!!!!!
# print(f.tell())  # 10
# f.close()

# # f = open('test5.txt', 'r+')  # FileNotFoundError
# f = open('test5.txt', 'w+')
# f1 = open('test6.txt', 'a+')
# f.close()
# f1.close()

# # f = open('test.txt', 'r+')
# f = open('test.txt', 'a+')  # 52 (len)
# # print(f.write("hehe I am "))  # hehe I am ing Python
# print(f.write("I am learning Python"))  # I am learning Python
# print(f.tell())  # 20
# print(f.seek(3))  # 3
# print(f.write("-new string-"))  # 12 (len)
# print(f.tell())  # 3 + 12 => 15
# f.close()

# with open('test.txt', 'w+') as f:
#     print(f.write('01234\n56789'))
#
# with open('test.txt', 'r') as f:
#     for line in f:
#         print(line[:3])  # 012, 567

# file_name = "res_1.txt"
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
#
#
# def get_line(lt):
#     lt = list(map(str, lt))
#     print(lt)
#     return " ".join(lt)
#
#
# with open(file_name, 'w') as f:
#     # f.write(lst)  # TypeError
#     # f.write(str(lst))  # '[4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]'
#     f.write(get_line(lst))
#
#
# with open(file_name, 'r') as f:
#     nums = f.read()
#
# print(nums)
# nums_list = list(map(float, nums.split()))
# print(nums_list)
# print(sum(nums_list))  # 24.607
# print(len(nums_list))  # 7
#
# print("Done!")


# def longest_words(file):
#     with open(file, 'r') as f:
#         w = f.read().split()
#         # max_length = max(w)  # системах.
#         max_length = len(max(w, key=len))  # взаимодействия -> 14
#         print(max_length)  # 14
#         res = [word for word in w if len(word) == max_length]
#         if len(res) == 1:
#             return res[0]  # взаимодействия
#         return res
#
#
# print(longest_words('words.txt'))

# one = 'one.txt'
# two = 'two.txt'

# text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10"
#
# with open(one, 'w') as f:
#     f.write(text)

# with open(one, 'r') as fr, open(two, 'w') as fw:
#     for line in fr:
#         line = line.replace("Строка", "Линия -")
#         fw.write(line)


# -----------------------------------------------------
# Модуль OS и OS.PATH

# import os
# import os.path

# print(os.path.split(r"C:\Users\a_ego\Documents\Python 313\test\nested2\nested3\test1.txt"))

# print(os.getcwd())  # путь к текущей директории
#
# print(os.listdir())  # содержимое текущей директории
#
# print(os.listdir(".."))  # выход на уровень выше
#
# os.mkdir("folder1")  # создание папки

# os.mkdir("nested1/nested2/nested3")  # FileNorFoundError

# os.makedirs("nested1/nested2/nested3")  # создание папки с промежуточными директориями (вложенные папки)

# os.rmdir("folder1")  # удаление папки

# os.remove("xyz.txt")  # удаление файла

# os.rmdir("folder")  # OSError (папка не пуста)

# os.remove("folder/test.txt")
# os.rmdir("folder")

# os.rename("nested1", "test")  # переименование папки

# os.rename("words.txt", "test/words_new.txt")  # переименование и перемещение файла

# os.rename("two.txt", "folder/file.txt")  # FileNotFoundError

# os.renames("two.txt", "folder/file.txt")  # переименование и перемещение файла в НОВУЮ папку

# for root, dirs, files in os.walk('test', topdown=False):
#     print('Root:', root)
#     print('Subdirs:', dirs)
#     print('Files:', files)


# def remove_empty_dirs(root_tree):
#     print(f'Удаление пустых директорий в ветви {root_tree}')
#     print('-' * 50)
#
#     for root, dirs, files in os.walk(root_tree):
#         if not os.listdir(root):
#             os.rmdir(root)
#             print(f'Директория {root} удалена.')
#
#     print('-' * 50)
#
#
# remove_empty_dirs("test")

# print(os.path.split(r"C:\Users\a_ego\Documents\Python 313\test\nested2\nested3\test1.txt")[1])
# # раху (head) и кету (tail) - разбиение пути элемента на последнем /.
# print(os.path.dirname(r"C:\Users\a_ego\Documents\Python 313\test\nested2\nested3\test1.txt"))  # путь
# print(os.path.basename(r"C:\Users\a_ego\Documents\Python 313\test\nested2\nested3\test1.txt"))  # последний элемент

# print(os.path.join(r"C:\Users", "a_ego", "Documents", "Python 313", "test"))  # соединение компонентов пути

# print(os.path.join(r"a_ego", "C:\Users", "Documents", "Python 313", "test"))  # SyntaxError

# dirs = [r'Work\F1', r'Work\F2\F21']
# for d in dirs:
#     os.makedirs(d)
#
# files = {
#     r'Work': ['w.txt'],
#     r'Work\F1': ['f11.txt', 'f12.txt', 'f13.txt'],
#     r'Work\F2\F21': ['f211.txt', 'f212.txt']
# }
# for k, v in files.items():
#     for value in v:
#         file_path = os.path.join(k, value)
#         open(file_path, 'w').close()

# files_with_text = [r'Work\w.txt', r'Work\F1\f12.txt', r'Work\F2\F21\f211.txt', r'Work\F2\F21\f212.txt']
# for file in files_with_text:
#     with open(file, 'w') as f:
#         f.write(f"Some sort of text for a file, located at the destination {file}")

# def print_tree(root, topdown):
#     print(f"Обход {root} {'сверху вниз' if topdown else 'снизу вверх'}")
#     for root, dirs, files in os.walk(root, topdown):
#         print(root)
#         print(dirs)
#         print(files)
#     print("-" * 50)
#
#
# print_tree('Work', False)
# print_tree('Work', True)

# print(os.path.exists(r"C:\Users\a_ego\Documents\Python 313\test\nested2\nested3\test1.txt"))  # True
#
# print(os.path.exists(r"C:\Users\a_ego\Documents\Python 313\test\nested2\nested3"))  # True
#
# print(os.path.exists(r"C:\Users\a_ego\Documents\Python 313\test\nested2\nested3\test_hehe.txt"))  # False
#
# print(os.path.exists(r"C:\Users\a_ego\Documents\Python 313\test\does_not\exist\test1.txt"))  # False
#
# print(os.path.isfile(r"C:\Users\a_ego\Documents\Python 313\test\nested2\nested3\test1.txt"))  # True
#
# print(os.path.isfile(r"C:\Users\a_ego\Documents\Python 313\test\nested2\nested3"))  # не файл - False
#
# print(os.path.isfile(r"C:\Users\a_ego\Documents\Python 313\test\does_not\exist\test1.txt"))  # неверный путь - False
#
# print(os.path.isdir(r"C:\Users\a_ego\Documents\Python 313\test\nested2\nested3\test1.txt"))  # False
#
# print(os.path.isdir(r"C:\Users\a_ego\Documents\Python 313\test\nested2\nested3"))  # True
#
# print(os.path.isfile(r"C:\Users\a_ego\Documents\Python 313\test\does_not\exist"))  # неверный путь - False

# import time
#
# path = "Python_theory.py"
# print(os.path.getsize(path))  # размер файла в байтах

# path = "main.py"
# print(os.path.getsize(path))  # FileNotFoundError

# print(os.path.getsize(path) // 1024)  # размер файла в килобайтах

# print(os.path.getatime(path))  # время последнего доступа к файлу (сек)
# print(os.path.getctime(path))  # время создания файла (сек)
# print(os.path.getmtime(path))  # время последнего изменения файла (сек)

# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(os.path.getatime(path))))  # время последнего доступа к файлу
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(os.path.getctime(path))))  # время
# # создания файла (сек)
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(os.path.getmtime(path))))  # время последнего изменения файла

# file_path = r"test\nested2\nested3\test1.txt"
#
# if os.path.exists(file_path):
#     # head = os.path.dirname(file_path)
#     # tail = os.path.basename(file_path)
#     head, tail = os.path.split(file_path)
#     print(f'{tail} ({head}) - last access time {os.path.getatime(file_path)} sec')
# else:
#     print(f"File {file_path} does not exist")


# -----------------------------------------------------
# Объектно-ориентированное программирование (OOP)
# Инкапсуляция - защита от несанкционированных изменений
# Наследование - возможность создания дочерних классов
# Полиморфизм - возможность разной отработки разных типов данных
# Свойства класса (поля, переменные): статические или динамические
# Методы класса (функции): экземпляры класса (self) или статические () или методы класса (cls)
# self = ссылка на экземпляр класса


# class Point:
#     x = 1
#     y = 3
#
#
# p1 = Point()  # экземпляр класса (instance) -> self
# # print(p1)  # <__main__.Point object at 0x0000022932F05940>
# p1.x = 5
# p1.y = 24
# print(p1.x)  # 1 -> 5
# print(p1.y)  # 3 -> 24
# # print(x)  # NameError: name 'x' is not defined
# print(p1.__dict__)  # {'x': 5, 'y': 24}
# print(id(p1))  # 2032472383200
#
# p2 = Point()
# print(p2.x)  # 1
# print(p2.y)  # 3
# print(p2.__dict__)  # {}
# print(id(p2))  # 2032472383152
#
# print(id(Point))  # 2032469526976
#
# print(isinstance(p1, Point))  # True
# print(isinstance(p2, Point))  # True


# class Point:
#     x = 1
#     y = 1
#
#     def set_coord(self, x, y):
#         self.x = x  # p1.x = 5
#         self.y = y  # p1.y = 24
#         print(self.__dict__)
#
#
# p1 = Point()
# # p1.x = 5
# # p1.y = 24
# # set_coord()  # NameError: name 'set_coord' is not defined
# p1.set_coord(5, 24)  # {'x': 5, 'y': 24}
# # Point.set_coord(p1)  # {'x': 5, 'y': 24}; self -> p1
#
# p2 = Point()
# # p2.x = 10
# # p2.y = 30
# p2.set_coord(10, 30)  # {'x': 10, 'y': 30}


# class Human:
#     name = 'name'
#     birthday = '00.00.0000'
#     phone = '00-00-00'
#     country = 'country'
#     city = 'city'
#     address = 'street, house'
#
#     def print_info(self):
#         print(" Персональные данные ".center(40, "*"))
#         print("Имя:", self.name)
#         print("Дата рождения:", self.birthday)
#         print("Номер телефона:", self.phone)
#         print("Страна:", self.country)
#         print("Город:", self.city)
#         print("домашний адрес:", self.address)
#         print("=" * 40)
#
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.name = first_name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def set_address(self, address):  # устанавливаем новое поле (адрес)
#         self.address = address
#
#     def get_address(self):  # получаем поле (адрес)
#         return self.address
#
#     def set_name(self, name):  # устанавливаем новое поле (имя)
#         self.name = name
#
#     def get_name(self):  # получаем поле (имя)
#         return self.name
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info("Юля", "23.05.1986", "45-46-98", "Россия", "Москва", "Чистопрудный бульвар, 1А",)
# h1.print_info()
# h1.set_address("улица Ленина, 56")
# h1.print_info()
# print(h1.get_address())  # улица Ленина, 56
# h1.set_name("Юлия")
# print(h1.get_name())  # Юлия


# class Person:
#     skill = 10  # статическое свойство
#     # name = ''
#     # surname = ''
#     count = 0
#
#     def __init__(self, name, surname):  # Инициализатор
#         self.name = name  # динамическое свойство / просто свойство
#         self.surname = surname
#         # print("Инициализатор класса", self)
#         Person.count += 1
#
#     # def __del__(self):  # Деструктор
#     #     print("Удаление экземпляра", self)
#     #
#     # def print_info(self):
#     #     # self.name = name
#     #     # self.surname = surname
#     #     print(f'Данные сотрудника: {self.name} {self.surname}')
#     #
#     # def add_skill(self, k):
#     #     self.skill += k
#     #     print(f'Квалификация сотрудника: {self.skill}', end='\n\n')
#
#
# p1 = Person("Виктор", "Резник")
# # p1.print_info()
# # p1.add_skill(3)
# # del p1
# # p1 = 5
# print(p1.count)
#
# p2 = Person("Анна", "Долгих")
# # p2.print_info()
# # p2.add_skill(2)
# print(p2.count)
#
# p3 = Person("Анна", "Долгих")
#
# print(Person.count)  # 2 -> 3
# print(p1.count)  # 2 -> 3


# class Robot:
#     count = 0
#
#     def __init__(self, name):
#         self.name = name
#         print("Инициализация робота:", self.name)
#         Robot.count += 1
#
#     def __del__(self):
#         print(self.name, "выключается!")
#         Robot.count -= 1
#         if Robot.count == 0:
#             print(self.name, "был последним.")
#         else:
#             print("Работающих роботов осталось:", Robot.count)
#
#     def say_hi(self):
#         print("Приветствую! Меня зовут:", self.name)
#
#     # count = 0
#
#
# droid1 = Robot('R2-D2')
# droid1.say_hi()
# print("Численность роботов:", Robot.count)
#
# droid2 = Robot('C-3PO')
# droid2.say_hi()
# print("Численность роботов:", Robot.count)
#
# droid3 = Robot('HP-2PO')
# droid2.say_hi()
# print("Численность роботов:", Robot.count)
#
# print("\nЗдесь роботы могут проделать какую-то работу.\n")
#
# print("Роботы закончили свою работу. Давайте их выключим.")
# del droid1
# del droid2
# del droid3
# print("Численность роботов:", Robot.count)


# class Point:
#     __slots__ = ["__x", "__y", "z"]
#
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         # self.set_coord(x, y)
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         # self.x = x
#         # self.y = y
#
#     def __check_value(c):
#         if isinstance(c, int) or isinstance(c, float):
#             return True
#         return False
#
#     def get_coord(self):  # Получить
#         return self.__x, self.__y
#
#     def set_coord(self, x, y):  # Установить
#         # if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_x(self):
#         return self.__x
#
#     def get_y(self):
#         return self.__y
#
#     def set_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print(f'координата {x} должна быть числом')
#
#     def set_y(self, y):
#         if Point.__check_value(y):
#             self.__y = y
#         else:
#             print(f'координата {y} должна быть числом')
#
#
# p1 = Point(5, 10)
# p1.z = 1
# print(p1.z)  # -> {'_Point__x': 5, '_Point__y': 10, 'z': 1} -> AttributeError
# p1.set_x('asd')
# p1.set_x(20.5)
# p1.set_y('aaa')
# p1.set_y(49)
# print(p1.get_coord())  # (5, 10) -> AttributeError -> (0, 0)
# p1.set_coord(100, "abc")
# print(p1.get_coord())  # (100, 'abc')
# print(p1.__dict__)  # {'x': 5, 'y': 10} -> {'_Point__x': 5, '_Point__y': 10}
# p1.x = 100
# p1.y = "abc"
# print(p1.x, p1.y)  # 100 abc

# print(p1.__dict__)  # {'_Point__x': 5, '_Point__y': 10, 'x': 100, 'y': 'abc'}
# print(Point.__dict__)
# print(p1.get_x())  # 5 -> 5 -> 20.5
# print(p1.get_y())  # 10 -> 10 -> 49

# print(p1._Point__x)  # 5 (Not allowed)
# print(p1._Point__y)  # 10 (Not allowed)

# p1._Point__x = 'asd'
# print(p1.__dict__)  # {'_Point__x': 'asd', '_Point__y': 10}


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __get_x(self):
#         return self.__x
#
#     def __get_y(self):
#         return self.__y
#
#     def __set_x(self, x):
#         self.__x = x
#
#     def __set_y(self, y):
#         self.__y = y
#
#     def __del_x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     x = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# # print(p1.get_x())  # 5 -> AttributeError
# p1.x = 100
# print(p1.x)  # 100
# del p1.x
# print(p1.__dict__)  # {'_Point__x': 100, '_Point__y': 10} -> {'_Point__y': 10}


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, x):
#         if not isinstance(x, (int, float)):
#             raise TypeError("Устанавливаемое значение должно быть числом")
#             # print("Устанавливаемое значение должно быть числом")
#         self.__x = x
#
#     @x.deleter
#     def x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     def __get_y(self):
#         return self.__y
#
#     def __set_y(self, y):
#         self.__y = y
#
#
# p1 = Point(5, 10)
# # print(p1.get_x())  # 5 -> AttributeError
# p1.x = '100'
# print(p1.x)  # 100
# # del p1.x
# print(p1.__dict__)  # {'_Point__x': 100, '_Point__y': 10}


# class KgToPounds:
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             print("Килограммы задаются только числами")
#
#     def to_pounds(self):
#         return self.__kg * 2.205
#
#     def print(self):
#         print(self.__kg, 'кг => ', end='')
#         print(self.to_pounds(), "фунтов")
#
#
# weight = KgToPounds(12)
# weight.print()
#
# weight.kg = 41
# weight.print()
#
# weight.kg = 'десять'
# weight.print()


# class Point:
#     __count = 0
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Point.__count += 1
#
#     @staticmethod
#     def get_count():
#         return Point.__count
#
#     # get_count = staticmethod(get_count)
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
#
# print(Point.get_count())  # AttributeError -> 3
# print(p2.get_count())  # 3


# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#
# print(Change.inc(10), Change.dec(10))  # 11 9


# class Maths:
#     @staticmethod
#     def maximum(*args):
#         if len(args) == 4:
#             return max(args)
#         else:
#             print("Должно быть введено 4 аргумента")
#
#     @staticmethod
#     def minimum(*args):
#         if len(args) == 4:
#             return min(args)
#         else:
#             print("Должно быть введено 4 аргумента")
#
#     @staticmethod
#     def mean(*args):
#         if len(args) == 4:
#             return sum(args) / len(args)
#         else:
#             print("Должно быть введено 4 аргумента")
#
#     @staticmethod
#     def fact(x):
#         for i in range(1, x):
#             x *= i
#         return x
#
#
# print(f'Минимальное число: {Maths.minimum(3, 5, 7, 9)}')
# print(f'Максимальное число: {Maths.maximum(3, 5, 7, 9)}')
# print(f'Среднее арифметическое: {Maths.mean(3, 5, 7, 9)}')
# print(f'Факториал числа: {Maths.fact(5)}')


# from Geometry import sqrt
#
#
# class Area:
#     __count = 0
#
#     @staticmethod
#     def triangle_1(a, b, c):
#         Area.__count += 1
#         p = (a + b + c) / 2
#         return sqrt(p * (p - a) * (p - b) * (p - c))
#
#     @staticmethod
#     def triangle_2(a, h):
#         Area.__count += 1
#         return a * h / 2
#
#     @staticmethod
#     def square(a):
#         Area.__count += 1
#         return a ** 2
#
#     @staticmethod
#     def rectangle(a, b):
#         Area.__count += 1
#         return a * b
#
#     @staticmethod
#     def get_count():
#         return Area.__count
#
#     def print_info(self):
#         print(self, "Hello")
#
#
# square = Area()
# square.print_info()
# square1 = Area()
# Area.print_info(square1)
# print(f'Площадь треугольника по формуле Герона (3,4,5): {square.triangle_1(3, 4, 5)}')
# print(f'Площадь треугольника через основание и высоту (6,7): {square1.triangle_2(6, 7)}')
# print(f'Площадь квадрата (7): {Area.square(7)}')
# print(f'Площадь прямоугольника (2,6): {Area.rectangle(2, 6)}')
# print(f'Количество подсчетов площади: {Area.get_count()}')


# class Date:
#     def __init__(self, day, month, year):
#         self.day = day  # -> 23
#         self.month = month  # -> 10
#         self.year = year  # -> 2024
#
#     @classmethod
#     def from_string(cls, date_as_string):
#         day, month, year = map(int, date_as_string.split("."))
#         date1 = cls(day, month, year)  # date1 = Date(23, 10, 2024)
#         return date1
#
#     @staticmethod
#     def is_date_valid(date_as_string):
#         if date_as_string.count(".") == 2:
#             day, month, year = map(int, date_as_string.split("."))
#             return 0 < day <= 31 and 0 < month <= 12 and year <= 3999
#
#     def string_to_db(self):
#         return f'{self.year}-{self.month}-{self.day}'


# string_date = "23.10.2024"
# day, month, year = map(int, string_date.split("."))
# print(day, month, year)
#
# date = Date(day, month, year)
# print(date.string_to_db())  # 2024-10-23
#
# a = 12
# print("Число" + str(a))

# date2 = Date.from_string('23.10.2024')
# print(date2.string_to_db())  # 2024-10-23
#
# date3 = Date.from_string('25.12.2023')
# print(date3.string_to_db())  # 2023-12-25

# dates = [
#     "30.12.2023",
#     "30-12-2020",
#     "01.01.2024",
#     "12.31.2020"
# ]
#
# for string_date in dates:
#     if Date.is_date_valid(string_date):
#         date = Date.from_string(string_date)
#         print(date.string_to_db())
#     else:
#         print("Неправильная дата или неверный формат строки с датой")


# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     SUFFIX = 'RUB'
#     SUFFIX_USD = 'USD'
#     SUFFIX_EUR = 'EUR'
#
#     def __init__(self, surname, num, percent, value=0):
#         self.surname = surname
#         self.num = num
#         self.percent = percent
#         self.value = value
#         print(f'Счет #{self.num}, принадлежащий {self.surname}, был открыт')
#         print('*' * 50)
#
#     def __del__(self):
#         print('*' * 50)
#         print(f'Счет #{self.num}, принадлежащий {self.surname}, был закрыт')
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def add_money(self, val):
#         self.value += val
#         print(f'{val} {Account.SUFFIX} было успешно добавлено!')
#         self.print_balance()
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f'Состояние счета: {usd_val} {Account.SUFFIX_USD}.')
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.value, Account.rate_eur)
#         print(f'Состояние счета: {eur_val} {Account.SUFFIX_EUR}.')
#
#     def edit_owner(self, new_surname):
#         self.surname = new_surname
#
#     def add_percent(self):
#         self.value += self.value * self.percent
#         print("Проценты были успешно начислены!")
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f'К сожалению, у вас нет {val} {Account.SUFFIX}')
#         else:
#             self.value -= val
#             print(f"{val} {Account.SUFFIX} было успешно снято!")
#         self.print_balance()
#
#     def print_balance(self):
#         print(f'Текущий баланс: {self.value} {Account.SUFFIX}')
#
#     def print_info(self):
#         print('Информация о счете: ')
#         print('-' * 20)
#         print(f'#{self.num}')
#         print(f'Владелец: {self.surname}')
#         self.print_balance()
#         print(f'Проценты: {self.percent:.0%}')
#         print('-' * 20)
#
#
# acc = Account("Долгих", "12345", 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# Account.set_usd_rate(2)
# Account.set_eur_rate(3)
# print()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# acc.edit_owner('Дюма')
# acc.print_info()
# acc.add_percent()
# print()
# acc.withdraw_money(100)
# print()
# acc.withdraw_money(3000)
# print()
# acc.add_money(5000)
# print()
# acc.withdraw_money(3000)
# print()

# import re
#
#
# class UserData:
#     def __init__(self, fio, old, ps, weight):
#         self.fio = fio
#         self.old = old
#         self.password = ps
#         self.weight = weight
#
#     @staticmethod
#     def verify_fio(fio):
#         if not isinstance(fio, str):
#             raise TypeError("Вводимое ФИО должно быть строкой")
#         f = fio.split()
#         if len(f) != 3:
#             raise TypeError("Неверный формат ввода ФИО")
#         letters = "".join(re.findall("[a-zа-яё-]", fio, re.IGNORECASE))  # ВолковИгорьНиколаевич
#         for s in f:
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("При вводе ФИО можно использовать только буквы и символ '-'")
#
#     @staticmethod
#     def verify_old(old):
#         if not isinstance(old, int) or old < 14 or old > 120:  # not 14 < old < 120
#             raise TypeError("Вводимый возраст должен быть целым числом в диапазоне от 14 до 120 лет")
#
#     @staticmethod
#     def verify_weight(w):
#         if not isinstance(w, (int, float)) or w < 20:
#             raise TypeError("Вводимый вес должен выражаться целым или вещественным числом от 20 кг и выше")
#
#     @staticmethod
#     def verify_ps(ps):
#         if not isinstance(ps, str):
#             raise TypeError("Вводимые паспортные данные должны быть выражены строкой")
#         s = ps.split()
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError("Неверный формат вводимых паспортных данных")
#         for p in s:
#             if not p.isdigit():
#                 raise TypeError("Вводимые серия и номер паспорта должны быть числами")
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, old):
#         self.verify_old(old)
#         self.__old = old
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, w):
#         self.verify_weight(w)
#         self.__weight = w
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, ps):
#         self.verify_ps(ps)
#         self.__password = ps
#
#
# p1 = UserData('Волков-Петров Игорь Николаевич', 96, "1234 567890", 80.8)
# # p2 = UserData(456, 26, "1234 567890", 80.8)
# # p3 = UserData('Волков Игорь', 26, "1234 567890", 80.8)
# # p4 = UserData('Волков2 _Игорь Николаевич?', 26, "1234 567890", 80.8)
#
# # p5 = UserData('Волков-Петров Игорь Николаевич', 26.3, "1234 567890", 80.8)
# # p6 = UserData('Волков-Петров Игорь Николаевич', 11, "1234 567890", 80.8)
#
# # p7 = UserData('Волков-Петров Игорь Николаевич', 26, "1234 567890", "fifty")
#
# # p8 = UserData('Волков-Петров Игорь Николаевич', 26, 1234567890, 80.8)
# # p9 = UserData('Волков-Петров Игорь Николаевич', 26, '1234 567 890', 80.8)
# # p10 = UserData('Волков-Петров Игорь Николаевич', 26, '123 4567890', 80.8)
# # p10 = UserData('Волков-Петров Игорь Николаевич', 26, '123 4567890', 80.8)
# # p11 = UserData('Волков-Петров Игорь Николаевич', 26, '123p 56&890', 80.8)
#
# # print(p1.fio)  # Волков-Петров Игорь Николаевич
# p1.fio = "Волков-Петров Игорь Игоревич"
# print(p1.fio)  # Волков-Петров Игорь Игоревич
#
# p1.old = 26  # TypeError
# print(p1.old)
#
# p1.weight = 80.5
# print(p1.weight)  # TypeError
#
# p1.password = "9876 543210"
# print(p1.password)


# class Point:  # class Point(object):
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#
# print(issubclass(Point, object))  # True
# print(issubclass(Point, int))  # False


# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f'({self.__x}, {self.__y})'
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width=1) -> None:
#         self.__sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#         print("Инициализатор базового класса Prop")
#
#     def get_sp(self):
#         return self.__sp
#
#
# class Line(Prop):
#     def __init__(self, *args):
#         # Prop.__init__(self, *args)
#         super().__init__(*args)
#         print("Переопределенный инициализатор Line")
#
#     def draw_line(self) -> None:  # def draw_line(self) -> str:
#         print(f'Рисование линии: {self.get_sp()}, {self._ep}, {self._color}, {self._width}')
#         # return f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}'


# class Rect(Prop):
#     def draw_rect(self) -> None:
#         print(f'Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}')


# line = Line(Point(1, 2), Point(10, 20), 'yellow', 5)
# line.draw_line()
# print(line.get_sp())

# rect = Rect(Point(30, 40), Point(70, 80))
# rect.draw_rect()


# DRY (Don't Repeat Yourself) - принцип "не повторяйся"


# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
#
# class Rectangle(Figure):
#     def __init__(self, width, height, color):
#         self.width = width
#         self.height = height
#         super().__init__(color)
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, w):
#         if isinstance(w, int) and w > 0:
#             self.__width = w
#         else:
#             raise ValueError("Вводимое значение ширины должно быть положительным числом")
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, h):
#         if isinstance(h, int) and h > 0:
#             self.__height = h
#         else:
#             raise ValueError("Вводимое значение высоты должно быть положительным числом")
#
#     def area(self):
#         print(f'The area of a {self.color} rectangle:')
#         return self.__width * self.__height
#
#
# rect = Rectangle(10, 20, 'green')
# print(rect.area())  # -200

# rect.width = -90
# print(rect.area())  # ValueError

# rect.height = -30
# print(rect.area())  # ValueError


# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f'({self.__x}, {self.__y})'
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1) -> None:
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coord(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#
# class Line(Prop):
#     def set_coord(self, sp, ep):
#         if sp.is_int() and ep.is_int():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть целыми числами")
#
#     def draw_line(self):
#         print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#
# class Rect(Prop):
#     def draw_rect(self):
#         print(f'Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#
# line = Line(Point(1, 2), Point(10, 20), "yellow", 5)
# line.draw_line()
#
# line.set_coord(Point(15, 45), Point(100.5, 200))
# line.draw_line()
#
# rect = Rect(Point(30, 40), Point(70, 80))
# rect.draw_rect()
#
# rect.set_coord(Point(15.5, 67), Point('one  hundred', 200))
# rect.draw_rect()


# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def show_rect(self):
#         print(f'Прямоугольник: \nШирина: {self.width} \nВысота: {self.height}')
#
#
# class RectFon(Rect):
#     def __init__(self, width, height, background):
#         self.fon = background
#         super().__init__(width, height)
#
#     def show_rect(self):
#         super().show_rect()
#         print("Фон:", self.fon)
#
#
# class RectBorder(Rect):
#     def __init__(self, width, height, line_width, line_fill, color):
#         super().__init__(width, height)
#         self.line_width = line_width
#         self.line_fill = line_fill
#         self.color = color
#
#     def show_rect(self):
#         super().show_rect()
#         print(f'Ширина контура: {self.line_width} \nТекстура контура: {self.line_fill} \nцвет контура: {self.color}')
#
#
# shape1 = RectFon(400, 200, 'yellow')
# shape1.show_rect()
# print()
# shape2 = RectBorder(600, 300, '1px', 'solid', 'red')
# shape2.show_rect()


# class Vector(list):
#     # def __init__(self, lst):
#     #     super().__init__()
#     #     self.lst = lst
#
#     def __str__(self):
#         return " ".join(map(str, self))
#         # return " ".join(map(str, self.lst))
#
#
# v = Vector([1, 2, 3])
# print(sum(v))  # 6
# print(v)  # [1, 2, 3]
# print(type(v))  # <class '__main__.Vector'>


# -----------------------------------------------------
# Перегрузка методов


# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f'({self.__x}, {self.__y})'
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1) -> None:
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coord(self, sp, ep):
#         if sp.is_int() and ep.is_int():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#
# class Line(Prop):
#     def draw_line(self):
#         print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#     def set_coord(self, sp=None, ep=None):
#         if ep is None:
#             if sp.is_int():
#                 self._sp = sp
#
#         elif sp is None:
#             if ep.is_int():
#                 self._ep = ep
#         else:
#             if sp.is_digit() and ep.is_digit():
#                 self._sp = sp
#                 self._ep = ep
#             else:
#                 print("Координаты должны быть целыми числами")
#
#
# line = Line(Point(1, 2), Point(10, 20), "yellow", 5)
# line.draw_line()
#
# line.set_coord(Point(15, 45), Point(100, 200))
# line.draw_line()
#
# line.set_coord(Point(55, 55))
# line.draw_line()
#
# line.set_coord(ep=Point(90, 20))
# line.draw_line()


# -----------------------------------------------------
# Абстрактные методы


# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f'({self.__x}, {self.__y})'
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1) -> None:
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def draw(self):
#         raise NotImplementedError("В дочернем классе должен быть определен метод draw()")
#
#
# class Line(Prop):
#     def draw(self):
#         print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#
# class Rect(Prop):
#     def draw(self):
#         print(f'Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#
# class Ellipse(Prop):
#     def draw(self):
#         print(f'Рисование эллипса: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#
# figs = list()
# figs.append(Line(Point(0, 0), Point(10, 10)))
# figs.append(Line(Point(10, 10), Point(20, 10)))
# figs.append(Rect(Point(50, 50), Point(100, 100)))
# figs.append(Ellipse(Point(-10, -10), Point(10, 10)))
#
# for i in figs:
#     i.draw()


# -----------------------------------------------------
# Абстрактные классы


# from abc import ABC, abstractmethod
#
#
# class Chess(ABC):  # Абстрактный класс
#     def draw(self):
#         print("Нарисовал шахматную фигуру")
#
#     @abstractmethod
#     def move(self):
#         print("Метод move() в базовом классе")
#
#
# class Queen(Chess):
#     def move(self):
#         super().move()
#         print("Ферзь перемещен на Е2Е4")
#
#
# # q = Chess()  # TypeError (no implementation for abstract method 'move')
# q = Queen()
# q.draw()
# q.move()


# from abc import ABC, abstractmethod
#
#
# class Currency(ABC):
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     @abstractmethod
#     def print_value(self):
#         print(self.value, end=' ')
#
#     def show(self):
#         print(f'= {self.convert_to_rub():.2f} RUB')
#
#
# class Dollar(Currency):
#     rate_to_rub = 74.16
#     SUFFIX = 'USD'
#
#     # def convert_to_rub(self):
#     #     return self.value * Dollar.rate_to_rub
#     #
#     # def print_value(self):
#     #     super().print_value()
#     #     print(Dollar.SUFFIX, end=' ')
#
#
# class Euro(Currency):
#     rate_to_rub = 90.14
#     SUFFIX = 'EUR'
#
#     def convert_to_rub(self):
#         return self.value * Euro.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.SUFFIX, end=' ')
#
#
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# e = [Euro(5), Euro(10), Euro(50), Euro(100)]
#
# d += e
# for elem in e:
#     elem.print_value()
#     elem.show()
#
# d.show()


# -----------------------------------------------------
# Интерфейсы


# from abc import ABC, abstractmethod
#
# class Father(ABC):
#     @abstractmethod
#     def display_1(self):
#         pass
#
#     @abstractmethod
#     def display_2(self):
#         pass
#
#
# class Child(Father):
#     def display_1(self):
#         print('Child')
#
#
# class Grandchild(Child):
#     def display_2(self):
#         print('Grandchild')
#
#
# # one = Father()  # TypeError
# # two = Child()  # TypeError
# three = Grandchild()
# three.display_1()
# three.display_2()


# -----------------------------------------------------
# Вложенные классы, видимость методов
# Видны: статические переменные, staticmethod, classmethod
# Не видны: non-static свойства и методы


# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def static_method():
#         print('Static method')
#
#     def outer_method(self):
#         print('Метод в наружном классе')
#
#     class MyInner:
#         def __init__(self, inner_name, obj):
#             self.inner_name = inner_name
#             self.obj = obj
#
#         def inner_method(self):
#             print('Inner class', MyOuter.age, self.obj.name)
#             MyOuter.static_method()
#             self.obj.outer_method()
#
#
# # out = MyInner()  # NameError
# out = MyOuter('outer')
# inner = out.MyInner('inner', out)
# print(inner.inner_name)
#
# inner.inner_method()


# class Color:
#     def __init__(self):
#         self.name = 'Green'
#         self.lg = self.LightGreen()
#
#     def show(self):
#         print('Name:', self.name)
#
#     class LightGreen:
#         def __init__(self):
#             self.name = 'Light Green'
#
#         def display(self):
#             print('Name:', self.name)
#
#
# outer = Color()
# outer.show()
# # outer.display()  # AttributeError
# outer.lg.display()
#
# g = outer.lg
# g.display()

# class Intern:
#     def __init__(self):
#         self.name = "Smith"
#
#     def display(self):
#         print("Name:", self.name)
#
#
# class Employee:
#     def __init__(self):
#         self.name = "Employee"
#         self.intern = Intern()
#         self.head = self.Head()
#
#     def show(self):
#         print("Name:", self.name)
#
#     class Head:
#         def __init__(self):
#             self.name = "Alba"
#
#         def display(self):
#             print("Name:", self.name)
#
#
# outer = Employee()
# outer.show()
#
# d1 = outer.intern
# d1.display()
#
# d2 = outer.head
# d2.display()


# class Outer:
#     def __init__(self):
#         self.inner = self.Inner()
#
#     def show(self):
#         print('Class Outer')
#
#     class Inner:
#         def __init__(self):
#             self.inner_inner = self.InnerClass()
#
#         def show(self):
#             print('Class Inner')
#
#         class InnerClass:
#             def show(self):
#                 print('Class InnerClass')
#
#
# outer = Outer()
# outer.show()
#
# inner1 = outer.inner
# inner1.show()
#
# inner2 = inner1.inner_inner
# inner2.show()
#
# inner3 = outer.inner.inner_inner
# inner3.show()


# class Computer:
#     def __init__(self):
#         self.name = 'PC001'
#         # self.os = self.OS()
#         # self.cpu = self.CPU()
#
#     class OS:
#         def system(self):
#             return 'Windows 10'
#
#     class CPU:
#         def make(self):
#             return 'Intel'
#
#         def model(self):
#             return 'Core-i7'
#
#
# comp = Computer()
# # my_os = comp.os
# # my_cpu = comp.cpu
#
# print(comp.name)
# print(comp.OS().system())
# print(comp.CPU().make())
# print(comp.CPU().model())


# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):  # По умолчанию (ВСЕГДА) отрабатывает в консоли и со многими объектами
#         return f'{self.__class__}: {self.name}'
#
#     def __str__(self):  # Метод __str__ имеет приоритет над методом __repr__
#         return f'{self.name}'
#
#
# cat = Cat('Пушок')
# print(cat)
#
# cat1 = [Cat('Пушок')]
# print(cat1)


# class Point:
#     def __init__(self, *args):
#         self.__coord = args
#
#     def __len__(self):
#         return len(self.__coord)
#
#
# p = Point(1, 2, 3)
# print(len(p))  # TypeError -> 3


# class Point:
#     __slots__ = ('x', 'y', '__length')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = Geometry.sqrt(x ** 2 + y ** 2)
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, value):
#         self.__length = value
#
#
# p = Point(1, 2)
# print(p.length)
#
# p.length = 20
# print(p.length)


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# pt1 = Point(1, 2)
# pt2 = Point2D(1, 2)
#
# print('pt1 =', pt1.__sizeof__())
# print('pt2 =', pt2.__sizeof__() + pt2.__dict__.__sizeof__())
#
# # print(pt1.__dict__)  # AttributeError
# print(pt2.__dict__)


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point3D(Point):
#     __slots__ = 'z',
#
#     def __init__(self, x, y, z):
#         super().__init__(x, y)
#         self.z = z
#
#
# pt1 = Point(1, 2)
# pt3 = Point3D(10, 20, 25)
#
# pt3.z = 30
# print(pt3.x, pt3.y, pt3.z)


# -----------------------------------------------------
# Множественное наследование


# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name + ' is sleeping')
#
#
# class Pet(Creature):
#     def play(self):
#         print(self.name + ' is playing')
#
#
# class Dog(Animal, Pet):
#     def __init__(self):
#         print('Инициализатор Dog')
#
#     def bark(self):
#         print(self.name + ' is barking')
#
#
# dog = Dog('Buddy')
# dog.bark()
# dog.play()
# dog.sleep()


# class A:
#     def __init__(self):
#         print('Инициализатор класса A')
#
#     def hi(self):
#         print('A')
#
#
# class AA:
#     def __init__(self):
#         print('Инициализатор класса AA')
#
#     def hi(self):
#         print('AA')
#
#
# class B(A):
#     def __init__(self):
#         print('Инициализатор класса B')
#
#     # def hi(self):
#     #     print('B')
#
#
# class C(AA):
#     def __init__(self):
#         print('Инициализатор класса C')
#
#     # def hi(self):
#     #     print('C')
#
#
# class D(B, C):
#     def __init__(self):
#         # super().__init__()
#         C.__init__(self)
#         B.__init__(self)
#         print('Инициализатор класса D')
#
#
# d = D()
# d.hi()
# print(D.mro())  # list
# print(D.__mro__)  # tuple


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f'({self.__x}, {self.__y})'
#
#
# class Styles:
#     def __init__(self, color='red', width=1):
#         print('Инициализатор Styles')
#         self._color = color
#         self._width = width
#
#
# class A:
#     def __init__(self):
#         print("Инициализатор A")
#
#
# class Pos(A):
#     def __init__(self, sp: Point, ep: Point, color='red', width=1):
#         print('Инициализатор Pos')
#         self._sp = sp
#         self._ep = ep
#         # super().__init__(color, width)
#         Styles.__init__(self, color, width)
#
#
# class Line(Pos, Styles):
#     def draw(self):
#         print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#
# l1 = Line(Point(10, 10), Point(100, 100), 'green', 5)
# l1.draw()
# print(Line.mro())


# -----------------------------------------------------
# Классы Миксины - создают дополнительный функционал при множественном наследовании классов


# class Displayer:
#     @staticmethod
#     def display(message):
#         print(message)
#
#
# class LoggerMixin:
#     def log(self, message, filename='logfile.txt'):
#         with open(filename, 'a') as fh:
#             fh.write(message)
#
#     def display(self, message):
#         Displayer.display(message)
#         self.log(message)
#
#
# class MySubClass(LoggerMixin, Displayer):
#     def log(self, message, filename=''):
#         super().log(message, filename='sublog.txt')
#
#
# subclass = MySubClass()
# subclass.display('Строка будет отображаться и запишется в файл')


# class Goods:
#     def __init__(self, name, weight, price):
#         print('Инициализатор Goods')
#         self.name = name
#         self.weight = weight
#         self.price = price
#         super().__init__()
#
#     def print_info(self):
#         print(f'{self.name}, {self.weight}, {self.price}')
#
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         print("Инициализатор MixinLog")
#         MixinLog.ID += 1
#         self.id = MixinLog.ID
#
#     def save_sell_log(self):
#         print(f'{self.id}: товар был продан в 00:00')
#
#
# class NoteBook(Goods, MixinLog):
#     pass
#
#
# n = NoteBook("HP", 1.5, 35000)
# n.print_info()
# n.save_sell_log()
#
# n2 = NoteBook('LTE', 2.0, 48000)
# n2.save_sell_log()


# -----------------------------------------------------
# Перегрузка операторов


# class Clock:
#     DAY = 86400
#
#     def __init__(self, sec):
#         if not isinstance(sec, int):
#             raise TypeError("Секунды должны быть выражены целым числом")
#         self.sec = sec % self.DAY
#
#     def get_format_time(self):
#         s = self.sec % 60
#         n = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f'{Clock.get_form(h)}:{Clock.get_form(n)}:{Clock.get_form(s)}'
#
#     @staticmethod
#     def get_form(x):
#         return str(x) if x > 9 else '0' + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError('Правый операнд должен быть выражен типом данных Clock')
#         return Clock(self.sec + other.sec)
#
#     def __eq__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError('Правый операнд должен быть выражен типом данных Clock')
#         return self.sec == other.sec
#
#     def __ne__(self, other):
#         return not self.__eq__(other)
#
#     def __lt__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError('Правый операнд должен быть выражен типом данных Clock')
#         return self.sec < other.sec
#
#     def __le__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError('Правый операнд должен быть выражен типом данных Clock')
#         return self.sec <= other.sec
#
#     def __gt__(self, other):
#         return not self.__le__(other)
#
#     def __ge__(self, other):
#         return not self.__lt__(other)
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError('Ключ должен быть выражен строкой')
#         if item == 'hour':
#             return (self.sec // 3600) % 24
#         elif item == 'min':
#             return (self.sec // 60) % 60
#         elif item == 'sec':
#             return self.sec % 60
#         return 'Неверный ключ'
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise TypeError('Ключ должен быть выражен строкой')
#         if not isinstance(value, int):
#             raise TypeError('Значение должно быть выражено целым числом')
#
#         s = self.sec % 60
#         n = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         if key == 'hour':
#             self.sec = s + 60 * n + value * 3600
#         if key == 'min':
#             self.sec = s + 60 * value + h * 3600
#         if key == 'sec':
#             self.sec = value + 60 * n + h * 3600
#
#
# c1 = Clock(80000)
# print(c1.get_format_time())
#
# c1['hour'] = 11
# print(c1.get_format_time())
#
# c1['min'] = 25
# print(c1.get_format_time())
#
# c1['sec'] = 150
# print(c1.get_format_time())

# c2 = Clock(100)
# # c2 = 'abc'
# print(c2.get_format_time())

# c4 = Clock(300)
# print(c4.get_format_time())
#
# c3 = c1 + c2 + c4
# print(c3.get_format_time())

# c2 += c1
# print(c2.get_format_time())
#
#
# if c1 == c2:
#     print("Время одно")
# else:
#     print("Время разное")
#
# if c1 != c2:
#     print("Время разное")
# else:
#     print("Время одно")
#
# print(f'c2 > c1 {c2 > c1}')
# print(f'c2 >= c1 {c2 >= c1}')
# print(f'c2 < c1 {c2 < c1}')
# print(f'c2 <= c1 {c2 <= c1}')


# class Student:
#     def __init__(self, name, *marks):
#         self.name = name
#         self.marks = list(marks)
#
#     def __getitem__(self, item):
#         if 0 <= item <= len(self.marks):
#             return self.marks[item]
#         else:
#             raise IndexError("Неверно введено значение индекса")
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, int) or key < 0:
#             raise TypeError('Индекс должен быть выражен целым неотрицательным числом')
#         if key > len(self.marks):
#             off = key + 1 - len(self.marks)
#             self.marks.extend([None] * off)
#         self.marks[key] = value
#
#     def __delitem__(self, key):
#         if not isinstance(key, int):
#             raise TypeError('Индекс должен быть выражен целым числом')
#         # if not 0 <= key <= len(self.marks):
#         if key not in range(len(self.marks)):
#             raise IndexError('Индекс находится за пределами допустимого диапазона значений')
#         del self.marks[key]
#
#
# s1 = Student('Сергей', 5, 5, 3, 4, 5)
# # print(s1.name)
# # print(s1.marks[2])
# print(s1[2])
#
# s1[10] = 4
# print(s1.marks)
#
# del s1[2]
# print(s1.marks)


# from random import choice, randint
#
#
# class Cat:
#     def __init__(self, name, age, pol):
#         self.name = name
#         self.age = age
#         self.pol = pol
#
#     def __str__(self):
#         if self.pol == 'M':
#             return f'{self.name} is a good boy!!!'
#         elif self.pol == 'F':
#             return f'{self.name} is a good girl!!!'
#         else:
#             return f'{self.name} is a good kitten!!!'
#
#     def __repr__(self):
#         return f"Cat(name='{self.name}', age={self.age}, pol='{self.pol}')"
#
#     def __add__(self, other):
#         if (self.pol == 'M' and other.pol == 'F') or (self.pol == 'F' and other.pol == 'M'):
#             return [Cat('No name', 0, choice(['M', 'F'])) for _ in range(randint(1, 5))]
#         else:
#             raise TypeError('Unsupported types are crossed')
#
#
# cat1 = Cat('Tom', 4, 'M')
# cat2 = Cat('Elsa', 5, 'F')
# cat3 = Cat('Murzik', 4, 'M')
#
# print(cat1)
# print(cat2)
# print(cat3)
#
# print(cat1 + cat2)


# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_perimetr(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_perimetr(self):
#         return 4 * self.a
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_perimetr(self):
#         return self.a + self.b + self.c
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
#
# s1 = Square(10)
# s2 = Square(20)
#
# t1 = Triangle(1, 2, 3)
# t2 = Triangle(4, 5, 6)
#
# shape = [r1, r2, s1, s2, t1, t2]
# for g in shape:
#     print(g.get_perimetr())


# -----------------------------------------------------
# Функторы


# class Counter:
#     def __init__(self):
#         self.__count = 0
#
#     def __call__(self, *args, **kwargs):
#         self.__count += 1
#         print(self.__count)
#
#
# c1 = Counter()
# c1()  # 1
# c1()  # 2
# c1()  # 3
#
# c2 = Counter()
# c2()  # 1
#
# c1()  # 4


# class StripChars:
#     def __init__(self, chars):
#         self.__chars = chars
#
#     def __call__(self, *args, **kwargs):
#         if not isinstance(args[0], str):
#             raise TypeError("Вводимый аргумент должен быть выражен строкой")
#         return args[0].strip(self.__chars)
#
#
# s1 = StripChars("?:!.; ")
# print(s1(" He?llo World!  "))
# # print(s1(50))


# def strip_chars(chars):
#     def wrap(string):
#         if not isinstance(string, str):
#             raise TypeError("Вводимый аргумент должен быть выражен строкой")
#         return string.strip(chars)
#
#     return wrap
#
#
# s2 = strip_chars("?:!.; ")
# print(s2(" He?llo World!  "))


# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self):
#         print('Перед вызовом функции')
#         self.func()
#         print('После вызова функции')
#
#
# @MyDecorator
# def function():
#     print("Текст функции")
#
#
# function()


# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, x, y):
#         return f'Перед вызовом функции \n{self.func(x, y)} \nПосле вызова функции'
#
#
# @MyDecorator
# def function(a, b):
#     return a * b
#
#
# print(function(2, 5))


# class Power:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, a, b):
#         return self.func(a, b) ** 2
#
#
# @Power
# def function(a, b):
#     return a * b
#
#
# print("Результат:", function(2, 3))


# class MyDecorator:
#     def __init__(self, arg):
#         self.name = arg
#
#     def __call__(self, func):
#         def wrap(*args, **kwargs):
#             return f'Перед вызовом функции ({self.name})\n{func(*args, **kwargs)} \nПосле вызова функции ({self.name})'
#
#         return wrap
#
#
# @MyDecorator("два параметра")
# def function(a, b):
#     return a * b
#
#
# @MyDecorator("три параметра")
# def function1(a, b, c):
#     return a * b * c
#
#
# print(function(2, 5))
# print(function1(2, 5, 2))


# class Power:
#     def __init__(self, arg):
#         self.power = arg
#
#     def __call__(self, func):
#         def wrap(*args, **kwargs):
#             return f'Результат: {func(*args, **kwargs) ** self.power}'
#
#         return wrap
#
#
# @Power(3)
# def function(a, b):
#     return a * b
#
#
# print(function(2, 2))


# -----------------------------------------------------
# Декорирование методов


# def dec(fn):
#     def wrap(*args, **kwargs):
#         print("*" * 20)
#         fn(*args, **kwargs)
#         print("*" * 20)
#
#     return wrap
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     @dec
#     def info(self):
#         print(f'{self.name} {self.surname}')
#
#
# p1 = Person("Виталий", "Карасев")
# p1.info()


# def decorator(cls):
#     class Wrapper(cls):
#         def doubler(self, value):
#             return value * 2
#
#     return Wrapper
#
#
# @decorator
# class ActualClass:
#     def __init__(self):
#         print("Инициализатор класса ActualClass")
#
#     def quad(self, value):
#         return value * 4
#
#
# obj = ActualClass()
# print(obj.quad(4))
# print(obj.doubler(4))


# -----------------------------------------------------
# Дескрипторы (__get__, __set__, __delete__, __set_name__)


# class String:
#     def __init__(self, value=None):
#         print("Инициализатор String:", value)
#         if value:
#             self.set(value)
#
#     def set(self, value):
#         if not isinstance(value, str):
#             raise TypeError(f"{value} должно быть строкой")
#         self.__value = value
#
#     def get(self):
#         return self.__value
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = String(name)
#         self.surname = String(surname)
#
#     # @property
#     # def name(self):
#     #     return self.__name
#     #
#     # @name.setter
#     # # def name(self, value):
#     #     if not isinstance(value, str):
#     #         raise TypeError(f"{value} должно быть строкой")
#     #     self.__name = value
#     #
#     # @property
#     # def surname(self):
#     #     return self.__surname
#     #
#     # @surname.setter
#     # def surname(self, value):
#     #     if not isinstance(value, str):
#     #         raise TypeError(f"{value} должно быть строкой")
#     #     self.__surname = value
#
#
# p = Person("Ivan", "Petrov")
# p.name.set("Harry")
# p.surname.set("Potter")
# print(p.name.get())
# print(p.surname.get())


# class ValidString:
#     def __set_name__(self, owner, name):
#         # print(owner)  # класс
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         # print(instance)  # экземпляр класса
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise TypeError(f"{self.__name} должно быть выражено строкой")
#         instance.__dict__[self.__name] = value
#
#
# class Person:
#     name = ValidString()
#     surname = ValidString()
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#
# p = Person("Ivan", "Petrov")
# print(p.name)
# print(p.surname)
# print(p.__dict__)
#
# p.name = "Harry"
# p.surname = "Potter"
# print(p.__dict__)


# class ValidValue:
#     @staticmethod
#     def verify_coord(coord):
#         if not isinstance(coord, int):
#             raise TypeError(f"Координата {coord} должна быть выражена целочисленным значением")
#
#     def __set_name__(self, owner, name):
#         self.__name = "_" + name
#
#     def __get__(self, instance, owner):
#         # return instance.__dict__[self.__name]
#         return getattr(instance, self.__name)
#
#     def __set__(self, instance, value):
#         self.verify_coord(value)
#         # instance.__dict__[self.__name] = value
#         setattr(instance, self.__name, value)
#
#
# class Point3D:
#     x = ValidValue()
#     y = ValidValue()
#     z = ValidValue()
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#
# p1 = Point3D(1, 2, 3)
# p1.x = 20
# print(p1.x)
# print(p1.__dict__)


# -----------------------------------------------------
# Метаклассы - классы, создающие другие классы

# a = 5
# print(type(a))  # int
# print(type(int))  # type


# class MyList(list):
#     def get_length(self):
#         return len(self)
#
#
# lst = MyList()
# lst.append(5)
# lst.append(8)
# print(lst, lst.get_length())
#
#
# MyList1 = type(
#     "MyList1",
#     (list, ),
#     dict(get_length=lambda self: len(self))
# )
#
#
# lst1 = MyList1()
# lst1.append(5)
# lst1.append(8)
# print(lst1, lst1.get_length())
#
# print(MyList.__dict__)
# print(MyList1.__dict__)


# import Geometry.rect
# import Geometry.sq
# import Geometry.trian

# from Geometry import rect, sq, trian

# from Geometry import *

# print('Hello')
#
#
# def run():
#     r1 = rect.Rectangle(1, 2)
#     r2 = rect.Rectangle(3, 4)
#
#     s1 = sq.Square(10)
#     s2 = sq.Square(20)
#
#     t1 = trian.Triangle(1, 2, 3)
#     t2 = trian.Triangle(4, 5, 6)
#
#     shape = [r1, r2, s1, s2, t1, t2]
#
#     for g in shape:
#         print(g.get_perimetr())
#
#
# if __name__ == '__main__':
#     run()


# from Car.electrocar import ElectroCar
#
# e_car = ElectroCar('Tesla', 'T', 2018, 99000)
# e_car.show_car()
# e_car.description_battery()


# class PayrollSystem:
#     def calculate(self, employees):
#         print("Расчет заработной платы:")
#         print("*" * 50)
#         for employee in employees:
#             print(f"Заработная плата: {employee.id} - {employee.name}")
#             print(f"- Проверить сумму: {employee.calculate_payroll()}")
#             print()
#
#
# class Employee:
#     def __init__(self, id_employee, name):
#         self.id = id_employee
#         self.name = name
#
#
# class SalaryEmployee(Employee):
#     """Административные работники с фиксированной зарплатой"""
#
#     def __init__(self, id_employee, name, weekly_salary):
#         super().__init__(id_employee, name)
#         self.weekly_salary = weekly_salary
#
#     def calculate_payroll(self):
#         return self.weekly_salary
#
#
# class HourlyEmployee(Employee):
#     """Сотрудники с почасовой оплатой"""
#
#     def __init__(self, id_employee, name, hours_worked, hour_rate):
#         super().__init__(id_employee, name)
#         self.hours_worked = hours_worked
#         self.hour_rate = hour_rate
#
#     def calculate_payroll(self):
#         return self.hours_worked * self.hour_rate
#
#
# class CommissionEmployee(SalaryEmployee):
#     """Торговые представители, получающие фиксированную оплату и комиссию сверху"""
#
#     def __init__(self, id_employee, name, weekly_salary, commission):
#         super().__init__(id_employee, name, weekly_salary)
#         self.commission = commission
#
#     def calculate_payroll(self):
#         return self.weekly_salary + self.commission
#
#
# salary_employee = SalaryEmployee(1, "Валерий Задорожный", 1500)
# hourly_employee = HourlyEmployee(2, "Илья Кронин", 40, 15)
# commission_employee = CommissionEmployee(3, "Николай Хорольский", 1100, 150)
#
# payroll_system = PayrollSystem()
# payroll_system.calculate([
#     salary_employee,
#     hourly_employee,
#     commission_employee
# ])
