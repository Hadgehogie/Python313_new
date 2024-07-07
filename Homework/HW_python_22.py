# Обмен местами двух строк в файле:

test = 'test_file.txt'

with open(test, 'w') as file:
    file.write("""Замена строки в текстовом файле; 
изменить строку в списке; 
записать список в файл; 
""")

with open(test, 'r') as file:
    list_lines = file.readlines()
    lines = len(list_lines)

with open(test, 'w') as file:
    one = int(input("pos1 = "))
    two = int(input("pos2 = "))
    if 0 <= one < lines and 0 <= one < lines:
        list_lines[one], list_lines[two] = list_lines[two], list_lines[one]
        file.writelines(list_lines)
    else:
        print("Ошибка ввода индексов строк в списке. Пожалуйста, обновите страницу и повторите попытку")
