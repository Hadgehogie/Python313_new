# Даны два числа: a = 122 и b = 97, где и - коды символов. Ваша задача = вывести все символы, ASCII-коды которых лежат
# между a и b включительно, в порядке возрастания их кодов.

a = 122
b = 97


def decor(fn):
    def wrap(arg1, arg2):
        for i in fn(arg1, arg2):
            print(i, end=' ')

    return wrap


@decor
def code(x, y):
    lst = []
    if x > y:
        lst += [chr(i) for i in range(a, b - 1, -1)]
    if x < y:
        lst += [chr(i) for i in range(a, b + 1)]
    lst.sort()

    return lst


code(a, b)


# if a > b:
#     lst = [chr(i) for i in range(a, b - 1, -1)]
#     lst.sort()
#     for i in lst:
#         print(i, end=' ')
#
# if b > a:
#     lst = [chr(i) for i in range(a, b + 1)]
#     lst.sort()
#     for i in lst:
#         print(i, end=' ')
