# Создать класс Student, который будет содержать имя и распечатывать информацию. Также создать вложенный класс,
# который будет содержать информацию о ноутбуке с техническими характеристиками: модель, процессор и память

class Student:
    def __init__(self, name):
        self.name = name
        self.comp = self.Computer('HP', 'i7', 16)

    def show(self):
        print(f'{self.name} => {self.comp.model}, {self.comp.proc}, {self.comp.mem}')

    class Computer:
        def __init__(self, model, proc, mem):
            self.model = model
            self.proc = proc
            self.mem = mem


winner1 = Student('Roman')
winner1.show()

winner2 = Student('Vladimir')
winner2.show()
