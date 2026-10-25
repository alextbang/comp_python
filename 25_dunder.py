# Dunder methods are special methods in Python that have double underscores at the beginning and end of their names. They are also known as "magic methods" or "special methods". These methods allow you to define how your objects behave with built-in operations, such as addition, subtraction, string representation, and more.   

class Employee:
    company = "HP"  # Static/Class variable
    def __init__(self, name, salary):
        self.name = name  # Instance variable
        self.salary = salary  # Instance variable   

    def __str__(self):
        return f"The name is {self.name} and the salary is {self.salary}"  # Accessing static variable using class name

    def __repr__(self):
        return f"name: {self.name}, salary: {self.salary}"  # Accessing static variable using class name

    
e = Employee("Jack", 34555)
print(e.name, e.salary) 
print(str(e))  # This will call the __str__ method and print the string representation of the object
print(repr(e))  # This will call the __repr__ method and print the string representation of the object. __repr__ is used for debugging and development, while __str__ is used for creating output for end users. If __str__ is not defined, Python will use __repr__ as a fallback.