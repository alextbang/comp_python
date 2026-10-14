# lambda functions are simple, anonymous inlinefunctions defined using the `lambda` keyword. They can take any number of arguments but can only have one expression.

# take a single argument X and return its square
square = lambda x: x * x
print(square(5))  # Output: 25
# this is equivalent to:
# def square(x):
#     return x * x
# print(square(5))  # Output: 25

# take two arguments X and Y and return their sum
add = lambda x, y: x + y
print(add(3, 7))  # Output: 10

