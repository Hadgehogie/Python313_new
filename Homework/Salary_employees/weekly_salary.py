from Homework.Salary_employees.employee import Employee


class SalaryEmployee(Employee):
    """Административные работники с фиксированной зарплатой"""

    def __init__(self, id_employee, name, weekly_salary):
        super().__init__(id_employee, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary
