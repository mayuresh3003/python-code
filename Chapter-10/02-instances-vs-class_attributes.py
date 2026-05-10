class Employee:
    language = "Py"    # This is a class attribute 
    salary = 1200000
    
    def getInfo():
        print(f"The language is {language}. The salary is {salary}")
    

harry = Employee()
harry.language = "JavaScript"   # This is an object attribute 
harry.getInfo()