#Inheritance utilizes a pre existing class to inherit its functionalities without need for redundant code
class parentc:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print("Multiplication of a and b: ",self.a*self.b)    

class childc(parentc):

    def __init__(self,a,b):
        super().__init__(a,b)
        self.a = a
        self.b = b
        print("Addition of a and b is: ",self.a+self.b)
        print("Multiplication using super() into child class: ",self.a*self.b) 



p1 = childc(2,4)


# Types of Python Inheritance
# Single Inheritance: A child class inherits from one parent class.
# Multiple Inheritance: A child class inherits from more than one parent class.
# Multilevel Inheritance: A class is derived from a class which is also derived from another class.
# Hierarchical Inheritance: Multiple classes inherit from a single parent class.
# Hybrid Inheritance: A combination of more than one type of inheritance.

