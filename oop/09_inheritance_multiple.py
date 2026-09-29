class Teacher:
    def __init__(self, salary):
        self.salary = salary

class Student:
    def __init__(self, gpa):
        self.gpa = gpa

class TA(Teacher, Student):
    def __init__(self, salary, gpa, name):
        super().__init__(salary)
        Student.__init__(self, gpa)
        self.name = name

ta1 = TA(25_000, 3.22, "jahid")
print(f"Name: {ta1.name}\nSalary is: {ta1.salary}\nGPA: {ta1.gpa}") 