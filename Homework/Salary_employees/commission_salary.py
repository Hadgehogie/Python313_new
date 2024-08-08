from Homework.Salary_employees.weekly_salary import SalaryEmployee


class CommissionEmployee(SalaryEmployee):
    """Торговые представители, получающие фиксированную оплату и комиссию сверху"""

    def __init__(self, id_employee, name, weekly_salary, commission):
        super().__init__(id_employee, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        return self.weekly_salary + self.commission
