from abc import ABC, abstractmethod

#ABC = Abstract Base Class

#@abstractmethod = decorator to mark a method that must be implemented

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
        
r = Rectangle(10, 20)
print(r.area())
        
class Circle(Shape):
     def __init__(self,radius):
          self.radius = radius

     def area(self):
          return 3.14 *  self.radius
     
c = Circle(10)
print(c.area())