# Getters and setters in Python

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property # property decorator allows us to access the 'first_name' method like an attribute         
    def first_name(self):
        l = self.name.split(" ")
        print(l)
        return l[0]
    
    @first_name.setter # setter decorator allows us to set the value of 'first_name' like an attribute
    # def set_first_name(self, first):
    def first_name(self, first):
        l = self.name.split(" ")
        new_name = f"{first} {l[1]}"
        self.name = new_name


e = Employee("Jack Doe", 34555)
# print(e.first_name)
# e.set_first_name = "John"         
# print(e.name) 
# instead of calling the methods directly, we can use property decorator to make it look like an attribute

print(e.first_name)
e.first_name = "John"
print(e.name)