n = int(input("Enter a number: "))

i = 1
while i < 11:
    print(f"{n} x {i} = {n*i}")
    i += 1

# In this code snippet, we first take an integer input from the user and store it in the variable n. Then, we initialize a variable i to 1. We use a while loop that continues as long as i is less than 11. Inside the loop, we print the multiplication of n with the current value of i in a formatted string. After printing, we increment i by 1 to move to the next number. This will output the multiplication table for the number n from 1 to 10. For example, if the user enters 5, the output will be: 