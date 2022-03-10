string=input("Enter a string: ")
if string.endswith("est"):
    print(string)
elif string.endswith("er"):
    print(string.replace("er","est"))
elif len(string)<4:
    print(string)
else:
    print(string + "er")