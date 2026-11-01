
import time

# Non-Recursive Function
def fibonacci_non_recursive(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()


# Recursive Function
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# Main Program
n = int(input("Enter the number of terms: "))

if n <= 0:
    print("Enter a positive number.")
else:
    # Non-Recursive Execution Time
    before = time.time()
    print("\nNon-Recursive Fibonacci Series:")
    fibonacci_non_recursive(n)
    after = time.time()

    print("Before time:", before)
    print("After time:", after)
    print("Execution time:", after - before, "seconds")

    # Recursive Execution Time
    before = time.time()
    print("\nRecursive Fibonacci Series:")
    for i in range(n):
        print(fibonacci_recursive(i), end=" ")
    print()
    after = time.time()

    print("Before time:", before)
    print("After time:", after)
    print("Execution time:", after - before, "seconds")
