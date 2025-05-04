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
2. Using cls
The cls keyword is used in class methods to refer to the class itself. It enables you to interact with class-level variables and methods.

Example:

python
Copy
Edit
class Counter:
    count = 0
    
    @classmethod
    def increment(cls):
        cls.count += 1
3. Public Variables and Methods
Public variables and methods can be accessed directly from outside the class. These are not restricted and can be modified without limitations.

Example:

python
Copy
Edit
class Car:
    def __init__(self, brand):
        self.brand = brand  # Public variable
    
    def start(self):  # Public method
        print("Car started")
4. Class Variables and Class Methods
Class variables are shared by all instances of the class. Class methods modify or interact with class variables and are defined using the @classmethod decorator.

Example:

python
Copy
Edit
class Bank:
    bank_name = "ABC Bank"
    
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
5. Static Variables and Static Methods
Static variables are shared across all instances of the class, but they do not depend on any instance. Static methods are defined using @staticmethod and do not take self or cls as parameters.

Example:

python
Copy
Edit
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
6. Constructors and Destructors
Constructors (__init__) are used to initialize objects, while destructors (__del__) are called when objects are destroyed, allowing you to perform cleanup tasks.

Example:

python
Copy
Edit
class Logger:
    def __init__(self):
        print("Object created")
    
    def __del__(self):
        print("Object destroyed")
7. Access Modifiers: Public, Private, and Protected
In Python, access modifiers control the visibility of variables and methods. Public members are accessible from outside the class, while private members are intended for internal use.

Example:

python
Copy
Edit
class Employee:
    def __init__(self):
        self.name = "John"  # Public
        self._salary = 50000  # Protected
        self.__ssn = "123-45-6789"  # Private
8. The super() Function
The super() function allows calling a method from the base class. It is useful when working with inheritance and helps avoid explicit calls to the parent class.

Example:

python
Copy
Edit
class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Calling the constructor of Person
        self.subject = subject
9. Abstract Classes and Methods
Abstract classes cannot be instantiated directly and are meant to be subclassed. Abstract methods must be implemented in the subclass. The abc module is used to define abstract classes.

Example:

python
Copy
Edit
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
10. Instance Methods
Instance methods are functions defined within a class that operate on an instance of the class. They are the most commonly used type of method in OOP.

Example:

python
Copy
Edit
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} is barking!")
11. Class Methods
Class methods are used to work with class variables, and they are defined using the @classmethod decorator. They take cls as the first argument to refer to the class.

Example:

python
Copy
Edit
class Book:
    total_books = 0
    
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
12. Static Methods
Static methods are independent of both instance and class variables. They are defined using the @staticmethod decorator and are used for utility functions.

Example:

python
Copy
Edit
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
13. Composition
Composition refers to creating relationships where one class contains objects of other classes. It establishes a "has-a" relationship between the objects.

Example:

python
Copy
Edit
class Engine:
    def start(self):
        print("Engine starting...")

class Car:
    def __init__(self, engine):
        self.engine = engine  # Composition

car = Car(Engine())
car.engine.start()  # Accessing Engine method from Car
14. Aggregation
Aggregation is a special form of association where one class references another, but both can exist independently.

Example:

python
Copy
Edit
class Department:
    def __init__(self, employee):
        self.employee = employee  # Aggregation

class Employee:
    def __init__(self, name):
        self.name = name
15. Method Resolution Order (MRO) and Diamond Inheritance
The Method Resolution Order (MRO) determines the order in which methods are inherited when using multiple inheritance, especially in diamond inheritance scenarios.

Example:

python
Copy
Edit
class A:
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
16. Function Decorators
Decorators are functions that modify or extend the behavior of other functions or methods. They are often used to add additional functionality to a function in a clean and reusable manner.

Example:

python
Copy
Edit
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        func()
    return wrapper

@log_function_call
def say_hello():
    print("Hello!")
17. Class Decorators
Class decorators are used to modify classes, adding or altering methods, or changing the behavior of the class.

Example:

python
Copy
Edit
def add_greeting(cls):
    cls.greet = lambda self: "Hello from Decorator!"
    return cls

@add_greeting
class Person:
    pass
18. Property Decorators: @property, @setter, and @deleter
The @property decorator allows a method to be accessed like an attribute. The @setter decorator is used to update the property, and the @deleter decorator deletes the property.

Example:

python
Copy
Edit
class Product:
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
19. callable() and __call__()
The __call__() method allows an object to be called as if it were a function. The callable() function checks if an object can be called like a function.

Example:

python
Copy
Edit
class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, x):
        return x * self.factor
20. Creating a Custom Exception
Custom exceptions allow you to create more specific error types, making it easier to handle errors in a program. They are raised using the raise statement.

Example:

python
Copy
Edit
class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older")
21. Make a Custom Class Iterable
By implementing __iter__() and __next__() methods, you can make a class iterable, enabling it to be used in a for loop.

Example:

python
Copy
Edit
class Countdown:
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

```
Good luck with your assignments and continue your OOP journey! 🚀

pgsql
Copy
Edit

This version should align better with your request while still keeping the content relevant to your
