with open("log.txt") as f: 
    content = f.read()

if("failed" in content):
    print ("Yes failed is present")
else:
    print ("No failed is not present")
 