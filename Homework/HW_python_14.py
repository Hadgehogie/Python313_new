# Пользователь вводит данные о количестве студентов, их имена и балл для каждого.
# Программа должна определить средний балл и вывести имена студентов, чей балл выше среднего.

quant = int(input("Количество студентов: "))
d = {}
for i in range(1, quant + 1):
    name = input(str(i) + '-й студент: ')
    point = int(input("Балл: "))
    d.update({name: point})

mean = round(sum(d.values()) / len(d))
print("Средний балл:", round(sum(d.values()) / len(d)))

lst = []
for k, v in d.items():
    if v > mean:
        lst.append(k)

print("Студенты с баллом выше среднего: ")
for i in range(len(lst)):
    print(lst[i])
