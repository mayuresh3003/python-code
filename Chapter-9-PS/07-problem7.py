line =1 
with open("log.txt") as f: 
    lines = f.readlines()

lineno =1 
for line in lines: 
    if("failed" in line):
        print (f"Yes failed is present. Line no: {lineno}")
        break
    lineno +=1 
else:
    print ("No failed is not present")
 
 