age = int(input("What is your age? "))

if (age > 18):
    print("You can drive!")
elif (age == 18):
    print("Let's schedule an appointment")
elif (age == 0):
    print("You were just born!")
else:
    print("You are too young to drive.")