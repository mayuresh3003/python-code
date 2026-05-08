'''
1 for snake
-1 for water
0 for gun

'''

import random

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "snake", -1: "water", 0: "gun"}
you = youDict[youstr]

print(f"Computer chose {reverseDict[computer]} and you chose {reverseDict[you]}")

if computer == you:
    print("It's a tie!")

elif (you == 1 and computer == -1) or (you == -1 and computer == 0) or (you == 0 and computer == 1):
    print("You win!")  

elif (you == 1 and computer == 0) or (you == -1 and computer == 1) or (you == 0 and computer == -1):
    print("Computer wins!")

else:
    print("Invalid input! Please enter 's' for snake, 'w' for water, or 'g' for gun.")


