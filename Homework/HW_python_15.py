# Создать лямбда-выражения для нахождения площадей фигур

from Geometry import pi

area = {
    'circle': lambda r: pi * (r ** 2),
    'rectangle': lambda x, y: x * y,
    'trapezoid': lambda a, b, h: (a + b) / 2 * h
}

print("Площадь окружности:", area['circle'](2))
print("Площадь прямоугольника:", area['rectangle'](10, 13))
print("Площадь трапеции:", area['trapezoid'](7, 5, 3))
