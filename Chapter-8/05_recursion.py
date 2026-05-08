'''

factorial(1) = 1
factorial(2) = 2 * factorial(1) = 2 * 1
factorial(3) = 3 * factorial(2) = 3 * 2 * 1
factorial(4) = 4 * factorial(3) = 4 * 3 * 2 * 1
factorial(5) = 5 * factorial(4) = 5 * 4 * 3 * 2 * 1

factorial(n) = n * n-1 * n-2 * n-3 * ... 3 * 2 * 1

factorial(n) = n * factorial(n-1)

'''
def factorial(n):
    if (n == 1 or n == 0):
        return 1
    return n * factorial(n-1)

n = int(input("Enter your number: "))
print(f"The factorial of {n} is: {factorial(n)}")
