def sum(a, b):
    c = a + b
    z = 1 # it creates a local variable called z
    return c

print(sum(4, 6))

# variable c is out of scope
# print(c)

z = 8 # z is a global variable
print(z)

