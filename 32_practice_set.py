# write a function that sums all the numbers between 1 and the argument
def sum_numbers(n):
    total = 0
    # range() function in Python does not include the stop number. It is exclusive, meaning it stops just before reaching that number. To add number between 1 and 5, we need to use n + 1 as the stop number.
    for i in range(1, n + 1):
        total += i
    return total

print(sum_numbers(5)) # output: 15
# 1+2+3+4+5=15
