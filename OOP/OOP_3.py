# inherits, extend and override
class Employee:

    def __init__(self, name, age, salary):
        self.name   = name
        self.age    = age
        self.salary = salary

    def work(self):
        return f'{self.name} is working...'

class SoftwareEngineer(Employee):

    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary)
        self.level = level

    def debug(self):
        return f'{self.name} is debugging...'

    def work(self):
        return f'{self.name} is coding...'

class Designer(Employee):
    
    def draw(self):
        return f'{self.name} is drawing...'

    def work(self):
        return f'{self.name} is designing...'

# se = SoftwareEngineer('Max', 28, 5000, 'Junior')
# print(se.name, se.age)
# print(se.work())
# print(se.level)
# print(se.debug())

# d = Designer('Lisa', 23, 6000)
# print(d.name, d.age)
# print(d.work())
# print(d.draw())
# print()

# Polymorphism
employees = [SoftwareEngineer('Max', 28, 7000, 'Junior'), SoftwareEngineer('Jack', 23, 5000, 'Junior'), Designer('Lisa', 23, 6000)]

def motivateEmployees(employees: list):
    for employee in employees:
        print(employee.work())

motivateEmployees(employees)

# Recap:
# inheritance: ChildClass(BaseClass)
# inherit, extend and override
# super().__init__()
# polymorphism