# Class: Class is a blueprint or a templaet. E.g., a form for an exam that contains name, age, electives, father's name, etc.

# Object: Specific instance created from the template (class). E.g., Form which contains data for John Doe.

class Employee:
    company = "HP" # attribute of the class

    def get_salary(self): # this is the class/object method
        # self is importanat because self is a away to reference the object of the class which is being created
        #print(self)
        return 34000

e = Employee() # an object of class Employee is create here
print(e.get_salary()) # Empoyeee e"s get salary method is called

e2 = Employee()
print(e2.get_salary()) 
print(e2.company)