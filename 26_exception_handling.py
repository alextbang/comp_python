# while True:
#     # wrap the input and calculation in a try-except block to handle invalid input
#     try:
#         a = int(input("Enter number 1: "))   
#         b = int(input("Enter number 2: "))
#         print(f"the division is {a / b}")    

#     # cathch different error types
    
#     # catch ValueError exception if the user enters invalid input
#     except ValueError as e:
#         print(f"Invalid input given. Error: {e}")
#     # catch ZeroDivisionError exception if the user tries to divide by zero
#     except ZeroDivisionError as e:
#         print(f"Cannot divide by zero. Error: {e}")
#     # catch any other exceptions that may occur
#     except Exception as e:
#         print(f"Invalid input given. Error: {e}")


# # Allow user to exit
#     exit_choice = input("Do you want to exit? (yes/no): ")
#     if exit_choice.lower() == "yes":
#         break
#     else:
#         continue

###

# You can also raise an error explicitly using the raise statement and exit the program if needed

a = int(input("Enter number 1: "))   
b = int(input("Enter number 2: "))

if b == 0:
    raise ZeroDivisionError("Dude you cannot divide by zero")    

print(f"the division is {a / b}")
