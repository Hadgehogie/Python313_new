# Реализуйте класс "Автомобиль". Необходимо хранить в полях класса: название модели, год выпуска, производителя,
# мощность двигателя, цвет машины, цену. Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ
# к отдельным полям через методы класса.

class Automobile:

    def __init__(self, model, year, manufacturer, power, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.power = power
        self.color = color
        self.price = price

    def print_info(self):
        print(" Данные автомобиля ".center(40, "*"))
        print(f'Название модели: {self.model} \nГод выпуска: {self.year} \nПроизводитель: {self.manufacturer} '
              f'\nМощность двигателя: {self.power} \nЦвет машины: {self.color} \nЦена: {self.price}')
        print("=" * 40)

    def set_model(self, model):
        self.model = model

    def get_model(self):
        return self.model

    def year(self, year):
        self.year = year

    def get_year(self):
        return self.year

    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def get_manufacturer(self):
        return self.manufacturer

    def set_power(self, power):
        self.power = power

    def get_power(self):
        return self.power

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price


a1 = Automobile("X7 M501", "2021", "BMW", "530 л.с.", "white", "10790000")
a1.print_info()

a1.set_color('white')
a1.set_price('10810000')
a1.set_power('600 л.с.')

a1.print_info()

print(a1.get_color())
print(a1.get_price())
print(a1.get_power())
