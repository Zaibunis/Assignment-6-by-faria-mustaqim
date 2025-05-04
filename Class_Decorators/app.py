def add_greeting(cls):
    cls.greet = lambda self: "Hello from Decorator!"
    return cls

@add_greeting
class Person:
    pass

p = Person()
print(p.greet())
