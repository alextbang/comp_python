class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum(self, p): # this does the same thing as __add__ method below, but is not operator overloading, it can't add two Point objects using the + operator
        return Point(self.x + p.x, self.y + p.y) 

    # this is operator overloading, it allows us to use the + operator to add two Point objects where the sum method above does not allow us to do that, we have to call the sum method explicitly
    def __add__(self, p):
            return Point(self.x + p.x, self.y + p.y)   
    
    def print_point(self):
        print(f"X is {self.x}, Y is {self.y}")


p1 = Point(3, 2)
p2 = Point(6, 3)

# p = p1.sum(p2) # Returns a new point which is sum of p1 and p2; the sum method is called on p1 and p2 is passed as an argument   
p = p1 + p2 #this doesn't work because the + operator is not defined for Point objects, but if we define the __add__ method, it will work
p.print_point()

