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
