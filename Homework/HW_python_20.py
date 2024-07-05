# Валидация номера телефона:

import re

text = """
+7 499 456-45-78
+74994564578
+7 (499) 456 45 78
+7 (499) 456-45-78
"""
reg = r'\+7\s*[(]?\d{3}[)]?\s*\d{3}[\s-]*\d{2}[\s-]*\d{2}'


def phone_num(m):
    return m.group()


print(re.sub(reg, phone_num, text))
