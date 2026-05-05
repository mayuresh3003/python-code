for i in range(100):
    if i == 35:
        break
    print(i)
# In this code snippet, we have a for loop that iterates over the range of numbers from 0 to 99. Inside the loop, there is an if statement that checks if the current value of i is equal to 35. If it is, the break statement is executed, which immediately exits the loop. This means that the loop will stop executing once it reaches the number 35, and any numbers after 35 will not be printed. Therefore, this code will print the numbers from 0 to 34, and then it will stop without printing any further numbers.


for i in range(100):
    if i == 35:
        continue # skips the current iteration and moves to the next one
    print(i)

