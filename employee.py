"""Employee pay calculator."""

class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        return 0  # Default implementation, should be overridden by subclasses

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

class HourlyContractEmployee(Employee):
    def __init__(self, name, hours_worked, hourly_wage):
        super().__init__(name)
        self.hours_worked = hours_worked
        self.hourly_wage = hourly_wage

    def get_pay(self):
        return self.hours_worked * self.hourly_wage

    def __str__(self):
        return f"{self.name} works on a contract for {self.hours_worked} hours at {self.hourly_wage}/hour. Their total pay is {self.get_pay()}."

class MonthlySalaryContractBonusEmployee(MonthlySalaryEmployee):
    def __init__(self, name, monthly_salary, bonus_commission):
        super().__init__(name, monthly_salary)
        self.bonus_commission = bonus_commission

    def get_pay(self):
        return super().get_pay() + self.bonus_commission

    def __str__(self):
        return f"{super().__str__()} and receives a bonus commission of {self.bonus_commission}. Their total pay is {self.get_pay()}."

class HourlyContractBonusEmployee(HourlyContractEmployee):
    def __init__(self, name, hours_worked, hourly_wage, bonus_commission):
        super().__init__(name, hours_worked, hourly_wage)
        self.bonus_commission = bonus_commission

    def get_pay(self):
        return super().get_pay() + self.bonus_commission

    def __str__(self):
        return f"{super().__str__()} and receives a bonus commission of {self.bonus_commission}. Their total pay is {self.get_pay()}."

class MonthlySalaryContractCommissionEmployee(MonthlySalaryEmployee):
    def __init__(self, name, monthly_salary, contracts_landed, commission_per_contract):
        super().__init__(name, monthly_salary)
        self.contracts_landed = contracts_landed
        self.commission_per_contract = commission_per_contract

    def get_pay(self):
        return super().get_pay() + self.contracts_landed * self.commission_per_contract

    def __str__(self):
        return f"{super().__str__()} and receives a commission for {self.contracts_landed} contract(s) at {self.commission_per_contract}/contract. Their total pay is {self.get_pay()}."

class HourlyContractCommissionEmployee(HourlyContractEmployee):
    def __init__(self, name, hours_worked, hourly_wage, contracts_landed, commission_per_contract):
        super().__init__(name, hours_worked, hourly_wage)
        self.contracts_landed = contracts_landed
        self.commission_per_contract = commission_per_contract

    def get_pay(self):
        return super().get_pay() + self.contracts_landed * self.commission_per_contract

    def __str__(self):
        return f"{super().__str__()} and receives a commission for {self.contracts_landed} contract(s) at {self.commission_per_contract}/contract. Their total pay is {self.get_pay()}."

# Employee objects
billie = MonthlySalaryEmployee('Billie', 4000)
charlie = HourlyContractEmployee('Charlie', 100, 25)
renee = MonthlySalaryContractCommissionEmployee('Renee', 3000, 4, 200)
jan = HourlyContractCommissionEmployee('Jan', 150, 25, 3, 220)
robbie = MonthlySalaryContractBonusEmployee('Robbie', 2000, 1500)
ariel = HourlyContractBonusEmployee('Ariel', 120, 30, 600)
