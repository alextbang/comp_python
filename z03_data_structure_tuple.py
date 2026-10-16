# tuple is an immutable list.

my_tuple = (1,2,3,4,5)
x = my_tuple[1]
print(x)

x,y,z, *other = (2,4,6, 8, 10)
print('other-->', other)