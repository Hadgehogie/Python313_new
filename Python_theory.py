# -----------------------------------------------------
# Введение
# import random
import random

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
# import math

# import math
#
# num1 = math.sqrt(121)  # 11.0
# num2 = math.ceil(3.1)  # Округление в верхнюю сторону
# num3 = math.floor(3.8)  # Округление в нижнюю сторону
#
# print(num1)
# print(num2)
# print(num3)
# print(math.pi)

# import math as m  # from math import *
# from math import sqrt, ceil
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

