n = int(input("Enter a number: "))

for i in range(2,n):
    if (n % i == 0):
        print("Number is not prime")
        break
else:
    print("Number is prime")
# In this code snippet, we first take an integer input from the user and store it in the variable n. Then, we use a for loop to iterate over the range of numbers starting from 2 up to n-1. Inside the loop, we check if n is divisible by any of these numbers (i). If n is divisible by any number in this range, it means that n is not a prime number, and we print "Number is not prime" and break out of the loop. If the loop completes without finding any divisors (i.e., n is not divisible by any number in the range), the else block is executed, and we print "Number is prime".
