#Decorator is a form of design pattern used to add functionality to the existing object without changing its structure

#Simple Decorator
def num_val(number):
    return number + 1

result = num_val
print(result(4))

#Method Decorator
def func1(number):
    return number + 3

def func2(function):
    val = 22
    return function(val)

print(func2(func1))


