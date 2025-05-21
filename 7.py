class Employee:
    name = None
    salary = None
    
    def names(self):
        print(self.name)
        
    def prize(self):
        print(self.salary)
    pass

employee1 = Employee()

employee1.name = 'Sofiya'
employee1.salary = 1150
employee1.names()
employee1.prize()



# print(employee1.name, employee1.salary)