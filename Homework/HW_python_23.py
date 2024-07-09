# Напишите программу, которая просканирует выбранную директорию и для всех следующую информацию на экран:
# имя - тип - размер (только для файлов)
# * Типы объектов: файл, директория
# * Размер: только для файлов

import os

# dirs = [r'Work\F1', r'Work\F2\F21']
# for d in dirs:
#     os.makedirs(d)
#
# files = {
#     r'Work': ['w.txt'],
#     r'Work\F1': ['f11.txt', 'f12.txt', 'f13.txt'],
#     r'Work\F2\F21': ['f211.txt', 'f212.txt']
# }
# for k, v in files.items():
#     for value in v:
#         file_path = os.path.join(k, value)
#         open(file_path, 'w').close()
#
# files_with_text = [r'Work\w.txt', r'Work\F1\f12.txt', r'Work\F2\F21\f211.txt', r'Work\F2\F21\f212.txt']
# for file in files_with_text:
#     with open(file, 'w') as f:
#         f.write(f"Какой-то текст для файла, расположенного по адресу: {file}")

root = r"C:\Users\a_ego\Documents\Python 313\Work"
inner = os.listdir(root)
for item in inner:
    path = os.path.join(root, item)
    if os.path.isfile(path):
        size = os.path.getsize(path)
        print(f'{item} - file - {size} bytes')
    else:
        print(f'{item} - dir')
