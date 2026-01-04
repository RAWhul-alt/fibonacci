def fibonacci_iterative(n):
    a, b = 0, 1
    print("Fibonacci series using iteration:")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
n = int(input("Enter the number of terms: "))
fibonacci_iterative(n)
print("Fibonacci series using recursion:")
for i in range(n):
    print(fibonacci_recursive(i), end=" ")
