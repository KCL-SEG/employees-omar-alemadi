class Employee:
    def __init__(self, emplyy_name, emplyy_contract, emplyy_salary):
        self.emplyy_name = emplyy_name
        self.emplyy_contract = emplyy_contract
        self.emplyy_salary = emplyy_salary

    def get_pay(self):
        return self.emplyy_salary

    def __str__(self):
        if self.emplyy_contract == "monthly":
            return f"{self.emplyy_name} works on a monthly salary of {self.emplyy_salary}. Their total pay is {self.get_pay()}."


class WorkContract:
    def __init__(self, emplyy_name, emplyy_contract, emplyy_wage, emplyy_hours):
        self.emplyy_name = emplyy_name
        self.emplyy_contract = emplyy_contract
        self.emplyy_salary = None
        self.emplyy_wage = emplyy_wage
        self.emplyy_hours = emplyy_hours

    def get_pay(self):
        return self.emplyy_hours * self.emplyy_wage

    def __str__(self):
        return f"{self.emplyy_name} works on a contract of {self.emplyy_hours} hours at {self.emplyy_wage}/hour. Their total pay is {self.get_pay()}."


class BonusSalaryEmployee:
    def __init__(self, emplyy_name, emplyy_contract, emplyy_salary, emplyy_bonus):
        self.emplyy_name = emplyy_name
        self.emplyy_contract = emplyy_contract
        self.emplyy_salary = emplyy_salary
        self.emplyy_bonus = emplyy_bonus

    def get_pay(self):
        return self.emplyy_salary + self.emplyy_bonus

    def __str__(self):
        return f"{self.emplyy_name} works on a monthly salary of {self.emplyy_salary} and receives a bonus commission of {self.emplyy_bonus}. Their total pay is {self.get_pay()}."


class BonusWorkContract:
    def __init__(self, emplyy_name, emplyy_contract, emplyy_wage, emplyy_hours, emplyy_bonus):
        self.emplyy_name = emplyy_name
        self.emplyy_contract = emplyy_contract
        self.emplyy_salary = None
        self.emplyy_wage = emplyy_wage
        self.emplyy_hours = emplyy_hours
        self.emplyy_bonus = emplyy_bonus

    def get_pay(self):
        return (self.emplyy_hours * self.emplyy_wage) + self.emplyy_bonus

    def __str__(self):
        return f"{self.emplyy_name} works on a contract of {self.emplyy_hours} hours at {self.emplyy_wage}/hour and receives a bonus commission of {self.emplyy_bonus}. Their total pay is {self.get_pay()}."


class CommissionSalaryEmployee:
    def __init__(self, emplyy_name, emplyy_contract, emplyy_salary, emplyy_commission_rate, emplyy_num_contracts):
        self.emplyy_name = emplyy_name
        self.emplyy_contract = emplyy_contract
        self.emplyy_salary = emplyy_salary
        self.emplyy_commission_rate = emplyy_commission_rate
        self.emplyy_num_contracts = emplyy_num_contracts

    def get_pay(self):
        return self.emplyy_salary + (self.emplyy_commission_rate * self.emplyy_num_contracts)

    def __str__(self):
        return f"{self.emplyy_name} works on a monthly salary of {self.emplyy_salary} and receives a commission for {self.emplyy_num_contracts} contract(s) at {self.emplyy_commission_rate}/contract. Their total pay is {self.get_pay()}."


class CommissionWorkContract:
    def __init__(self, emplyy_name, emplyy_contract, emplyy_wage, emplyy_hours, emplyy_commission_rate, emplyy_num_contracts):
        self.emplyy_name = emplyy_name
        self.emplyy_contract = emplyy_contract
        self.emplyy_salary = None
        self.emplyy_wage = emplyy_wage
        self.emplyy_hours = emplyy_hours
        self.emplyy_commission_rate = emplyy_commission_rate
        self.emplyy_num_contracts = emplyy_num_contracts

    def get_pay(self):
        return (self.emplyy_hours * self.emplyy_wage) + (self.emplyy_commission_rate * self.emplyy_num_contracts)

    def __str__(self):
        return f"{self.emplyy_name} works on a contract of {self.emplyy_hours} hours at {self.emplyy_wage}/hour and receives a commission for {self.emplyy_num_contracts} contract(s) at {self.emplyy_commission_rate}/contract. Their total pay is {self.get_pay()}."


billie = Employee('Billie', 'monthly', 4000)
charlie = WorkContract('Charlie', 'hourly', 25, 100)
renee = CommissionSalaryEmployee('Renee', 'commissioned', 3000, 200, 4)
jan = CommissionWorkContract('Jan', 'contract', 25, 150, 220, 3)
robbie = BonusSalaryEmployee('Robbie', 'bonus_commissioned', 2000, 1500)
ariel = BonusWorkContract('Ariel', 'bonus_contract', 30, 120, 600)
