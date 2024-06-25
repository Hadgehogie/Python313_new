# Создать функцию, которая будет находить сумму любого количества чисел. Создать декоратор, который будет находить
# среднее арифметическое этих чисел

def mean(fn):
    def wrap(*args):
        ar_mean = sum(args) / len(args)
        print('Сумма чисел: ', fn(*args), '\n', 'Среднее арифметическое чисел: ', ar_mean, sep='')
    return wrap


@mean
def summa(*args):
    return sum(args)


summa(2, 3, 3, 4)
