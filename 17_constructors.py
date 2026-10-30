class Employee:
    company = "HP" # attribute of the class

    def __init__(self, salary, name, bond): # initializes a new obect from class Employee with given parameters
        self.salary = salary
        self.name = name
        self.bond = bond

    def get_salary(self): 
        return self.salary
        #return 34000

    def get_info(self):
        print(f"The name of the employee is {self.name}. Salary is {self.salary}. The bond is for {self.bond} years.")

e1 = Employee(34000, "John Doe", 4) # This creates an instance of the Employee class with the given salary, name, and bond.
print(e1.get_salary())
e1.get_info()