import math

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
        return f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_wage}/hour. Their total pay is {self.get_pay()}."


class MonthlySalaryContractBonusEmployee(MonthlySalaryEmployee):
    def __init__(self, name, monthly_salary, bonus_commission):
        super().__init__(name, monthly_salary)
        self.bonus_commission = bonus_commission

    def get_pay(self):
        return super().get_pay() + self.bonus_commission

    def __str__(self):
        return f"{super().__str__()} and receives a bonus commission of {self.bonus_commission}. Their total pay is {self.get_pay()}."


class HourlySalaryContractBonusEmployee(HourlySalaryEmployee):
    def __init__(self, name, hourly_wage, hours_worked, bonus_commission):
        super().__init__(name, hourly_wage, hours_worked)
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
        return super().get_pay() + (self.contracts_landed * self.commission_per_contract)

    def __str__(self):
        return f"{super().__str__()} and receives a commission for {self.contracts_landed} contract(s) at {self.commission_per_contract}/contract. Their total pay is {self.get_pay()}."


class HourlySalaryContractCommissionEmployee(HourlySalaryEmployee):
    def __init__(self, name, hourly_wage, hours_worked, contracts_landed, commission_per_contract):
        super().__init__(name, hourly_wage, hours_worked)
        self.contracts_landed = contracts_landed
        self.commission_per_contract = commission_per_contract

    def get_pay(self):
        return super().get_pay() + (self.contracts_landed * self.commission_per_contract)

    def __str__(self):
        return f"{super().__str__()} and receives a commission for {self.contracts_landed} contract(s) at {self.commission_per_contract}/contract. Their total pay is {self.get_pay()}."

# Test cases
billie = MonthlySalaryEmployee('Billie', 4000)
charlie = HourlySalaryEmployee
