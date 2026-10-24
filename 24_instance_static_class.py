class Employee:
    company = "HP"  # Static/Class variable

    def __init__(self, name, salary):
        self.name = name  # Instance variable
        self.salary = salary  # Instance variable

    # instance method to print employee information
    def print_info(self):
        info = f"Name: {self.name}, Salary: {self.salary}, Company: {Employee.company}"  # Accessing static variable using class name
        print(info)

    @staticmethod # this allows the method to be called without creating an instance of the class
    def sum(a, b):
        return a + b
e1 = Employee("Jack", 34555)
e2 = Employee("Jill", 34777)
print(Employee.company)  # Accessing static variable using class name
# print(Employee.salary) # This will raise an AttributeError since 'salary' is not a class variable

e1.print_info()
e2.print_info() 

print(e2.sum(5, 3))   # This will raise a TypeError since 'sum' is not an instance method and should be called using the class name, unless you add @staticmethod decorator to the method definition.

#print(Employee.sum(5, 3))  # Correct way to call the static method when using the class name and when no @staticmethod decorator is used.