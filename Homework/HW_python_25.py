# Создать класс Person с двумя закрытыми свойствами: имя и возраст. С использованием декоратора @property создать
# возможность изменения этих свойств, а также возможность их удаления.

class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self.__name = new_name
            print(new_name)
        else:
            print("Новое вводимое имя должно быть строкой")

    @name.deleter
    def name(self):
        del self.__name

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, new_old):
        if isinstance(new_old, int):
            self.__old = new_old
            print(new_old)
        else:
            print("Новое вводимое имя должно быть целым числом")

    @old.deleter
    def old(self):
        del self.__old

    def print_data(self):
        print(self.__dict__)


admin = Person('Irina', 26)
admin.print_data()
admin.name = 'Igor'
admin.old = 31
# admin.print_data()
del admin.name
admin.print_data()
