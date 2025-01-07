#Polymorphism means many forms, we have many pre existing polymorhic functions like len() method
#But for user defined we can utilize class level polymorphism
#Where different classes have methods having same name but performing different functions

class CS:
    def __init__(self,id,name):
        self.id = id
        self.name = name

    def data(self):
        dict_name = {
            "Student Id" : self.id,
            "Student Name" : self.name,
            "College" : "College of Sciences",
            "Department" : "Computer Science",
            "Building" : "ECS"
        }
        print(dict_name)


class BM:
    def __init__(self,id,name):
        self.id = id
        self.name = name

    def data(self):
        dict_name = {
            "Student Id" : self.id,
            "Student Name" : self.name,
            "College" : "Batten College of Engineering",
            "Department" : "Bio Mechanics",
            "Building" : "Engineering Building"
        }
        print(dict_name)

CSstudent = CS(123,"Ayngaran")
BMStudent = BM(456,"Abed")

for x in (CSstudent,BMStudent):
  x.data()