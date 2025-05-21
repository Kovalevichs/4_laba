class User:

class Employee:
   def setter(self, salary,name, sname):
        self.salary = salary
        self.name = name
        self.sname = sname
    def getter(self, salary, name, sname):
        return self.salary + ' ' + self.name + ' ' + self.sname
class Employee(User):
   pass
employee = Employee()
employee.setter(123, 'asdff', 'asdfasd')

info = employee.getter()
print(name, sname, salary)

