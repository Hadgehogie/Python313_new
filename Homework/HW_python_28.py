# Создайте базовый класс "Стол" и дочерние: "Прямоугольные столы" и "Круглые столы". Через инициализатор базового
# класса передавайте размер поверхности стола: для прямоугольного - ширина и длина, для круглого - радиус. В дочерних
# классах реализуйте метод вычисления площади поверхности стола.

class Table:
    def __init__(self, width=None, height=None, radius=None):
        if radius is None:
            if height is None:
                self._width = width
                self._width = height
            elif width is None:
                self._height = width
                self._height = height
            else:
                self._width = width
                self._height = height
        else:
            self._radius = radius

    def area(self):
        raise NotImplementedError("Метод area() должен быть определен во всех дочерних классах")


class Edged(Table):
    def area(self):
        print(f'Площадь стола: {self._width * self._height}')


class Round(Table):
    PI = 3.14

    def area(self):
        print(f'Площадь стола: {self._radius ** 2 * Round.PI}')


table1 = Edged(20, 10)
print(table1.__dict__)
table1.area()

table2 = Edged(20, 20)
print(table2.__dict__)
table2.area()

table3 = Round(0, 0, 20)
print(table3.__dict__)
table3.area()
