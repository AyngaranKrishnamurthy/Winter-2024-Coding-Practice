#Abstract Class
from abc import ABC, abstractmethod

class university(ABC): #Use of ABC defines this as Abstract Class

    @abstractmethod
    def college_data(self):
        pass

    @abstractmethod
    def department_data(self):
        pass

class OldDominionUniversity(university):
    def __init__(self,college,dept):
        self.college = college
        self.dept = dept

    def college_data(self):
        return self.college
    
    def department_data(self):
        return self.dept
    
new_dept = OldDominionUniversity("College of Sciences","Computer Science")

print(new_dept.college_data())
print(new_dept.department_data())
        