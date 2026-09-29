# Polymorphism --> Duck Typing

class Teacher():
    def get_designation(self):
        print("Designation is: Teacher")

class Accountant:
    def get_designation(self):
        print("Designation is: Accountant")

t1 = Teacher()
t1.get_designation()

acc1 = Accountant()
acc1.get_designation()