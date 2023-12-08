class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        pass

    def __str__(self):
        return self.name


class MonthlyEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def get_pay(self):
        return self.monthly_salary

    def __str__(self):
        return f"{super().__str__()} works on a monthly salary of {self.monthly_salary}. Their total pay is {self.get_pay()}."


class ContractEmployee(Employee):
    def __init__(self, name, hours, rate):
        super().__init__(name)
        self.hours = hours
        self.rate = rate

    def get_pay(self):
        return self.hours * self.rate

    def __str__(self):
        return f"{super().__str__()} works on a contract of {self.hours} hours at {self.rate}/hour. Their total pay is {self.get_pay()}."


class CommissionedEmployee(MonthlyEmployee):
    def __init__(self, name, monthly_salary, commission_rate, num_contracts):
        super().__init__(name, monthly_salary)
        self.commission_rate = commission_rate
        self.num_contracts = num_contracts

    def get_pay(self):
        return super().get_pay() + (self.commission_rate * self.num_contracts)

    def __str__(self):
        return f"{super().__str__()} and receives a commission for {self.num_contracts} contract(s) at {self.commission_rate}/contract. Their total pay is {self.get_pay()}."


class BonusCommissionedEmployee(MonthlyEmployee):
    def __init__(self, name, monthly_salary, bonus_commission):
        super().__init__(name, monthly_salary)
        self.bonus_commission = bonus_commission

    def get_pay(self):
        return super().get_pay() + self.bonus_commission

    def __str__(self):
        return f"{super().__str__()} and receives a bonus commission of {self.bonus_commission}. Their total pay is {self.get_pay()}."


# Create employee instances
billie = MonthlyEmployee('Billie', 4000)
charlie = ContractEmployee('Charlie', 100, 25)
renee = CommissionedEmployee('Renee', 3000, 200, 4)
jan = CommissionedEmployee('Jan', 0, 220, 3)  # Monthly salary set to 0
robbie = BonusCommissionedEmployee('Robbie', 2000, 1500)
ariel = BonusCommissionedEmployee('Ariel', 0, 600)  # Monthly salary set to 0



