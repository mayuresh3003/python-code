n = int(input("Enter a number: "))
product = 1
for i in range(1, n+1):
    product = product * i
print(product)
# In this code snippet, we first take an integer input from the user and store it in the variable n. We then initialize a variable product to 1. We use a for loop to iterate over the range of numbers from 1 to n (inclusive). Inside the loop, we multiply the current value of product with i and update product with the new value. After the loop completes, we print the final value of product, which will be the factorial of n. For example, if the user enters 5, the output will be 120 (since 5! = 5 x 4 x 3 x 2 x 1 = 120).
