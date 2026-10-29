# # map, filter, and reduce work on iterables (like lists, tuples, etc.)

# # map applies a function to all items in the input list
# numbers = [1, 2, 3, 4, 5]
# def square(x):
#     return x ** 2

# # by default, map returns an iterator, so we convert it to a list
# # new = map(square, numbers)
# new = list(map(square, numbers)) # you map or apply the function to each item in the list
# print("Squared numbers:", new)


### 

# # filter

# def is_greater_than_9(x):
#     if x > 9:
#         return True
#     else:
#         return False
    
# a = [1, 3, 5, 324, 45, 32, 943754, 56, 2, 5, 6, 7, 42]

# # new = list(filter(is_greater_than_9, a))
# new = list(filter(lambda x: x > 9, a))  # use lambda function to reduce the length of the code when it is clear

# print("Numbers greater than 9:", new)

### 



