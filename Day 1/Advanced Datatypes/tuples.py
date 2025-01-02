#Tuple Declaration
tuple_name = ("word","word2","word3",1,2,3,4,1,2,3,1,2,1,5,1)
print(tuple_name)

#User Defined Tuple
user_input = input("Add all the tuple elements seperated by commas: ")
tuple_values = user_input.split(",")
tuple_name1 = (tuple_values)
print(tuple_name1)

#Count
print("Count the number of 1s in the tuple: ",tuple_name.count(1))