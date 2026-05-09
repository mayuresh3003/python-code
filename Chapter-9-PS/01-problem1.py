f = open("poem.txt")
content = f. read()
if ("Twinkle" in content):
    print("Twinkle is present in content")
else:
    print("Twinkle is not present in the content")
f.close()