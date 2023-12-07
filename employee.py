"""Employee pay calculator."""

import re  # Add this import for using re.match

class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        raise NotImplementedError("Subclasses must implement get_pay method")

    def __str__(self):
        raise NotImplementedError("Subclasses must implement __str__ method")

class MonthlySalaryEmployee(Employee):
    def __init__(self, name, monthly_salary, bonus=0, contracts=0, commission_per_contract=0):
        super().__init__(name)
        self.monthly_salary = monthly_salary
        self.bonus = bonus
        self.contracts = contracts
        self.commission_per_contract = commission_per_contract

    def get_pay(self):
        return self.monthly_salary + self.bonus + (self.contracts * self.commission_per_contract)

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.monthly_salary}. Their total pay is {self.get_pay()}."

class HourlySalaryEmployee(Employee):
    def __init__(self, name, hourly_wage, hours_worked, bonus=0, contracts=0, commission_per_contract=0):
        super().__init__(name)
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked
        self.bonus = bonus
        self.contracts = contracts
        self.commission_per_contract = commission_per_contract

    def get_pay(self):
        return (self.hourly_wage * self.hours_worked) + self.bonus + (self.contracts * self.commission_per_contract)

    def __str__(self):
        return f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_wage}/hour. Their total pay is {self.get_pay()}."

# Create instances for employees
billie = MonthlySalaryEmployee("Billie", monthly_salary=4000)
charlie = HourlySalaryEmployee("Charlie", hourly_wage=25, hours_worked=100)
renee = MonthlySalaryEmployee("Renee", monthly_salary=3000, contracts=4, commission_per_contract=200)
jan = HourlySalaryEmployee("Jan", hourly_wage=25, hours_worked=150, contracts=3, commission_per_contract=220)
robbie = MonthlySalaryEmployee("Robbie", monthly_salary=2000, bonus=1500)
ariel = HourlySalaryEmployee("Ariel", hourly_wage=30, hours_worked=120, bonus=600)
