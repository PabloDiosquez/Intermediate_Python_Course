se1 = ['Software Engineer','Max',35,'Junior',1000]
d1 = ['Designer','Philipp']

def code(se):
    return f'{se[1]} is writing code...'

# print(code(se1))
# print(code(d1))

# class
class SoftwareEngineer:
    # class attribute
    alias = 'Keyboard Magician'

    def __init__(self, name, age, level, salary):
        # instance attributes
        self.name   = name
        self.age    = age
        self.level  = level
        self.salary = salary

    # instance method
    def code(self):
        return f'{self.name} is writing code...'

    def code_in_language(self, language):
        return f'{self.name} is writing code in {language}...'

    # def information(self):
    #     return f'Name: {self.name} -- Age: {self.age} -- Level: {self.level} -- Salary: {self.salary}'

    # dunder method
    def __str__(self):
        information =  f'Name: {self.name} -- Age: {self.age} -- Level: {self.level}'
        return information

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age
    
    @staticmethod
    def entry_salary(age):
        if age < 25:
            return 5000
        elif age < 30:
            return 7000
        return 9000

se1 = SoftwareEngineer('Max',22,'Senior',5000)
se2 = SoftwareEngineer('Max',28,'Senior',7000)

print(se1.code())
print(se1.code_in_language('Python'))
print(se2.code_in_language('C++'))
# print(se1.information())
print(se1)
print(se1 == se2)
print(se1.entry_salary(32)) 
print(SoftwareEngineer.entry_salary(24))

# Recap:
# instance method(self)
# can take arguments and can return values
# special "dunder" (__str__ and __eq__)
# @staticmethod