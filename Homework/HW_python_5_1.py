# Найти среднее арифметическое всех ненулевых элементов введенного списка

a = [(int(input("-> "))) for i in range(int(input("n = ")))]
b = list()
summa = quan = 0
for i in a:
    if i != 0:
        summa += i
        quan += 1
mean = summa / quan
print("Среднее арифметическое: ", mean)
