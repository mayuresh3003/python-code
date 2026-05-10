class Demo:
    a = 4

o = Demo()
print(o.a)      # Prints the class attirbute because instance attribute is not present 
o.a = 0         # Instance attribute is set 
print(o.a)      # Prints the instance attributes because instance attribute is present
print(Demo.a)   # Prints the class attribute  