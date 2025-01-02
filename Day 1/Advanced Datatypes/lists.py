#List Declaration
list_name1 = [1,True,"word","word1"]
print("Pre-defined list: ",list_name1,"/n")

#User Defined List
list_name = []
input_range = int(input("Get user input range: "))

for i in range(input_range):
    user_input = input("Enter User Defined Input: ")
    list_name.append(user_input)

print(list_name,"/n")

#Remove List items using index
list_name1.pop(1)
print("List after using pop function: ",list_name1)
del list_name1[0]
print("List after executing del function: ",list_name1)

#List Sorting
list_name1.sort()
print("Sorted List: ",list_name1)




