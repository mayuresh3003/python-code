a = int(input("Enter your age: "))

#If stament no 1 
if (a%2 == 0):
    print("Your age is even")


#If stament no 2
if (a>=18):
    print("You are an adult")
    print("You can vote")

elif(a<0):
    print("Invalid age")

else:
    print("You are a minor")