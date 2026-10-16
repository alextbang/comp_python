
def sum(a, b):
    '''This will sum two numbers.''' # doc string
    c = a + b
    # z = 1 # it creates a local variable called z
    # print("local z-->", z)
    global z # modifies global variable outside the function
    z = 20
    return c

print(sum.__doc__) # print doc string
print(sum(4, 6))

# variable c is out of scope
# print(c)

print("global z-->", z)

########

