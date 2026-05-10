class Employee:
    language = "Py"    # This is a class attribute 
    salary = 1200000
    
    def __init__(self): # dunder method which is automatically called 
        print("I am creating an object")    

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    

harry = Employee()
harry.name = "Harry"
print(harry.name, harry.salary)

