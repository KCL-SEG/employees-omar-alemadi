"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""
class MonthlySalaryEmployee(Employee):
    def __init__(self, name, monthly_salary, bonus_commission=0):
        super().__init__(name)
        self.monthly_salary = monthly_salary
        self.bonus_commission = bonus_commission

    def get_pay(self):
        return self.monthly_salary + self.bonus_commission

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.monthly_salary} and receives a bonus commission of {self.bonus_commission}. Their total pay is {self.get_pay()}."


class HourlyContractEmployee(Employee):
    def __init__(self, name, hourly_wage, hours_worked, bonus_commission=0):
        super().__init__(name)
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked
        self.bonus_commission = bonus_commission

    def get_pay(self):
        return self.hourly_wage * self.hours_worked + self.bonus_commission

    def __str__(self):
        return f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_wage}/hour and receives a bonus commission of {self.bonus_commission}. Their total pay is {self.get_pay()}."


class MonthlySalaryContractEmployee(Employee):
    def __init__(self, name, monthly_salary, contract_commission, num_contracts):
        super().__init__(name)
        self.monthly_salary = monthly_salary
        self.contract_commission = contract_commission
        self.num_contracts = num_contracts

    def get_pay(self):
        return self.monthly_salary + (self.contract_commission * self.num_contracts)

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.monthly_salary} and receives a commission for {self.num_contracts} contract(s) at {self.contract_commission}/contract. Their total pay is {self.get_pay()}."




