# Дана таблица (изображение zip.jpeg). Используя функцию zip(), найдите чистую прибыль по месяцам.

mon = ['January', 'February', 'March']
total = [52000.00, 51000.00, 48000.00]
prod_cost = [46800.00, 45900.00, 43200.00]

a = list(zip(mon, total, prod_cost))
for i in a:
    i = list(i)
    profit = i[1] - i[2]
    print("Чистая прибыль в", i[0], "=", profit)
