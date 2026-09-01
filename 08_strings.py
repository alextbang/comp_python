name = "Philadelphia"

# string index
print(name[0]) #prints 0 index, or first string character
print(name[2]) 

print(name[-1], "index -1") #count backwards from the last string index
print(name[-3], "index -3")

# string slicing
print(name[0:2]) # prints from 0 index and stops before index 2.
print(name[2:-1]) # same as name[2:4]

# print(name[0:10:n]) # skip n-1 character
print(name[0:10:3], "skip 2 characters") # skip 3-1, i.e., 2 characters

print(name[:4])
print(name[1:])