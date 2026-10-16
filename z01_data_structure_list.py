# list can be modified
basket = [1, 2, 3, 4]

new_list = print(basket.append(100))

# append changes the list in place, does not create a new list
print("basket -->", basket)
# new_list will not be printed
print("new_list -->" , new_list)

#to create a new_list, you must reassign the original list
new_list = basket

print("new_list -->",new_list)

# review list methods: pop, remove, insert, extend, slice

############ more list methonds

container = ['a','b','c','d','e']
print("container -->", container)

# sort alphabetically or numerically
container.sort()

container.reverse()
print(container)

print(len(container))

############# join method

sentence = ' '
new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'Bob'])

print("new_sentence:",new_sentence)

########### list unpacking
box = [1, 2, 3]

a,b,c, *other = [1, 2, 3, 4, 5, 6, 7, 8]
print(a)
print(b)
print(c)
print("other-->",other)

