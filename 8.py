class Student:
    name = 'Sofiya'
    surname = 'Kovalevich'
    
    def emp_name(self):
        return self.cape(self.name + ' ' + self.surname)
    
    def cape(self, stri):
        return stri.upper()
        
    def ravine(self):
        return self.cape(self.name[0] + ' ' + self.surname[0])
    pass

student = Student()

print(student.emp_name())
print(student.ravine())
