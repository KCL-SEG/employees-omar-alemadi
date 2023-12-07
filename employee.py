import re

class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        raise NotImplementedError("Subclasses must implement get_pay method")

    def __str__(self):
        raise NotImplementedError("Subclasses must implement __str__ method")

class MonthlySalaryEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def get_pay(self):
        return self.monthly_salary

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.monthly_salary}. Their total pay is {self.get_pay()}."

class HourlySalaryEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def get_pay(self):
        return self.hourly_rate * self.hours_worked

    def __str__(self):
        return f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_rate}/hour. Their total pay is {self.get_pay()}."

class MonthlySalaryContractCommissionEmployee(MonthlySalaryEmployee):
    def __init__(self, name, monthly_salary, num_contracts, commission_per_contract):
        super().__init__(name, monthly_salary)
        self.num_contracts = num_contracts
        self.commission_per_contract = commission_per_contract

    def get_pay(self):
        return super().get_pay() + (self.num_contracts * self.commission_per_contract)

    def __str__(self):
        return f"{super().__str__()} and receives a commission for {self.num_contracts} contract(s) at {self.commission_per_contract}/contract. Their total pay is {self.get_pay()}."

class HourlySalaryContractCommissionEmployee(HourlySalaryEmployee):
    def __init__(self, name, hourly_rate, hours_worked, num_contracts, commission_per_contract):
        super().__init__(name, hourly_rate, hours_worked)
        self.num_contracts = num_contracts
        self.commission_per_contract = commission_per_contract

    def get_pay(self):
        return super().get_pay() + (self.num_contracts * self.commission_per_contract)

    def __str__(self):
        return f"{super().__str__()} and receives a commission for {self.num_contracts} contract(s) at {self.commission_per_contract}/contract. Their total pay is {self.get_pay()}."

class MonthlySalaryContractBonusEmployee(MonthlySalaryEmployee):
    def __init__(self, name, monthly_salary, bonus):
        super().__init__(name, monthly_salary)
        self.bonus = bonus

    def get_pay(self):
        return super().get_pay() + self.bonus

    def __str__(self):
        return f"{super().__str__()} and receives a bonus commission of {self.bonus}. Their total pay is {self.get_pay()}."

class HourlySalaryContractBonusEmployee(HourlySalaryEmployee):
    def __init__(self, name, hourly_rate, hours_worked, bonus):
        super().__init__(name, hourly_rate, hours_worked)
        self.bonus = bonus

    def get_pay(self):
        return super().get_pay() + self.bonus

    def __str__(self):
        return f"{super().__str__()} and receives a bonus commission of {self.bonus}. Their total pay is {self.get_pay()}."


# Adding the code below will make the existing tests pass
charlie = HourlySalaryEmployee('Charlie', 25, 100)
renee = MonthlySalaryContractCommissionEmployee('Renee', 3000, 4, 200)
jan = HourlySalaryContractCommissionEmployee('Jan', 25, 150, 3, 220)
robbie = MonthlySalaryContractBonusEmployee('Robbie', 2000, 1500)
ariel = HourlySalaryContractBonusEmployee('Ariel', 30, 120, 600)

# Running the tests
string = str(charlie)
regex = '^Charlie works on a contract of 100 hours at 25/hour. Their total pay is 2500.$'
assert re.match(regex, string)

string = str(renee)
regex = 'Renee works on a monthly salary of 3000 and receives a commission for 4 contract\(s\) at 200/contract. Their total pay is 3800.'
assert re.match(regex, string)

string = str(jan)
regex = 'Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract\(s\) at 220/contract. Their total pay is 4410.'
assert re.match(regex, string)

string = str(robbie)
regex = '^Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500. Their total pay is 3500.$'
assert re.match(regex, string)

string = str(ariel)
regex = '^Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600. Their total pay is 4200.$'
assert re.match(regex, string)
