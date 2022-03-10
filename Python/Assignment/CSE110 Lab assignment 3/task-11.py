string=input("Ente a string: ")
letter=input("Enter a letter: ")
ind=0
n=1
if letter in string:
    print(string.replace(letter,""))
elif letter not in string and len(string)>3:
    print(string[1:len(string)-1:])
else:
    print(string)