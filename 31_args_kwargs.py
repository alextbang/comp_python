# *args
# def order_pizza(size, *toppings): # args can be named anything, like 'toppings'
#     print(f"Orderd a {size} pizza with the following toppings:")
#     for topping in toppings:
#         print(f"Adding {topping}")
# # Python will automatically collect all the additional positional arguments into a tuple for *args .
# order_pizza("large", "pepperoni", "mushrooms", "green peppers")

# **kwargs
def order_pizza(size, *toppings, **details): # kwargs can be named anything, like 'details'
    print(f"Orderd a {size} pizza with the following toppings:")
    for topping in toppings:
        print(f"Adding {topping}")
    print("\nDetails of the order:")
    for key, value in details.items():
        print(f"{key}: {value}")

# Python will automatically collect all the additional keyword arguments like 'delivery' and 'tip' into a dictionary for **kwargs .
order_pizza("large", "pepperoni", "mushrooms", "green peppers", delivery=True, tip=5)