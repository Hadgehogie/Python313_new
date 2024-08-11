import json


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        a = ", ".join(map(str, self.marks))
        return f'Студент: {self.name}: {a}'

    def add_mark(self, mark):
        self.marks.append(mark)

    def delete_mark(self, index):
        self.marks.pop(index)

    def edit_mark(self, index, new_mark):
        self.marks[index] = new_mark

    def average_mark(self):
        return round(sum(self.marks) / len(self.marks), 2)

    def dump_to_json(self):
        data = {'name': self.name, 'marks': self.marks}
        with open(self.get_file_name(), 'w') as f:
            json.dump(data, f)

    def load_from_file(self):
        with open(self.get_file_name(), 'r') as f:
            print(json.load(f))

    def get_file_name(self):
        return f'{self.name}.json'


class Group:
    def __init__(self, students, group: str):
        self.students = students
        self.group: str = group

    def __str__(self):
        a = " \n".join(map(str, self.students))
        return f'\nГруппа: {self.group} \n{a}'

    @staticmethod
    def change_group(group_1, group_2, index):
        group_2.add_student(group_1.delete_student(index))

    def add_student(self, new_student):
        self.students.append(new_student)

    def delete_student(self, index):
        return self.students.pop(index)

    # def dump_to_json(self):
    #     data = [
    #             {'name': student.name, 'marks': student.marks} for student in self.students
    #         ]
    #     with open(self.get_file_name(), 'w') as f:
    #         json.dump(data, f, indent=2)
    #
    # def get_file_name(self):
    #     return f'{self.group.lower().replace(" ", "-")}.json'
    #
    # def load_from_file(self):
    #     with open(self.get_file_name(), 'r') as f:
    #         print(json.load(f))

    def get_students(self):
        return [
            {
                student.name: student.marks
            } for student in self.students
        ]

    @staticmethod
    def one_file_to_rule_them_all(*args):
        data = [
            {
                arg.group: arg.get_students()
            } for arg in args
        ]
        with open("all_groups.json", 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)


st1 = Student('Petrov', [4, 5, 3, 4, 4, 5])
st2 = Student('Ivanov', [2, 2, 3, 4, 5, 2])
st3 = Student('Sidorov', [5, 5, 4, 5, 3, 5])
st4 = Student('Doronina', [4, 4, 3, 5, 2, 5])

# st1.add_mark(4)
# st1.delete_mark(2)
# st1.edit_mark(4, 5)

gr1 = [st1, st2, st3]

group1 = Group(gr1, "ГК Python")
group1.add_student(st4)
group1.delete_student(1)

gr2 = [st2]

group2 = Group(gr2, "ГК Web")
Group.change_group(group1, group2, 0)
print(group1)
print(group2)

Group.one_file_to_rule_them_all(group1, group2)
