# reduce applies a function cumulatively to the items of an iterable, reducing it to a single value.

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

def sum(a, b):
    return a + b

# reduce method applies the function repeatedly to the items of the iterable; it addS the first two items, then adds the result to the next item, and so on, until a single value is obtained.
total = reduce(sum, numbers)
print("Sum of numbers:", total)

