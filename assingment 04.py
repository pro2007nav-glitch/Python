
def fibonacci(n):
    if n < 0:
        return "Please enter a non-negative number"

    a, b = 0, 1

    for i in range(n):
        a, b = b, a + b

    return a


n = int(input("Enter the value of n: "))
print("Fibonacci number:", fibonacci(n))
