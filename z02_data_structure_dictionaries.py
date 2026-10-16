dictionary = {
    'weapons': ['bat', 'knife', 'gun'],
    'greeting': 'hello',
    'married': True,
    'age': 67
}

print("age-->",dictionary['age'])
print("dictionary-->",dictionary)
print('dictionary items-->', dictionary.items())

# avoid error accessing dictionary key
print(dictionary.get('species:'))

# assigns default value if it doesn't exist
print(dictionary.get('country', 'USA'))

# check if key/value exists
print("check if 'greeting: hello' exists-->", 'hello' in dictionary.values())
print('size' in dictionary)

# update dictionary key/values
print(dictionary.update({'age': 27}))
print(dictionary)
