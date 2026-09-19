# Classes & Objects

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"I'm {self.name}, {self.age} years old."


student = Student("Jahid", 25)

print(student.name)
print(student.introduce())
