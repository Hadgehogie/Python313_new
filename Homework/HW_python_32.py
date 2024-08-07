# Создать дескриптор класса Order, который задает имя товара, его цену и количество. В дескрипторе должна быть
# реализована проверка на ввод положительных значений цены и количества товара.


class ValidString:
    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f"{self.__name} должно быть строкой")
        instance.__dict__[self.__name] = value


class ValidValue:
    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"{self.__name} должно быть положительными целым числом")
        instance.__dict__[self.__name] = value


class Order:
    name = ValidString()
    price = ValidValue()
    count = ValidValue()

    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count

    def cost(self):
        return self.price * self.count

    def print_info(self):
        print(f'Стоимость товара "{self.name}" составляет {self.cost()}')


test = Order('apples', 5, 10)
test.print_info()

test.name = 'oranges'
test.price = 7
test.count = 20
test.print_info()

# test.name = 79
# test.price = 'eight'
# test.count = -9
