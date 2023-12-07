"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        pass

    def __str__(self):
        return self.name


class MonthlySalaryEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def get_pay(self):
        return self.monthly_salary

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.monthly_salary}. Their total pay is {self.get_pay()}."


class HourlySalaryEmployee(Employee):
    def __init__(self, name, hourly_wage, hours_worked):
        super().__init__(name)
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked

    def get_pay(self):
        return self.hourly_wage * self.hours_worked

    def __str__(self):
        return f"{self.name} works on a contract for {self.hours_worked} hours at {self.hourly_wage}/hour. Their total pay is {self.get_pay()}."


class MonthlySalaryBonusEmployee(Employee):
    def __init__(self, name, monthly_salary, bonus_commission):
        super().__init__(name)
        self.monthly_salary = monthly_salary
        self.bonus_commission = bonus_commission

    def get_pay(self):
        return self.monthly_salary + self.bonus_commission

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.monthly_salary} and receives a bonus commission of {self.bonus_commission}. Their total pay is {self.get_pay()}."


class HourlySalaryBonusEmployee(Employee):
    def __init__(self, name, hourly_wage, hours_worked, bonus_commission):
        super().__init__(name)
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked
        self.bonus_commission = bonus_commission

    def get_pay(self):
        return (self.hourly_wage * self.hours_worked) + self.bonus_commission

    def __str__(self):
        return f"{self.name} works on a contract for {self.hours_worked} hours at {self.hourly_wage}/hour and receives a bonus commission of {self.bonus_commission}. Their total pay is {self.get_pay()}."


class MonthlySalaryContractBonusEmployee(Employee):
    def __init__(self, name, monthly_salary, contract_commission, num_contracts, bonus_commission):
        super().__init__(name)
        self.monthly_salary = monthly_salary
        self.contract_commission = contract_commission
        self.num_contracts = num_contracts
        self.bonus_commission = bonus_commission

    def get_pay(self):
        return (self.monthly_salary + (self.contract_commission * self.num_contracts)) + self.bonus_commission

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.monthly_salary} and receives a commission for {self.num_contracts} contract(s) at {self.contract_commission}/contract and a bonus commission of {self.bonus_commission}. Their total pay is {self.get_pay()}."


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = MonthlySalaryEmployee('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = HourlySalaryEmployee('Charlie', 25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = MonthlySalaryContractBonusEmployee('Renee', 3000, 200, 4, 0)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = MonthlySalaryContractBonusEmployee('Jan', 0, 25, 3, 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = MonthlySalaryBonusEmployee('Robbie', 2000, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = HourlySalaryBonusEmployee('Ariel', 30, 120, 600)
