# Напишите класс Point3D для хранения координат в трехмерном пространстве (x, y, z). Реализуйте перегрузку операторов
# сложения, вычитания, умножения и деления для этого класса. Также сделайте возможность сравнения координат между
# собой и запись/считывание значений через ключи: "x", "y", "z."


class Point3D:
    count = 0
    DESCR = "Второй операнд должен являться экземпляром класса Point3D"
    INT = 'Вводимые координаты должны быть целыми числами'
    KEY = "Вводимое значение ключа должно быть строкой"

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        Point3D.count += 1

    def __str__(self):
        return f'Координаты {Point3D.count}-й точки: {self.x}, {self.y}, {self.z}'

    def __add__(self, other):
        if not isinstance(other, Point3D):
            raise TypeError(self.DESCR)
        if not isinstance(self.x, int) or not isinstance(self.y, int) or not isinstance(self.z, int):
            raise TypeError(self.INT)
        return f'Сложение координат: {self.x + other.x, self.y + other.y, self.z + other.z}'

    def __sub__(self, other):
        if not isinstance(other, Point3D):
            raise TypeError(self.DESCR)
        if not isinstance(self.x, int) or not isinstance(self.y, int) or not isinstance(self.z, int):
            raise TypeError(self.INT)
        return f'Вычитание координат: {self.x - other.x, self.y - other.y, self.z - other.z}'

    def __mul__(self, other):
        if not isinstance(other, Point3D):
            raise TypeError(self.DESCR)
        if not isinstance(self.x, int) or not isinstance(self.y, int) or not isinstance(self.z, int):
            raise TypeError(self.INT)
        return f'Вычитание координат: {self.x * other.x, self.y * other.y, self.z * other.z}'

    def __truediv__(self, other):
        if not isinstance(other, Point3D):
            raise TypeError(self.DESCR)
        if not isinstance(self.x, int) or not isinstance(self.y, int) or not isinstance(self.z, int):
            raise TypeError(self.INT)
        return f'Вычитание координат: {self.x / other.x, self.y / other.y, self.z / other.z}'

    def __eq__(self, other):
        if not isinstance(other, Point3D):
            raise TypeError(self.DESCR)
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other):
        return not self.__eq__(other)

    def __getitem__(self, item):
        if not isinstance(item, str):
            raise TypeError(self.KEY)
        if item == 'x':
            return self.x
        elif item == 'y':
            return self.y
        elif item == 'z':
            return self.z
        return 'Неверное значение ключа'

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError(self.KEY)
        if not isinstance(value, int):
            raise TypeError(self.INT)
        if key == 'x':
            self.x = value
        elif key == 'y':
            self.y = value
        elif key == 'z':
            self.z = value
        else:
            print('Неверно введены ключ и/или новое значение')


one = Point3D(12, 15, 18)
print(one)

two = Point3D(6, 3, 9)
print(two)

print(one + two)
print(one - two)
print(one * two)
print(one / two)

print(f'Равенство координат: {one == two}')

print(f"x = {one['x']} x1 = {two['x']}")
print(f"y = {one['y']} y1 = {two['y']}")
print(f"z = {one['z']} z1 = {two['z']}")

one['x'] = 20
one['y'] = 20
one['z'] = 20
print(one)