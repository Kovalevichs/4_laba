class Position :
    position = None
    
    def __init__(self, position):
        self.position = position
        
class Department : 
    department = None
    
    def __init__(self, department):
        self.department = department

class User :
    name = None
    position = None
    department = None
    
    
    def __init__(self,name, position, department):
        self.name = name
        self.position = position
        self.department = department
        

        
    
position = Position('asdffasdf')
department = Department('fdafdsafads')
user = User('Maksim', position, department)

print(user.position.name)

