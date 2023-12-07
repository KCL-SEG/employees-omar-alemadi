"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""
class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        return 0

    def __str__(self):
        return self.name


class MonthlySalaryEmployee(Employee):
    def __init__(self, name, monthly_salary, bonus=0, contract_commission=0):
        super().__init__(name)
        self.monthly_salary = monthly_salary
        self.bonus = bonus
        self.contract_commission = contract_commission

    def get_pay(self):
        total_pay = self.monthly_salary + self.bonus + (self.contract_commission * self.num_contracts)
        return total_pay

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.monthly_salary} and receives a bonus commission of {self.bonus}. Their total pay is {self.get_pay()}."


class HourlyEmployee(Employee):
    def __init__(self, name, hours_worked, hourly_rate, bonus=0, contract_commission=0):
        super().__init__(name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
        self.bonus = bonus
        self.contract_commission = contract_commission

    def get_pay(self):
        total_pay = (self.hours_worked * self.hourly_rate) + self.bonus + (self.contract_commission * self.num_contracts)
        return total_pay

    def __str__(self):
        return f"{self.name} works on a contract for {self.hours_worked} hours at {self.hourly_rate}/hour and receives a bonus commission of {self.bonus}. Their total pay is {self.get_pay()}."


# Examples with original names
billie = MonthlySalaryEmployee('Billie', 4000)
charlie = HourlyEmployee('Charlie', 100, 25)
renee = MonthlySalaryEmployee('Renee', 3000, contract_commission=200, num_contracts=4)
jan = HourlyEmployee('Jan', 150, 25, contract_commission=220, num_contracts=3)
robbie = MonthlySalaryEmployee('Robbie', 2000, bonus=1500)
ariel = HourlyEmployee('Ariel', 120, 30, bonus=600)

# Testing
print(str(billie))
print(str(charlie))
print(str(renee))
print(str(jan))
print(str(robbie))
print(str(ariel))

