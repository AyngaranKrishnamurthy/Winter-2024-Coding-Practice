#Two or more methods have the same name but different numbers of parameters or different types of parameters, or both. 
#These methods are called overloaded methods and this is called method overloading. 

def department(id,type):
    dict_name = {
        "id" : id,
        "Department" : "Chemistry",
        "Course Type" : type
    }
    print(dict_name)

def department(id,type,course):
    dict_name = {
        "id" : id,
        "Course Type" : type,
        "Course" : course,
        "Department" : "Computer Science"
    }
    print(dict_name)

department(1234,"Project","Cyber Security")
