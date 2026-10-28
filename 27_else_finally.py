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

finally:
    print("This is always excuted. Program completed.")