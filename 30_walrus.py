# walrus operator (:=) allows you to assign a value to a variable as part of an expression. It is useful for writing more concise code, especially in conditions and loops.

# foods = list()
# while True:
#     food = input("Enter a food: ")
#     if food == "quit":
#         break
#     foods.append(food)

# print("Foods entered:", foods)

# The above code can be rewritten using the walrus operator to make it more concise:
foods = list()
while (food := input("Enter a food: ")) != "quit":
    foods.append(food)

print("Foods entered:", foods)  