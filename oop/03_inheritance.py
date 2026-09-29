# Inheritance

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return "Some sound"


# class Dog(Animal):
#     def speak(self):
#         return "Woof!"


# dog = Dog("Buddy")

# print(dog.name)
# print(dog.speak())

class Employee: #parent/base class
    starting_time = "10am"
    ending_time = "6pm"

    def change_end_time(self, new_ending_time):
        self.ending_time = new_ending_time

class Teacher(Employee): #child/derived class
    def __init__(self, subj):
        self.subj = subj
    def get_info(self):
        print(f"Subject is {self.subj} and ending time is {self.ending_time}")

class AdminStuff(Employee):
    def __init__(self, role):
        self.role= role

class Acountant(AdminStuff):
    def __init__(self, salary, role):
        super().__init__(role)
        self.salary = salary

# t1 = Teacher("Math")
# t1.change_end_time("5pm")
# t1.get_info()

stuff1 = AdminStuff("manager")
print(stuff1.role, stuff1.starting_time, stuff1.ending_time)

acc1 = Acountant(25_000, "CA")
print(acc1.role, acc1.salary, acc1.starting_time, acc1.ending_time)
