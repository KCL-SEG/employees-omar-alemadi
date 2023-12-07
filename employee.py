import re

class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        raise NotImplementedError("Subclasses must implement get_pay method")

    def __str__(self):
        raise NotImplementedError("Subclasses must implement __str__ method")

class MonthlySalaryEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def get_pay(self):
        return self.monthly_salary

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.monthly_salary}. Their total pay is {self.get_pay()}."

class HourlySalaryEmployee(Employee):
    def __init__(self, name, hours_worked, hourly_rate):
        super().__init__(name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def get_pay(self):
        return self.hours_worked * self.hourly_rate

    def __str__(self):
        return f"{self.name} works on a contract for {self.hours_worked} hours at {self.hourly_rate}/hour. Their total pay is {self.get_pay()}."

class MonthlySalaryContractCommissionEmployee(MonthlySalaryEmployee):
    def __init__(self, name, monthly_salary, num_contracts, commission_per_contract):
        super().__init__(name, monthly_salary)
        self.num_contracts = num_contracts
        self.commission_per_contract = commission_per_contract

    def get_pay(self):
        return super().get_pay() + (self.num_contracts * self.commission_per_contract)

    def __str__(self):
        return (f"{self.name} works on a monthly salary of {self.monthly_salary} and receives a commission for "
                f"{self.num_contracts} contract(s) at {self.commission_per_contract}/contract. Their total pay is {self.get_pay()}.")
