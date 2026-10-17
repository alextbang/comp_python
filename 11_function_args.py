def add(a, b, plus=0):      # third parameter is optional, default value is 0
    x = a + b + plus
    return x

c = add(3, 5, 2)
print(c)

c = add(3, 5)
print(c)
