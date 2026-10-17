class Employee:
    company = "Asus" # attribute of the class

    def __init__(self, salary, name, bond, company): # initializes a new obect from class Employee with given parameters
        self.salary = salary
        self.name = name
        self.bond = bond
        self.company = company

    def get_salary(self): 
        return self.salary
        #return 34000

    def get_info(self):
        print(f"The name of the employee is {self.name}. Salary is {self.salary}. The bond is for {self.bond} years.")

e1 = Employee(34000, "John", 3, "Tesla")
print(e1.company) # will always print instance attribute when present
print("Class attribute company-->", Employee.company)

#print(dir(e1))   /Object introspection; prints all class methods 