"""Employee pay calculator."""

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
