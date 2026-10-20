class Animal: # Parent class (superclass)
    location = "Australia"
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("speaking now...")

class Dog (Animal): # Dog inherits from Animal class; a child class (subclass) is created
    def speak(self):
        super().speak() # call method from parent class
        print("Dog.speak-->","Woof")

# a = Animal("Dog")
# a.speak()

d = Dog("Bruno") # Dog class inherits from parent class Animal
d.speak()
print(d.location)