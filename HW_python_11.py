# Посчитайте гласные буквы в строке

a = input("Введите строку: ")
vowels = {"А", "а", "О", "о", "У", "у", "ы", "Э", "э", "Я", "я", "Ё", "ё", "Ю", "ю", "И", "и", "Е", "е"}
quant = 0
for i in a:
    if i in vowels:
        quant += 1
print("Количество гласных равно:", quant)
