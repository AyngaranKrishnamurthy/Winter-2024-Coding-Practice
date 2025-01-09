#Python Magic methods are the methods starting and ending with double underscores ‘__’. 
#They are defined by built-in classes in Python and commonly used for operator overloading.

class magic():
    def __init__(self,str):
        self.str = str
    
    def __repr__(self):
        print(self.str)

obj = magic("Hello")
obj.__repr__()