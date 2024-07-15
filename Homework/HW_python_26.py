# Создать класс Rectangle, описывающий прямоугольник.
# В классе должны быть все необходимые методы, а также методы вычисления площади, периметра, диагонали и метод,
# который рисует прямоугольник

class Rectangle:
    def __init__(self, a=3, b=9):
        self.__a = a
        self.__b = b

    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

    @staticmethod
    def area(a, b):
        return a * b

    @staticmethod
    def perimeter(a, b):
        return (a + b) * 2

    @staticmethod
    def hypotenuse(a, b):
        from math import sqrt
        return round(sqrt(a ** 2 + b ** 2), 2)

    @staticmethod
    def model(a, b):
        figure = ''
        for i in range(a):
            for j in range(b):
                figure += '*'
            figure += '\n'
        return figure
        

this = Rectangle(3, 9)
print("Длина прямоугольника:", this.a)
print("Ширина прямоугольника:", this.b)
print("Площадь прямоугольника:", Rectangle.area(this.a, this.b))
print("Периметр прямоугольника:", Rectangle.perimeter(this.a, this.b))
print("Диагональ прямоугольника:", Rectangle.hypotenuse(this.a, this.b))
print(Rectangle.model(3, 9))
