# Polymorphism

class Cat:
    def speak(self):
        return "Meow"


class Dog:
    def speak(self):
        return "Woof"


animals = [Cat(), Dog()]

for animal in animals:
    print(animal.speak())
