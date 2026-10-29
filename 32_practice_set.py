# write a function that sums all the numbers between 1 and the argument
def sum_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Example usage
print(sum_numbers(3))  # Output: 15