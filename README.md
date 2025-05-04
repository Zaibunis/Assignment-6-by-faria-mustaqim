# 06_Complete_Traditional_OOP_Practice_Series_With_Composition_And_Decorators

This document provides an explanation guide for various Python Object-Oriented Programming (OOP) concepts. The assignments are structured to help you understand the key principles of OOP and their practical applications, covering both fundamental and advanced features.

---

## 1. **Using `self`**

In Python, the `self` keyword is used to reference the current instance of a class. It is essential in initializing and manipulating instance variables and calling instance methods.

Example:
```python
class Student:
    def __init__(self, name, marks):
        self.name = name  # Instance variable
        self.marks = marks  # Instance variable

```
## 2. **Using `cls`**

The cls keyword is used in class methods to refer to the class itself. It enables you to interact with class-level variables and methods.

Example:
```class Counter:
    count = 0
    
    @classmethod
    def increment(cls):
        cls.count += 1

```

## 3. **Public Variables and Methods**
Public variables and methods can be accessed directly from outside the class. These are not restricted and can be modified without limitations.

Example:
```class Car:
    def __init__(self, brand):
        self.brand = brand  # Public variable
    
    def start(self):  # Public method
        print("Car started")

```

## 4. **Class Variables and Class Methods**
Class variables are shared by all instances of the class. Class methods modify or interact with class variables and are defined using the @classmethod decorator.

Example:
```class Bank:
    bank_name = "ABC Bank"
    
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

```

5. Static Variables and Static Methods
Static methods are related to the class itself and do not require an instance to access. They are defined with the @staticmethod decorator.

```class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

```
6. Constructors and Destructors
Constructors are used to initialize an object, while destructors are used for cleaning up when the object is destroyed.

```class Logger:
    def __init__(self):
        print("Object created")
    
    def __del__(self):
        print("Object destroyed")

```
        
7. Access Modifiers: Public, Private, and Protected
Public variables and methods can be accessed from outside the class. Protected variables are meant for internal use, while private variables cannot be accessed directly from outside the class.

```class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name        # Public
        self._salary = salary   # Protected
        self.__ssn = ssn        # Private

```
        
8. The super() Function
The super() function is used to call methods from the parent class, which is useful when you override methods in child classes but still want to access the functionality of the parent class.

```class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

```
        
9. Abstract Classes and Methods
Abstract classes contain abstract methods that must be implemented in child classes. They cannot be instantiated directly.

```from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

```
        
10. Instance Methods
Instance methods are regular methods that operate on object-level data. They always take self as the first argument.

```class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} is barking!")

```
        
11. Class Methods
Class methods are methods that take cls as the first parameter and operate on class-level data. They are marked with the @classmethod decorator.

```class Book:
    total_books = 0
    
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

```
        
12. Static Methods
Static methods don’t take self or cls as parameters and can be called on both the class and instances. They are defined using the @staticmethod decorator.

```class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

```
        
13. Composition
Composition is when one object contains another object as part of it. It represents a "has-a" relationship.

```class Engine:
    def start(self):
        print("Engine started")
    
class Car:
    def __init__(self, engine):
        self.engine = engine
    
    def start_car(self):
        self.engine.start()

```
        
14. Aggregation
Aggregation is when one object refers to another object, but they are independent. It represents a "has-a" relationship.

```class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, employee):
        self.employee = employee

```
        
15. Method Resolution Order (MRO) and Diamond Inheritance
MRO determines the order in which methods are inherited. In diamond inheritance, when a class inherits from two classes that inherit from the same base class, MRO defines the order of method resolution.

```class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

d = D()
d.show()  # Outputs "B"
`
```

16. Function Decorators
Function decorators are functions that modify the behavior of other functions. They are defined using the @ syntax.

```def log_function_call(func):
    def wrapper():
        print("Function is being called")
        return func()
    return wrapper

@log_function_call
def say_hello():
    print("Hello!")

```
    
17. Class Decorators
Class decorators are used to modify the behavior of classes, similar to function decorators.

```def add_greeting(cls):
    cls.greet = lambda self: "Hello from Decorator!"
    return cls

@add_greeting
class Person:
    pass

```
    
18. Property Decorators: @property, @setter, and @deleter
Property decorators are used to manage attribute access. @property is used to get a value, @setter is used to set a value, and @deleter is used to delete the value.

```class Product:
    def __init__(self, price):
        self._price = price
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        self._price = value
    
    @price.deleter
    def price(self):
        del self._price

```
        
19. callable() and __call__()
__call__() allows objects to be used as functions. callable() checks whether an object is callable.

```class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, x):
        return x * self.factor

m = Multiplier(5)
print(callable(m))  # True
print(m(10))         # 50

```

20. Creating a Custom Exception
Custom exceptions are user-defined error types. You can create your own exceptions for specific situations.

```class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above")

```
        
21. Make a Custom Class Iterable
Making a class iterable allows you to use it in a for loop. This is done by implementing the __iter__() and __next__() methods.

```class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        else:
            current = self.current
            self.current -= 1
            return current

for num in Countdown(5):
    print(num)


```
Conclusion
In this guide, we covered important Python OOP (Object-Oriented Programming) concepts with examples to help you understand how to use them. By completing these assignments, you learned how to:

Use instance and class variables (self, cls).

Work with public, private, and protected variables.

Apply inheritance, abstract classes, and method resolution order (MRO).

Use decorators to modify classes and functions.

Understand composition and aggregation to connect different objects.

Create custom exceptions and iterable objects.

Use Python's built-in functions like callable() and __call__() to make objects more flexible.

These concepts will help you write cleaner and more organized code. Keep practicing, and you'll get even better at Python!

Good luck and happy coding! 🚀
