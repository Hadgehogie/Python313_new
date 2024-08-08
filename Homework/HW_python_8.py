# Напишите функции нахождения площади фигур:

def rectangle(x, y):
    return x * y


def triangle(x, y):
    return x * y / 2


def circle(x):
    from Geometry import pi
    return pi * x ** 2


choice = int(input("1 - прямоугольник, 2 - треугольник, 3 - круг: "))
if choice == 1:
    a = int(input("Длина: "))
    b = int(input("Ширина: "))
    print("Площадь:", rectangle(a, b))
elif choice == 2:
    a = int(input("Основание: "))
    h = int(input("Высота: "))
    print("Площадь:", triangle(a, h))
elif choice == 3:
    r = int(input("Радиус: "))
    n = int(input("Количество знаков после запятой при округлении: "))
    print("Площадь:", round(circle(r), n))
else:
    print("Ошибка ввода данных, попробуйте еще раз")
    choice = int(input("1 - прямоугольник, 2 - треугольник, 3 - круг: "))
