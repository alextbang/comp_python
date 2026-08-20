a = int(input("Enter a lucky number: "))

match a:
    case 122:
        print("the value is 122")
    case 3:
        print("The value is 3")
    case 6:
        print("The value is 6")
    case _:  # default case
        print("Better luck next times")