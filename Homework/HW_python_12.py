# Дан словарь {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}. Создать новый словарь, который
# будет содержать только имя и зарплату сотрудника, а затем удалить эти значения из словаря.

d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
d_new = d.copy()

d.pop('name')
d.pop('salary')
print('Исходный словарь:', d)

d_new.pop('age')
d_new.pop('city')
print('Новый словарь:', d_new)

