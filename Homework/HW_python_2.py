# Напишите программу, которая запрашивает у пользователя номер месяца и затем выводит соответствующее название
# времени года.
# В Случае, если пользователь введет недопустимое число, программа должна вывести сообщение "Ошибка ввода данных".

a = int(input("Введите номер месяца: "))
if a == 12 or a == 1 or a == 2:
    print("Зима")
elif 3 <= a <= 5:
    print("Весна")
elif 6 <= a <= 8:
    print("Лето")
elif 9 <= a <= 11:
    print("Осень")
else:
    print("Ошибка ввода данных")
