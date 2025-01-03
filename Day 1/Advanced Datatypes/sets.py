#Set Declaration
set_name = {"abc","def","ijk"}
set_name = set(("lmn","opq","rst",4,3,1,5))

print(set_name)

#Check if a value is in the set
print("opq" in set_name)

#add items to set
set_name.add("uvw")
print("Set after adding a new value", set_name)

#remove items from set
set_name.discard("opq")
print("Set after discarding a value", set_name)

#clear() and del keywords can be used to clear or delete a set

# There are several ways to join two or more sets in Python.
# The union() and update() methods joins all items from both sets.
# The intersection() method keeps ONLY the duplicates.
# The difference() method keeps the items from the first set that are not in the other set(s).
# The symmetric_difference() method keeps all items EXCEPT the duplicates.

#Joining Sets
set_name1 = {1,2,3,4,5,6}

set_name2 = set_name.union(set_name1)
print("Set result after Union ", set_name2)

set_name3 = set_name.intersection(set_name1)
print("Set result after Intersection ", set_name3)

set_name4 = set_name.difference(set_name1)
print("Set result after Difference ", set_name4)

set_name5 = set_name.symmetric_difference(set_name1)
print("Set result after Symmetric Difference ", set_name5)
