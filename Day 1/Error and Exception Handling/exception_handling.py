#Error message

list = [1,2,3]
print(list[3])
#To continue execution post the error. Comment the above line(Line 5) with hash "#"

#Error Handling
print("Execution of try..except \n")
try:
    print(list[3])
except:
    print("Something went wrong")
    

#Using a else block helps in user defined execution details
print("Execution of try..except with else block \n")
try:
    print("Run to server code")
except:
    print("Error running to server")
else:
    print("Server code ran successfully")

#Like Java we can use a finally block, to execute even if the exection works fine or fails
print("Execution of try..except with finally block \n")
try:
    print(list(4))
except:
    print("Error running to server")
else:
    print("Server code ran successfully")
finally:
    print("Log the output to server")

#Using raise we can even raise user defined exception, for example
print("Execution of user defined exception \n")
val = "Hello World"
if val is "Hello World":
    raise Exception("Invalid String Value")

#We can also use predefined exceptions for the raise exception calls, to exceute the following comment lines 39 and 40
if val is "Hello World":
    raise SyntaxError("Invalid String Syntax")