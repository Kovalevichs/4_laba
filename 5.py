class Employee:
    name = None
    age = None
    salary = None
    
    def prize(self):
        return 'prize 2000'
    pass

employee1 = Employee()
employee2 = Employee()

employee1.name = 'Sofiya'
employee1.age = 17
employee1.salary = 1150

employee2.name = 'Egor'
employee2.age = 19
employee2.salary = 20000

sum_salaries = employee1.salary + employee2.salary
print(sum_salaries)
print(employee1.prize())