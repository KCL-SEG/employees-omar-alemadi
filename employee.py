"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""
class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        return 0

    def __str__(self):
        return self.name


class CommissionedEmployee(Employee):
    def __init__(self, name, commission_rate=0, bonus=0, num_contracts=0):
        super().__init__(name)
        self.commission_rate = commission_rate
        self.bonus = bonus
        self.num_contracts = num_contracts

    def commission_pay(self):
        return self.commission_rate * self.num_contracts


class MonthlySalaryEmployee(CommissionedEmployee):
    def __init__(self, name, monthly_salary, bonus=0, commission_rate=0, num_contracts=0):
        super().__init__(name, commission_rate, bonus, num_contracts)
        self.monthly_salary = monthly_salary

    def get_pay(self):
        total_pay = self.monthly_salary + self.bonus + self.commission_pay()
        return total_pay

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.monthly_salary} and receives a bonus commission of {self.bonus}. Their total pay is {self.get_pay()}."


class HourlyEmployee(CommissionedEmployee):
    def __init__(self, name, hourly_rate, hours_worked, bonus=0, commission_rate=0, num_contracts=0):
        super().__init__(name, commission_rate, bonus, num_contracts)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def get_pay(self):
        total_pay = (self.hourly_rate * self.hours_worked) + self.bonus + self.commission_pay()
        return total_pay

    def __str__(self):
        return f"{self.name} works on a contract for {self.hours_worked} hours at {self.hourly_rate}/hour and receives a bonus commission of {self.bonus}. Their total pay is {self.get_pay()}."


# Examples with original names
billie = MonthlySalaryEmployee('Billie', monthly_salary=4000)
charlie = HourlyEmployee('Charlie', hourly_rate=25, hours_worked=100)
renee = MonthlySalaryEmployee('Renee', monthly_salary=3000, bonus=0, commission_rate=200, num_contracts=4)
jan = HourlyEmployee('Jan', hourly_rate=25, hours_worked=150, bonus=0, commission_rate=220, num_contracts=3)
robbie = MonthlySalaryEmployee('Robbie', monthly_salary=2000, bonus=1500)
ariel = HourlyEmployee('Ariel', hourly_rate=30, hours_worked=120, bonus=600)

# Testing
print(str(billie))
print(str(charlie))
print(str(renee))
print(str(jan))
print(str(robbie))
print(str(ariel))



