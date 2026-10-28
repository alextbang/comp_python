'''
try:
    a = 345/10

except Exception as e:
    print(f"An error occurred: {e}")

# Gets executed if no exception occurs
else:
    print("No error. Hey I am good")
    '''

#
a = int(input("Enter number 1: "))   
b = int(input("Enter number 2: "))

try:
    c = a / b
    print("Division is: ", c)

except Exception as e:
    print(f"An error occurred: {e}")

# use the keyword finally instead of print statements at the end of the program because print statements at the end of the program may not get executed if try except code block is inside a function or if the program exits early.
finally:
    print("This is always excuted. Program completed.")