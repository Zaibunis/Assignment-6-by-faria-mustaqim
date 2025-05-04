class Employee:
    def __init__(self):
        self.name = "John Doe"
        self._salary = 50000  
        self.__ssn = "123-45-6789"

e = Employee()
print(e.name)  # Public attribute, accessible
print(e._salary)   
print(e._Employee__ssn)  
#print(e.__ssn)  # Private attribute, not accessible directly

        
