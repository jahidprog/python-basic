class Student:
    college_name = "ABC college" # Class Attributes

    def __init__(self, name, gpa): 
        self.name = name # instance attribute
        self.gpa = gpa #instance attribute

stu1 = Student("jahid", 3.22)
print(Student.college_name)
print(stu1.college_name)
print(f"{stu1.name} : {stu1.gpa}")
