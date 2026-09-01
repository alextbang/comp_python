# s = "hello world"
# # s[0] = "R" # can't do this; strings are immutable

# a = len(s) 
# print("string length:", a)
# print(s.upper(), "but string not changed:", s)

##########

# text = "Apples, Bananas, Pineapples"
# print(text.split(",")) # will create a list separating on ","
# var = (",".join(['Apples', 'Bananas', 'Pineapples'])) # creates a list string
# print(type(var))

###########

# String formatting

a = "Harry"
b = "Sally"
m = 1000
print(f"{a} and {b} you are awesome. Take this ${m} prize.")
# inputs variables 
