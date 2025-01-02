#List Comprehension - Help create a new smaller list from an existing list
list_name = (1,2,3,1,2,5,1,34,1,34,2,512232,1233,11451)

list_comp = [val for val in list_name if "1" in val] # condition is that the list value has 1 as a part of the value
print("Small list created from: ",list_comp)