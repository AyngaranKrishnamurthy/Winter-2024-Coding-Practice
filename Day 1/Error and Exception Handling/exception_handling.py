#Error message

list = [1,2,3]

#print(list[3])
#To continue execution post the error. Comment the above line(Line 5) with hash "#"

#Error Handling

try:
    print(list[1])
except:
    print("Something went wrong")
    

#Using a else block helps in user defined execution details
try:
    print("Run to server code")
except:
    print("Error running to server")
else:
    print("Server code ran successfully")