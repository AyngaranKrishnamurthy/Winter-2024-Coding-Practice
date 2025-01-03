#Dictionary Declaration
student = {
    "Name" : "Ayngaran Krishnamurthy",
    "UIN" : "01276065"
}

dict_name = {
    "University" : "Old Dominion University",
    "College" : "College of Sciences",
    "Department" : "Computer Science",
    "Student" : student

}

print(dict_name)

#Get Specific Value
print(dict_name.get("Student"))

#Get all key values of the dictionary
print(dict_name.keys())

#Update Dictionary Values
dict_name.update({"Department":"Engineering"})
print(dict_name)

#Add values to dictionary
dict_name["Status"] = "International Student"
dict_name.update({"Visa Status": "F1"})
print(dict_name)

#User Defined Dictionary
my_dict = {}

while True:
    key = input("Enter a key (or 'q' to quit): ")
    if key == 'q':
        break

    value = input("Enter a value: ")
    my_dict[key] = value

print("User Defined dictionary:", my_dict)