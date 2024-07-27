import re


class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    SUFFIX = 'RUB'
    SUFFIX_USD = 'USD'
    SUFFIX_EUR = 'EUR'

    def __init__(self, surname, num, percent, value=0):
        self.verify_surname(surname)
        self.verify_num(num)
        self.verify_percent(percent)
        self.verify_value(value)

        self.surname = surname
        self.num = num
        self.percent = percent
        self.value = value
        print(f'Счет #{self.num}, принадлежащий {self.surname}, был открыт')
        print('*' * 50)

    def __del__(self):
        print('*' * 50)
        print(f'Счет #{self.num}, принадлежащий {self.surname}, был закрыт')

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    def get_surname(self):
        return self.surname

    def set_surname(self, surname):
        self.verify_surname(surname)
        self.surname = surname

    def get_num(self):
        return self.num

    def set_num(self, num):
        self.verify_num(num)
        self.num = num

    def get_percent(self):
        return self.percent

    def set_percent(self, percent):
        self.verify_percent(percent)
        self.percent = percent

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.verify_value(value)
        self.value = value

    @staticmethod
    def convert(value, rate):
        return value * rate

    @staticmethod
    def verify_surname(surname):
        if not isinstance(surname, str):
            raise TypeError("Вводимая фамилия должна быть строкой")
        letters = "".join(re.findall('[a-zа-яё-]', surname, re.IGNORECASE))
        if len(surname.strip(letters)) != 0:
            raise TypeError("При вводе ФИО можно использовать только буквы и символ '-'")

    @staticmethod
    def verify_num(num):
        if not isinstance(num, str):
            raise TypeError("Вводимый номер счёта должен быть строкой")
        if not num.isdigit():
            raise ValueError("Вводимый номер счёта должен быть числом")

    @staticmethod
    def verify_percent(per):
        if not isinstance(per, float):
            raise TypeError("Вводимый процент должен быть вещественным числом")
        if not 0 < per < 1:
            raise ValueError("Вводимый процент должен быть выражен десятичной дробью больше 0 и меньше 1")

    @staticmethod
    def verify_value(val):
        if not isinstance(val, int):
            raise TypeError("Вводимое количество средств должно быть целым числом")
        if val <= 0:
            raise ValueError("Вводимое количество средств не может быть отрицательным или равным 0")

    def add_money(self, val):
        self.value += val
        print(f'{val} {Account.SUFFIX} было успешно добавлено!')
        self.print_balance()

    def convert_to_usd(self):
        usd_val = Account.convert(self.value, Account.rate_usd)
        print(f'Состояние счета: {usd_val} {Account.SUFFIX_USD}.')

    def convert_to_eur(self):
        eur_val = Account.convert(self.value, Account.rate_eur)
        print(f'Состояние счета: {eur_val} {Account.SUFFIX_EUR}.')

    def print_balance(self):
        print(f'Текущий баланс: {self.value} {Account.SUFFIX}')

    def edit_owner(self, new_surname):
        self.surname = new_surname

    def add_percent(self):
        self.value += self.value * self.percent
        print("Проценты были успешно начислены!")
        self.print_balance()

    def withdraw_money(self, val):
        if val > self.value:
            print(f'К сожалению, у вас нет {val} {Account.SUFFIX}')
        else:
            self.value -= val
            print(f"{val} {Account.SUFFIX} было успешно снято!")
        self.print_balance()

    def print_info(self):
        print('Информация о счете: ')
        print('-' * 20)
        print(f'#{self.num}')
        print(f'Владелец: {self.surname}')
        self.print_balance()
        print(f'Проценты: {self.percent:.0%}')
        print('-' * 20)


acc = Account("Долгих", "12345", 0.03, 1000)
# acc1 = Account("Долгих28", "12345", 0.03, 1000)
# acc2 = Account("Долгих", "12hello345", 0.03, 1000)
# acc3 = Account("Долгих", "12345", 1.09, 1000)
# acc4 = Account("Долгих", "12345", 0.03, -1000)

acc.surname = "Петров"
print(acc.surname)

acc.num = "8800555353"
print(acc.num)

acc.percent = 0.16
print(acc.percent)

acc.value = 6789
print(acc.value)
