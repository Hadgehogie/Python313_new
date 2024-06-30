# Найти адрес электронной почты:

import re

test = "123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login.3@ru.name.ru, "

reg = r"[\w.-]+@[a-z]+\.?[a-z]*.ru"

print(re.findall(reg, test))
