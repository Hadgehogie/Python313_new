# Выведите статистику частности символов в кортеже:

num = input("Введите по порядку, без пробелов, элементы кортежа: ")

tpl = tuple(num)
print(tpl)

lst = []
for x in tpl:
    if x in lst:
        pass
    else:
        lst.append(x)
        print("Количество", x, "=", tpl.count(x))
