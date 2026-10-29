# args

def sum(*args): # the * unpacks the arguments into a tuple
    # args will be a tubple containing all the positional arguments passed to the function.
    total = 0
    for number in args:
        total += number
    return total    

print(sum(1, 2, 3, 4))
print(sum(10, 20, 30))
print(sum())