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
Static variables and methods are related to the class itself, but they don’t need an instance to be accessed. They are independent of the object state.

Example:
python
Copy
Edit
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
6. Constructors and Destructors
Constructors are used to initialize an object, while destructors are used to clean up when an object is destroyed.

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
Public variables and methods can be accessed from outside the class. Protected variables are typically meant for internal use, and private variables are meant to be inaccessible from outside the class.

Example:
python
Copy
Edit
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name        # Public
        self._salary = salary   # Protected
        self.__ssn = ssn        # Private
8. The super() Function
The super() function is used to call methods from the parent class. It is useful when overriding methods in child classes but still wanting to access the parent class functionality.

Example:
python
Copy
Edit
class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
9. Abstract Classes and Methods
Abstract classes cannot be instantiated directly. They contain abstract methods that must be implemented by child classes.

Example:
python
Copy
Edit
from abc import ABC, abstractmethod

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
10. Instance Methods
Instance methods work with object-level data. These methods are defined within a class and take self as the first argument.

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
Class methods are defined with the @classmethod decorator and are used to modify class-level variables or to perform class-specific actions.

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
Static methods are methods that don’t modify object or class state. They are defined with the @staticmethod decorator.

Example:
python
Copy
Edit
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
13. Composition
Composition is when one object contains another object as a part of it. It represents a "has-a" relationship.

Example:
python
Copy
Edit
class Engine:
    def start(self):
        print("Engine started")
    
class Car:
    def __init__(self, engine):
        self.engine = engine
    
    def start_car(self):
        self.engine.start()
14. Aggregation
Aggregation is when one object refers to another object but they are not necessarily dependent on each other. It represents a "has-a" relationship.

Example:
python
Copy
Edit
class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, employee):
        self.employee = employee
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
