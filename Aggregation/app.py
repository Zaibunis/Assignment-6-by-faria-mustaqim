class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, employees):
        self.employees = employees
       
employees = Employee("Ali")
d = Department(employees)
print(d.employees)
print(d.employees.name)  # Output: Ali
