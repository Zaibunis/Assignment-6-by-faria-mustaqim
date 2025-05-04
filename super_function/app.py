class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Teacher(Person):
        def __init__(self, name, age, subject):
            super().__init__(name, age)
            self.subject = subject

t = Teacher("Alice",35,"Mathematics")
print(t.name, t.subject)
