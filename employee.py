class Employee:
    def __init__(self, name, contract, salary):
        self.name = name
        self.contract = contract
        self.salary = salary

    def get_pay(self):
        return self.salary

    def __str__(self):
        if self.contract == "monthly":
            return f"{self.name} works on a monthly salary of {self.salary}. Their total pay is {self.get_pay()}."


class HourlyEmployee:
    def __init__(self, name, contract, wage, hours):
        self.name = name
        self.contract = contract
        self.salary = None
        self.wage = wage
        self.hours = hours

    def get_pay(self):
        return self.hours * self.wage

    def __str__(self):
        return f"{self.name} works on a contract of {self.hours} hours at {self.wage}/hour. Their total pay is {self.get_pay()}."


class BonusSalaryEmployee:
    def __init__(self, name, contract, salary, bonus):
        self.name = name
        self.contract = contract
        self.salary = salary
        self.bonus = bonus

    def get_pay(self):
        return self.salary + self.bonus

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.salary} and receives a bonus commission of {self.bonus}. Their total pay is {self.get_pay()}."


class BonusHourlyEmployee:
    def __init__(self, name, contract, wage, hours, bonus):
        self.name = name
        self.contract = contract
        self.salary = None
        self.wage = wage
        self.hours = hours
        self.bonus = bonus

    def get_pay(self):
        return (self.hours * self.wage) + self.bonus

    def __str__(self):
        return f"{self.name} works on a contract of {self.hours} hours at {self.wage}/hour and receives a bonus commission of {self.bonus}. Their total pay is {self.get_pay()}."


class CommissionSalaryEmployee:
    def __init__(self, name, contract, salary, commission_rate, num_contracts):
        self.name = name
        self.contract = contract
        self.salary = salary
        self.commission_rate = commission_rate
        self.num_contracts = num_contracts

    def get_pay(self):
        return self.salary + (self.commission_rate * self.num_contracts)

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.salary} and receives a commission for {self.num_contracts} contract(s) at {self.commission_rate}/contract. Their total pay is {self.get_pay()}."


class CommissionHourlyEmployee:
    def __init__(self, name, contract, wage, hours, commission_rate, num_contracts):
        self.name = name
        self.contract = contract
        self.salary = None
        self.wage = wage
        self.hours = hours
        self.commission_rate = commission_rate
        self.num_contracts = num_contracts

    def get_pay(self):
        return (self.hours * self.wage) + (self.commission_rate * self.num_contracts)

    def __str__(self):
        return f"{self.name} works on a contract of {self.hours} hours at {self.wage}/hour and receives a commission for {self.num_contracts} contract(s) at {self.commission_rate}/contract. Their total pay is {self.get_pay()}."


# Create employee instances
billie = Employee('Billie', 'monthly', 4000)
charlie = HourlyEmployee('Charlie', 'hourly', 25, 100)
renee = CommissionSalaryEmployee('Renee', 'commissioned', 3000, 200, 4)
jan = CommissionHourlyEmployee('Jan', 'contract', 25, 150, 220, 3)
robbie = BonusSalaryEmployee('Robbie', 'bonus_commissioned', 2000, 1500)
ariel = BonusHourlyEmployee('Ariel', 'bonus_contract', 30, 120, 600)
