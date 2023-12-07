import re

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

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = MonthlySalaryEmployee('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = HourlySalaryEmployee('Charlie', 25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = MonthlySalaryEmployee('Renee', 3000, contracts=4, commission_per_contract=200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = HourlySalaryEmployee('Jan', 25, 150, contracts=3, commission_per_contract=220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = MonthlySalaryEmployee('Robbie', 2000, bonus=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = HourlySalaryEmployee('Ariel', 30, 120, bonus=600)

if __name__ == "__main__":
    # Run additional tests if needed
    string = str(billie)
    regex = r'^Billie works on a monthly salary of 4000\.  Their total pay is 4000\.$'
    assert re.match(regex, string)

    string = str(charlie)
    regex = r'^Charlie works on a contract of 100 hours at 25/hour\.  Their total pay is 2500\.$'
    assert re.match(regex, string)

    string = str(renee)
    regex = r'Renee works on a monthly salary of 3000 and receives a commission for 4 contract\(s\) at 200/contract\.  Their total pay is 3800\.'
    assert re.match(regex, string)

    string = str(jan)
    regex = r'Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract\(s\) at 220/contract\.  Their total pay is 4410\.'
    assert re.match(regex, string)

    string = str(robbie)
    regex = r'^Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500\.  Their total pay is 3500\.$'
    assert re.match(regex, string)

    string = str(ariel)
    regex = r'^Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600\.  Their total pay is 4200\.$'
    assert re.match(regex, string)
