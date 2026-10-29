# kwargs

def marks(**kwargs):
    # kwargs will be a dictionary containing all the keyword arguments passed to the function.
    for item in kwargs.keys():
        print(f"The marks of {item}: {kwargs[item]}")

marks(math=95, science=88, history=76)