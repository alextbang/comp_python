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

    @classmethod # this allows the method to be called without creating an instance of the class    
    def print_company(cls):
        print(f"Company: {cls.company}")  # Accessing static variable using class name  

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company  # Changing the value of the static variable using class method
    
e1 = Employee("Jack", 34555)
e2 = Employee("Jill", 34777)
# print(Employee.company)  # Accessing static variable using class name
# # print(Employee.salary) # This will raise an AttributeError since 'salary' is not a class variable

# e1.print_info() # default way to call instance method using object reference
# e2.print_info() 

# print(e2.sum(5, 3))   # Adding @staticmethod decorator allows us to call the method using an instance of the class, but it is not recommended since it can be misleading. It is better to call static methods using the class name. 

#print(Employee.sum(5, 3))  # Correct way to call the static method when using the class name and when no @staticmethod decorator is used.

e1.print_company()  # Adding @classmethod decorator allows us to call the method using an instance of the class, but it is not recommended since it can be misleading. It is better to call class methods using the class name. 

e1.change_company("Acme")
e1.print_company()  # Adding @classmethod decorator allows us to call the method using an instance of the class, but it is not recommended since it can be misleading. It is better to call class methods using the class name.