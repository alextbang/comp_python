# fibonacci series using recursion, i.e., a function that calls itself to calculate the nth Fibonacci number.

def fibonacci(n):
    # base case of recursion
    if (n == 0 or n == 1):
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  # Output: 8
