#Inheritance utilizes a pre existing class to inherit its functionalities without need for redundant code
class parentc:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print("Multiplication of a and b: ",self.a*self.b)    

class childc(parentc):
    def __iit__(self,a,b):
        self.a = a
        self.b = b
        print("Addition of a and b is: ",self.a+self.b)



p1 = childc(2,4)