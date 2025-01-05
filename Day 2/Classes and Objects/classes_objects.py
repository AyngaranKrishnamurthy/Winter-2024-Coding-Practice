#A class is a blueprint for creating objects. In python almost everything is an object with its properties and methods

#Class Declaration
class class_name:
    def __init__(self,a,b):
        self.a = a+b

    

#Object Declaration (Creating a object using class we created)
add = class_name(9,8)

print("Value of addition: ",add.a)

#We can also define a __str__ within a class that can help to return a value
class class_name1:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"Value of subtracting a and b is: {self.a-self.b}"

sub = class_name1(9,7)
print(sub)