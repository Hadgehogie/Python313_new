# Создайте систему обработки платежной ведомости для сотрудников компании. Реализуйте базовый для всех сотрудников
# класс Employee. Он будет инициализировать код и имя сотрудника. Административные работники имеют фиксированную
# зарплату, поэтому каждую неделю им платят одну и ту же сумму. В компании также работают рабочие, которые получают
# почасовую оплату. В компании работают торговые представители, которым выплачивается фиксированная зарплата плюс
# комиссия, основанная на их продажах.

from Salary_employees import weekly_salary, hourly_salary, commission_salary


class PayrollSystem:
    @staticmethod
    def calculate(employees):
        print("Расчет заработной платы:")
        print("*" * 50)
        for employee in employees:
            print(f"Заработная плата: {employee.id} - {employee.name}")
            print(f"- Проверить сумму: {employee.calculate_payroll()}")
            print()


salary_employee = weekly_salary.SalaryEmployee(1, "Валерий Задорожный", 1500)
hourly_employee = hourly_salary.HourlyEmployee(2, "Илья Кронин", 40, 15)
commission_employee = commission_salary.CommissionEmployee(3, "Николай Хорольский", 1100, 150)

payroll_system = PayrollSystem()
payroll_system.calculate([
    salary_employee,
    hourly_employee,
    commission_employee
])
