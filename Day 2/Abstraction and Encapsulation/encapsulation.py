#Here we perform inter-class level encapsulation, where the object can only be accessed by a class or its subclass

class Protected:
    def __init__(self):
        self._id = 1234

class Subclass(Protected):
    def displayid(self):
        print(self._id)

obj=Subclass()
obj.displayid()

#Now let's perform intra-class level encapsulation

class Public:
    def __init__(self):
        self.__id = 5678

    def displayid(self):
        print(self.__id)

obj1=Public()
obj1.displayid() 