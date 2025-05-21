class Employee:
    def names(self, name, salary):
        return name + ' ' + salary
    name = None
    age = None
    salary = None
    
    pass

employee1 = Employee()

employee1.name = 'Sofiya'
employee1.age = 17
employee1.salary = 1150

print(employee1.name, employee1.age, employee1.salary)
print(employee1.names('Sofiya', '1150'))