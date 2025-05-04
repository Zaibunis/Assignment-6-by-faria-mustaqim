class Dog:
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

    def bark(self):
        print(f"{self.name} says Woof!")

name = input("Enter the dog's name: ")
dog = Dog(name)
dog.bark()