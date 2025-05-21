class Employee:
    __name = None 
    __salary = None
    def __init__(self,name,salary):
        self.__name = name
        self.__salary = salary
    
    def get(self):
        return self.__name + ' ' + str(self.__salary)
    
        
employee = [
            Employee('jhon', 22000),
            Employee('eric', 23000)
    ]
for employe in employee:
    print(employe.get())
