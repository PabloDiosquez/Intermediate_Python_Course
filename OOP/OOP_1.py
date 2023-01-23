# position, name, age, level, salary
se1 = ['Software Engineer','Lio',35,'Junior',1000]
se2 = ['Software Engineer','Lisa',29,'Senior',5000]

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

# instance
se1 = SoftwareEngineer('Max',28,'Senior',5000)
se2 = SoftwareEngineer('Lisa',25,'Senior',7000)
print(se1.name, se1.age)
print(SoftwareEngineer.alias)
print(se2.alias)

# Recap:
# create a class (blueprint)
# create a instance (object)
# class vs instance
# instance attributes defined in __init__(self)
# class attribute