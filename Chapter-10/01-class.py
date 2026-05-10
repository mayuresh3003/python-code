class Employee:
    language = "Py"    # This is a class attribute 
    salary = 1200000
    

harry = Employee()
harry.name = "Harry"   # This is an object attribute 
print(harry.name, harry.salary, harry.language)

ron = Employee()
ron.name = "Ron"
print(ron.name, ron.language, ron.salary)

#Here name is object attribute and salary and language are class 
#attributes as they directly belong to the class 