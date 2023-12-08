class Employee:
    def __init__(self, n, c, s):
        self.name = n
        self.contract = c
        self.salary = s

    def get_pay(self):
        return self.salary

    def __str__(self):
        if self.contract == "monthly":
            return f"{self.name} works on a monthly salary of {self.salary}. Their total pay is {self.get_pay()}."


class HourlyEmployee:
    def __init__(self, n, c, w, h):
        self.name = n
        self.contract = c
        self.salary = None
        self.wage = w
        self.hours = h

    def get_pay(self):
        return self.hours * self.wage

    def __str__(self):
        return f"{self.name} works on a contract of {self.hours} hours at {self.wage}/hour. Their total pay is {self.get_pay()}."


class BonusSalaryEmployee:
    def __init__(self, n, c, s, b):
        self.name = n
        self.contract = c
        self.salary = s
        self.bonus = b

    def get_pay(self):
        return self.salary + self.bonus

    def __str__(self):
        return f"{self.name} works on a {self.contract} salary of {self.salary} and receives a bonus commission of {self.bonus}. Their total pay is {self.get_pay()}."


class BonusHourlyEmployee:
    def __init__(self, n, c, w, h, b):
        self.name = n
        self.contract = c
        self.salary = None
        self.wage = w
        self.hours = h
        self.bonus = b

    def get_pay(self):
        return (self.hours * self.wage) + self.bonus

    def __str__(self):
        return f"{self.name} works on an {self.contract} contract of {self.hours} hours at {self.wage}/hour and receives a bonus commission of {self.bonus}. Their total pay is {self.get_pay()}."


class CommissionSalaryEmployee:
    def __init__(self, n, c, s, cr, nc):
        self.name = n
        self.contract = c
        self.salary = s
        self.commission_rate = cr
        self.num_contracts = nc

    def get_pay(self):
        return self.salary + (self.commission_rate * self.num_contracts)

    def __str__(self):
        return f"{self.name} works on a {self.contract} salary of {self.salary} and receives a commission for {self.num_contracts} contract(s) at {self.commission_rate}/contract. Their total pay is {self.get_pay()}."


class CommissionHourlyEmployee:
    def __init__(self, n, c, w, h, cr, nc):
        self.name = n
        self.contract = c
        self.salary = None
        self.wage = w
        self.hours = h
        self.commission_rate = cr
        self.num_contracts = nc

    def get_pay(self):
        return (self.hours * self.wage) + (self.commission_rate * self.num_contracts)

    def __str__(self):
        return f"{self.name} works on an {self.contract} contract of {self.hours} hours at {self.wage}/hour and receives a commission for {self.num_contracts} contract(s) at {self.commission_rate}/contract. Their total pay is {self.get_pay()}."


# Create employee instances
billie = Employee('Billie', 'monthly', 4000)
charlie = HourlyEmployee('Charlie', 'hourly', 25, 100)
renee = CommissionSalaryEmployee('Renee', 'commissioned', 3000, 200, 4)
jan = CommissionHourlyEmployee('Jan', 'contract', 25, 150, 220, 3)
robbie = BonusSalaryEmployee('Robbie', 'monthly', 2000, 1500)
ariel = BonusHourlyEmployee('Ariel', 'hourly', 30, 120, 600)
