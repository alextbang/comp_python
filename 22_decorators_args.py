# To create a decorator that takes arguments, we need to define a function that returns a decorator function. Here's an example of how to create a decorator that repeats the execution of a function n times:

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

# function to be enhanced by the decorator
@repeat(3)
def say_hello():
    print("Hello, World!")  

say_hello()  # This will print "Hello, World!" three times      

