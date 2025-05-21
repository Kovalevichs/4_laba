class Employee:
    __name = None 
    __salary = None
    def __init__(self,name,salary):
        self.__name = name
        self.__salary = salary
    
    def get(self):
        return self.__name + ' ' + str(self.__salary)
        
class EmpoyeesCollection:
    
    def __init__(self):
        self.__name = []
        self.__salary = []

        
    def add(self, employee, salary):
        self.__name.append(employee)
        self.__salary.append(salary)
        
    def show(self):
        for employe in self.__name:
            print(employe)
            
    def showzp(self):
        for zp in self.__salary:
            print(zp)
            
uc = EmpoyeesCollection()
uc.add('jhon', 23000)
uc.add('eric', 22000)

uc.show()
uc.showzp()
