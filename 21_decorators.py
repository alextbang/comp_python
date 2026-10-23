# Decorator is a function that takes another function as an argument, adds some functionality and returns it.

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

# function to be enhanced by the decorator 
def say_hello():
    print("Hello, World!")

#say_hello()


# you can call the decorator function using the @ symbol before the function definition
@my_decorator
def say_hello():
    print("Hello, World!")

say_hello()

