# Дан список. Выведите те его элементы, которые встречаются в списке только один раз. Элементы нужно вводить в том
# порядке, в котором они встречаются в списке.

# a = [1, 5, 3, 4, 2, 3, 7, 5, 8, 9]
# for i in a:
#     num = a.count(i)
#     if num == 1:
#         print(i, end=' ')

a = [1, 5, 3, 4, 2, 3, 7, 5, 8, 9]
b = []
for i in a:
    if i in b:
        b.remove(i)
    else:
        b.append(i)
print(b)
for j in range(len(b)):
    print(b.pop(j), end=' ')
    b.insert(0, 0)
